import logging
import time
from dataclasses import dataclass
from typing import Dict, Generator, Iterable, Optional, Set, cast

import numpy as np
import torch
from librosa import get_duration  # pylint: disable=no-name-in-module
from torch import LongTensor

from tacotron.audio_utils import mel_to_numpy
from tacotron.checkpoint_handling import (CheckpointDict, get_duration_mapping, get_hparams,
                                          get_speaker_mapping, get_stress_mapping,
                                          get_symbol_mapping, get_tone_mapping)
from tacotron.frontend.main import get_map_keys, get_mapped_indices, get_mappings_count
from tacotron.globals import NOT_INFERABLE_SYMBOL_MARKER
from tacotron.model import Tacotron2
from tacotron.training import load_model, try_get_mappings_count
from tacotron.typing import Duration, Speaker, Stress, Symbol, SymbolMapping, Symbols, Tone
from tacotron.utils import (console_out_len, find_indices, get_default_device, get_items_by_index,
                            init_global_seeds, overwrite_custom_hparams, try_copy_to)


@dataclass
class InferenceResult():
  sampling_rate: int
  reached_max_decoder_steps: bool
  inference_duration_s: float
  mel_outputs_postnet: np.ndarray
  mel_outputs: Optional[np.ndarray]
  gate_outputs: Optional[np.ndarray]
  alignments: Optional[np.ndarray]
  unmappable_symbols: Optional[Set[Symbol]]
  unmappable_stresses: Optional[Set[Stress]]
  unmappable_tones: Optional[Set[Tone]]
  unmappable_durations: Optional[Set[Duration]]
  duration_s: float


def get_symbols_noninferable_marked(symbols: Iterable[Symbol], symbol_mapping: SymbolMapping) -> Generator[Symbol, None, None]:
  marker = NOT_INFERABLE_SYMBOL_MARKER
  result = (symbol if symbol in symbol_mapping else marker * console_out_len(symbol)
            for symbol in symbols)
  return result


class Synthesizer():
  def __init__(self, checkpoint: CheckpointDict, custom_hparams: Optional[Dict[str, str]] = None, device: torch.device = get_default_device()):
    self.device = device

    hparams = get_hparams(checkpoint)
    hparams = overwrite_custom_hparams(hparams, custom_hparams)
    self.hparams = hparams

    symbol_mapping = get_symbol_mapping(checkpoint)
    self.symbol_mapping = symbol_mapping

    stress_mapping = None
    if hparams.use_stress_embedding:
      stress_mapping = get_stress_mapping(checkpoint)
    self.stress_mapping = stress_mapping

    tone_mapping = None
    if hparams.use_tone_embedding:
      tone_mapping = get_tone_mapping(checkpoint)
    self.tone_mapping = tone_mapping

    duration_mapping = None
    if hparams.use_duration_embedding:
      duration_mapping = get_duration_mapping(checkpoint)
    self.duration_mapping = duration_mapping

    speaker_mapping = None
    if hparams.use_speaker_embedding:
      speaker_mapping = get_speaker_mapping(checkpoint)
    self.speaker_mapping = speaker_mapping

    model = load_model(
        hparams=hparams,
        checkpoint=checkpoint,
        n_symbols=get_mappings_count(symbol_mapping),
        n_stresses=try_get_mappings_count(stress_mapping),
        n_tones=try_get_mappings_count(tone_mapping),
        n_durations=try_get_mappings_count(duration_mapping),
        n_speakers=try_get_mappings_count(speaker_mapping),
    )

    model = cast(Tacotron2, try_copy_to(model, device))
    model = model.eval()
    self.model = model

  def get_sampling_rate(self) -> int:
    return self.hparams.sampling_rate

  def infer(self, symbols: Symbols, speaker: Speaker, max_decoder_steps: int = 3000, seed: int = 0, include_stats: bool = False) -> InferenceResult:
    logger = logging.getLogger(__name__)

    core_symbols, stresses, tones, durations = get_map_keys(symbols, self.hparams)

    speaker_id = None
    if self.hparams.use_speaker_embedding:
      speaker_id = self.speaker_mapping.get(speaker)

    unmappable = set()
    indices = set(range(len(symbols)))

    stress_ids = None
    unmappable_stresses = None
    if self.hparams.use_stress_embedding:
      assert stresses is not None
      stress_ids = list(get_mapped_indices(stresses, self.stress_mapping))
      unmappable_indices = set(find_indices(stress_ids, {None}))
      if len(unmappable_indices) > 0:
        unmappable_stresses = set(get_items_by_index(stresses, unmappable_indices))
        logger.warning(f"Unknown stress(es): {' '.join(sorted(unmappable_stresses))}")
        unmappable |= unmappable_indices

    tone_ids = None
    unmappable_tones = None
    if self.hparams.use_tone_embedding:
      assert tones is not None
      tone_ids = list(get_mapped_indices(tones, self.tone_mapping))
      unmappable_indices = set(find_indices(tone_ids, {None}))
      if len(unmappable_indices) > 0:
        unmappable_tones = set(get_items_by_index(tones, unmappable_indices))
        logger.warning(f"Unknown tone(s): {' '.join(sorted(unmappable_tones))}")
        unmappable |= unmappable_indices

    duration_ids = None
    unmappable_durations = None
    if self.hparams.use_duration_embedding:
      assert durations is not None
      duration_ids = list(get_mapped_indices(durations, self.duration_mapping))
      unmappable_indices = set(find_indices(duration_ids, {None}))
      if len(unmappable_indices) > 0:
        unmappable_durations = set(get_items_by_index(durations, unmappable_indices))
        logger.warning(f"Unknown duration(s): {' '.join(sorted(unmappable_durations))}")
        unmappable |= unmappable_indices

    symbol_ids = list(get_mapped_indices(core_symbols, self.symbol_mapping))
    unmappable_indices = set(find_indices(symbol_ids, {None}))
    unmappable_symbols = None
    if len(unmappable_indices) > 0:
      unmappable_symbols = set(get_items_by_index(core_symbols, unmappable_indices))
      logger.warning(f"Unknown symbol(s): {' '.join(sorted(unmappable_symbols))}")
      unmappable |= unmappable_indices

    mappable = indices - unmappable

    # print_text_parts = []
    # for i, orig_symbol in enumerate(symbols):
    #   is_mappable = i in mapable
    #   tmp = orig_symbol
    #   parts = [core_symbols[i]]
    #   if self.hparams.use_stress_embedding:
    #     parts.append(stresses[i])
    #   if self.hparams.use_tone_embedding:
    #     parts.append(tones[i])
    #   if self.hparams.use_duration_embedding:
    #     parts.append(durations[i])
    #   tmp += f"({';'.join(parts)})"
    #   if not is_mappable:
    #     tmp = f"[{tmp}]"
    #   print_text_parts.append(tmp)
    # logger.info(' '.join(print_text_parts))

    print_text_parts = []
    for i, orig_symbol in enumerate(symbols):
      is_mappable = i in mappable
      tmp = orig_symbol
      if not is_mappable:
        tmp = f"[{tmp}]"
      print_text_parts.append(tmp)
    logger.debug('|'.join(print_text_parts))

    init_global_seeds(seed)

    symbol_tensor = LongTensor([list(get_items_by_index(symbol_ids, mappable))])
    symbol_tensor = try_copy_to(symbol_tensor, self.device)

    stress_tensor = None
    if self.hparams.use_stress_embedding:
      stress_tensor = LongTensor([list(get_items_by_index(stress_ids, mappable))])
      stress_tensor = try_copy_to(stress_tensor, self.device)

    tone_tensor = None
    if self.hparams.use_tone_embedding:
      tone_tensor = LongTensor([list(get_items_by_index(tone_ids, mappable))])
      tone_tensor = try_copy_to(tone_tensor, self.device)

    duration_tensor = None
    if self.hparams.use_duration_embedding:
      duration_tensor = LongTensor([list(get_items_by_index(duration_ids, mappable))])
      duration_tensor = try_copy_to(duration_tensor, self.device)

    speaker_tensor = None
    if self.hparams.use_speaker_embedding:
      speaker_tensor = LongTensor(
          symbol_tensor.size(0), symbol_tensor.size(1))
      torch.nn.init.constant_(speaker_tensor, speaker_id)
      speaker_tensor = try_copy_to(speaker_tensor, self.device)

    start = time.perf_counter()

    with torch.no_grad():
      mel_outputs, mel_outputs_postnet, gate_outputs, alignments, reached_max_decoder_steps = self.model.inference(
          symbols=symbol_tensor,
          stresses=stress_tensor,
          tones=tone_tensor,
          durations=duration_tensor,
          speakers=speaker_tensor,
          max_decoder_steps=max_decoder_steps,
      )

    end = time.perf_counter()
    inference_duration_s = end - start

    mel_outputs_postnet_np = mel_to_numpy(mel_outputs_postnet)
    duration_s = get_duration(S=mel_outputs_postnet_np,
                              n_fft=self.hparams.filter_length, hop_length=self.hparams.hop_length)
    infer_res = InferenceResult(
      sampling_rate=self.hparams.sampling_rate,
      reached_max_decoder_steps=reached_max_decoder_steps,
      inference_duration_s=inference_duration_s,
      mel_outputs_postnet=mel_outputs_postnet_np,
      mel_outputs=None,
      gate_outputs=None,
      alignments=None,
      unmappable_symbols=unmappable_symbols,
      unmappable_tones=unmappable_tones,
      unmappable_durations=unmappable_durations,
      unmappable_stresses=unmappable_stresses,
      duration_s=duration_s
    )

    if include_stats:
      infer_res.mel_outputs = mel_to_numpy(mel_outputs)
      infer_res.gate_outputs = mel_to_numpy(gate_outputs)
      infer_res.alignments = mel_to_numpy(alignments)

    return infer_res
