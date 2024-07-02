# Copyright (c) Microsoft Corporation.
# SPDX-License-Identifier: Apache-2.0

# DeepSpeed Team

import torch
from deepspeed.utils import logger, log_dist
from deepspeed.runtime.checkpoint_engine.checkpoint_engine import \
    CheckpointEngine


class TorchCheckpointEngine(CheckpointEngine):

    def __init__(self, config_params=None):
        super().__init__(config_params)

    def create(self, tag):
        log_dist(f"[Torch] Checkpoint {tag} is about to be saved!", ranks=[0])

    def save(self, state_dict, path: str):
        logger.info(f"[Torch] Saving {path}...")
        # TODO SW-169821: remove WA: Once SW-169817 is solved to allow numpy() HPU un-detached tensors
        save(state_dict, path, pickle_protocol=4)
        logger.info(f"[Torch] Saved {path}.")
        return None

    def load(self, path: str, map_location=None):
        logger.info(f"[Torch] Loading checkpoint from {path}...")
        partition = torch.load(path, map_location=map_location)
        logger.info(f"[Torch] Loaded checkpoint from {path}.")
        return partition

    def commit(self, tag):
        logger.info(f"[Torch] Checkpoint {tag} is ready now!")
        return True


# TODO SW-169821: remove WA: Once SW-169817 is solved to allow numpy() HPU un-detached tensors
def save(data, filename, pickle_protocol=4):

    def convert_for_pickle(obj):
        if isinstance(obj, torch.Size):
            return obj
        elif isinstance(obj, dict):
            return {k: convert_for_pickle(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [convert_for_pickle(e) for e in obj]
        elif isinstance(obj, tuple):
            return tuple([convert_for_pickle(e) for e in obj])
        else:
            if isinstance(obj, torch.Tensor):
                return obj.data.detach().clone().cpu()
            else:
                return obj

    data = convert_for_pickle(data)
    torch.save(data, filename, pickle_protocol=pickle_protocol)
