# Copyright (c) Microsoft Corporation.
# SPDX-License-Identifier: Apache-2.0

# DeepSpeed Team

import torch
import contextlib
from deepspeed.utils.torch import required_torch_version
from deepspeed.accelerator import get_accelerator

try:
    from torch.compiler import is_compiling as torch_is_compiling
except ImportError:
    try:
        from torch._dynamo.external_utils import is_compiling as torch_is_compiling
    except ImportError:
        # Torch does not have compiler support
        torch_is_compiling = lambda: False

if required_torch_version(min_version="2.6.0a"):
    from torch._dynamo.compiled_autograd import _enable as compiled_autograd_enable
else:
    from torch._dynamo.compiled_autograd import enable as compiled_autograd_enable


def is_compile_supported():
    return hasattr(torch, "compiler") and hasattr(torch.nn.Module, "compile")


def disable(func):
    if is_compile_supported():
        return torch.compiler.disable(func)
    return func


def is_compiling():
    return torch_is_compiling()


@contextlib.contextmanager
def compiled_autograd(enabled, kwargs):
    try:
        if enabled:
            with compiled_autograd_enable(torch.compile(backend=get_accelerator().get_compile_backend(), **kwargs)):
                yield
        else:
            yield
    finally:
        pass
