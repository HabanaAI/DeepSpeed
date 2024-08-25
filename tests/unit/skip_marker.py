# Copyright (c) 2023 Habana Labs, Ltd. an Intel Company
# Copyright (c) Microsoft Corporation.
# SPDX-License-Identifier: Apache-2.0

# DeepSpeed Team

hpu_lazy_skip_tests = {}

g1_lazy_skip_tests = {
    "unit/inference/test_human_eval.py::test_human_eval[codellama/CodeLlama-7b-Python-hf]":
    "HPU is not supported on deepspeed-mii",
}

g2_lazy_skip_tests = {
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[4-9-1024]":
    "Stuck, SW-190067.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test_eval[4-9-1024]":
    "stuck, SW-190067.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test_gradient_accumulation[4-9-1024]":
    "Stuck, SW-190067.",
    "unit/inference/test_human_eval.py::test_human_eval[codellama/CodeLlama-7b-Python-hf]":
    "HPU is not supported on deepspeed-mii",
}

g3_lazy_skip_tests = {
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-openai-community/gpt2-xl]":
    "Skip hang download",
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-EleutherAI/gpt-neo-2.7B]":
    "Skip hang download"
}
hpu_eager_skip_tests = {}

g1_eager_skip_tests = {
    "unit/inference/test_inference.py::TestMPSize::test[fp32-gpt-neo]":
    "Flaky Segfault. Stuck",
    "unit/inference/test_human_eval.py::test_human_eval[codellama/CodeLlama-7b-Python-hf]":
    "HPU is not supported on deepspeed-mii",
}

g2_eager_skip_tests = {
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[4-9-1024]":
    "Stuck, SW-190067.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test_eval[4-9-1024]":
    "stuck, SW-190067.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test_gradient_accumulation[4-9-1024]":
    "Stuck, SW-190067.",
    "unit/inference/test_human_eval.py::test_human_eval[codellama/CodeLlama-7b-Python-hf]":
    "HPU is not supported on deepspeed-mii",
}
g3_eager_skip_tests = {
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-openai-community/gpt2-xl]":
    "Skip hang download",
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-EleutherAI/gpt-neo-2.7B]":
    "Skip hang download",
    "unit/inference/test_inference.py::TestMPSize::test[fp16-gpt-neo]": "Skip synapse Device restart",
    "unit/inference/test_inference.py::TestMPSize::test[fp32-gpt-neo]": "Skip Seg fault Internal Error",
}

gpu_skip_tests = {
    "unit/runtime/zero/test_zero.py::TestZeroOffloadOptim::test[True]":
    "Disabled as it is causing test to stuck. SW-163517.",
    "unit/inference/test_stable_diffusion.py::TestStableDiffusion::test":
    "Xfail not supported",
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-openai-community/gpt2-xl]":
    "skip: timeout triggered",
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-EleutherAI/gpt-neo-2.7B]":
    "skip: timeout triggered",
}
