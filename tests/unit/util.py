# Copyright (c) Microsoft Corporation.
# SPDX-License-Identifier: Apache-2.0

# DeepSpeed Team

import pytest
import torch
import deepspeed
import os
import multiprocessing
from deepspeed.accelerator import get_accelerator, is_current_accelerator_supported
from deepspeed.git_version_info import torch_info


def skip_on_arch(min_arch=7):
    if get_accelerator().device_name() == 'cuda':
        if torch.cuda.get_device_capability()[0] < min_arch:  #ignore-cuda
            pytest.skip(f"needs higher compute capability than {min_arch}")
    else:
        assert is_current_accelerator_supported()
        return


def skip_on_cuda(valid_cuda):
    split_version = lambda x: map(int, x.split('.')[:2])
    if get_accelerator().device_name() == 'cuda':
        CUDA_MAJOR, CUDA_MINOR = split_version(torch_info['cuda_version'])
        CUDA_VERSION = (CUDA_MAJOR * 10) + CUDA_MINOR
        if valid_cuda.count(CUDA_VERSION) == 0:
            pytest.skip(f"requires cuda versions {valid_cuda}")
    else:
        assert is_current_accelerator_supported()
        return


def bf16_required_version_check(accelerator_check=True):
    split_version = lambda x: map(int, x.split('.')[:2])
    TORCH_MAJOR, TORCH_MINOR = split_version(torch_info['version'])
    NCCL_MAJOR, NCCL_MINOR = split_version(torch_info['nccl_version'])
    CUDA_MAJOR, CUDA_MINOR = split_version(torch_info['cuda_version'])

    # Sometimes bf16 tests are runnable even if not natively supported by accelerator
    if accelerator_check:
        accelerator_pass = get_accelerator().is_bf16_supported()
    else:
        accelerator_pass = True

    torch_version_available = TORCH_MAJOR > 1 or (TORCH_MAJOR == 1 and TORCH_MINOR >= 10)
    cuda_version_available = CUDA_MAJOR >= 11
    nccl_version_available = NCCL_MAJOR > 2 or (NCCL_MAJOR == 2 and NCCL_MINOR >= 10)
    npu_available = get_accelerator().device_name() == 'npu'
    hpu_available = get_accelerator().device_name() == 'hpu'
    xpu_available = get_accelerator().device_name() == 'xpu'

    if torch_version_available and cuda_version_available and nccl_version_available and accelerator_pass:
        return True
    elif npu_available:
        return True
    elif hpu_available:
        return True
    elif xpu_available:
        return True
    else:
        return False


def required_amp_check():
    from importlib.util import find_spec
    if find_spec('apex') is None:
        return False
    else:
        return True


class no_child_process_in_deepspeed_io:

    def __enter__(self):
        # deepspeed_io defaults to creating a dataloader that uses a
        # multiprocessing pool. Our tests use pools and we cannot nest pools in
        # python. Therefore we're injecting this kwarg to ensure that no pools
        # are used in the dataloader.
        self.old_method = deepspeed.runtime.engine.DeepSpeedEngine.deepspeed_io

        def new_method(*args, **kwargs):
            kwargs["num_local_io_workers"] = 0
            return self.old_method(*args, **kwargs)

        deepspeed.runtime.engine.DeepSpeedEngine.deepspeed_io = new_method

    def __exit__(self, *_):
        deepspeed.runtime.engine.DeepSpeedEngine.deepspeed_io = self.old_method


def worker(proc_id, return_dict):
    #TODO SW-114787: move to new api outside experimental
    import habana_frameworks.torch.utils.experimental as htexp
    deviceType = htexp._get_device_type()
    if deviceType == htexp.synDeviceType.synDeviceGaudi2:
        return_dict['devicetype'] = "Gaudi2"
    elif deviceType == htexp.synDeviceType.synDeviceGaudi3:
        return_dict['devicetype'] = "Gaudi3"
    else:
        return_dict['devicetype'] = None
        assert False, f'Unexpected hpu device Type: {deviceType}'


def get_hpu_dev_version():
    hpu_dev = None
    if get_accelerator().device_name() != 'hpu':
        return hpu_dev
    if os.getenv("DEEPSPEED_UT_HL_DEVICE", default=None):
        hpu_dev = os.getenv("DEEPSPEED_UT_HL_DEVICE")
    if hpu_dev not in ["Gaudi", "Gaudi2", "Gaudi3"]:
        manager = multiprocessing.Manager()
        return_dict = manager.dict()
        proc_id = 0
        multiprocessing.set_start_method("spawn", force=True)
        p = multiprocessing.Process(target=worker, args=(proc_id, return_dict))
        p.start()
        p.join()
        try:
            dev_type = return_dict['devicetype']
        except:
            assert False, 'Unexpected hpu device Type: {}'.format(return_dict['devicetype'])
        p.terminate()
        exit_code = p.exitcode
        if exit_code:
            assert False, 'HPU dev type process exit with: {}'.format(exit_code)
        if dev_type in ["Gaudi", "Gaudi2", "Gaudi3"]:
            hpu_dev = dev_type
            os.environ['DEEPSPEED_UT_HL_DEVICE'] = dev_type
            return dev_type
        else:
            assert False, 'Unexpected hpu device Type: {}'.format(return_dict['devicetype'])
    else:
        return hpu_dev


def hpu_lazy_enabled():
    if get_accelerator().device_name() == 'hpu':
        import habana_frameworks.torch.hpu as thpu
        return thpu.is_lazy()
    return False
