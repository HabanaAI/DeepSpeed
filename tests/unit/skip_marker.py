# Copyright (c) 2023 Habana Labs, Ltd. an Intel Company
# Copyright (c) Microsoft Corporation.
# SPDX-License-Identifier: Apache-2.0

# DeepSpeed Team

hpu_lazy_skip_tests = {}

g1_lazy_skip_tests = {
    "unit/runtime/half_precision/test_bf16.py::TestZeroSupportedClientOptimizer::test[FusedAdam]":
    "Skipping test due to segfault. SW-170285",
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[8-fp32]":
    "FusedAdam test not supported. Test got stuck.",
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[16-fp32]":
    "FusedAdam test not supported. Test got stuck.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1024-fp32]":
    "FusedAdam test not supported. Test got stuck.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[64-fp32]":
    "FusedAdam test not supported. Test got stuck.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1048576-fp32]":
    "FusedAdam test not supported. Test got stuck.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[22-fp32]":
    "FusedAdam test not supported. Test got stuck.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[128-fp32]":
    "FusedAdam test not supported. Test got stuck.",
    "unit/runtime/pipe/test_pipe.py::TestPipeCifar10::test_pipe_use_reentrant[topo_config2]":
    "Stuck on eager mode",
    "unit/runtime/pipe/test_pipe.py::TestPipeCifar10::test_pipe_use_reentrant[topo_config1]":
    "Stuck on eager mode",
    "unit/inference/test_human_eval.py::test_human_eval[codellama/CodeLlama-7b-Python-hf]":
    "HPU is not supported on deepspeed-mii",
}

g2_lazy_skip_tests = {
    "unit/runtime/half_precision/test_bf16.py::TestZeroSupportedClientOptimizer::test[FusedAdam]":
    "Skipping test due to segfault. SW-175725.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1048576-fp16]":
    "Skipping test due to segfault then stuck. SW-175725.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1024-fp16]":
    "Skipping test due to segfault then stuck. SW-175725.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[128-fp16]":
    "Skipping test due to segfault then stuck. SW-175725.",
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[16-fp16]":
    "FusedAdam test not supported. Test got stuck. SW-175725.",
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[8-fp32]":
    "FusedAdam test not supported. Test got stuck. SW-175725.",
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[16-fp32]":
    "FusedAdam test not supported. Test got stuck. SW-175725.",
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[8-fp16]":
    "FusedAdam test not supported. Test got stuck. SW-175725.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1024-fp32]":
    "FusedAdam test not supported. Test got stuck. SW-175725.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[64-fp32]":
    "FusedAdam test not supported. Test got stuck. SW-175725.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1048576-fp32]":
    "FusedAdam test not supported. Test got stuck. SW-175725.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[64-fp16]":
    "FusedAdam test not supported. Test got stuck. SW-175725.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[22-fp16]":
    "FusedAdam test not supported. Test got stuck. SW-175725.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[22-fp32]":
    "FusedAdam test not supported. Test got stuck. SW-175725.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[128-fp32]":
    "FusedAdam test not supported. Test got stuck. SW-175725.",
    "unit/runtime/half_precision/test_fp16.py::TestZeroSupportedClientOptimizer::test[FusedAdam-3]":
    "synapse detected critical error. SW-176889",
    "unit/runtime/half_precision/test_fp16.py::TestZeroSupportedClientOptimizer::test[FusedAdam-2]":
    "synapse detected critical error. SW-176889",
    "unit/runtime/half_precision/test_fp16.py::TestZeroSupportedClientOptimizer::test[FusedAdam-1]":
    "synapse detected critical error. SW-176889",
    "unit/runtime/half_precision/test_fp16.py::TestFP16OptimizerForMoE::test_fused_gradnorm":
    "FusedAdam test not supported. Test got stuck. SW-175725.",
    "unit/inference/test_human_eval.py::test_human_eval[codellama/CodeLlama-7b-Python-hf]":
    "HPU is not supported on deepspeed-mii",
}

hpu_eager_skip_tests = {}

g1_eager_skip_tests = {
    "unit/inference/test_human_eval.py::test_human_eval[codellama/CodeLlama-7b-Python-hf]":
    "HPU is not supported on deepspeed-mii",
}

g2_eager_skip_tests = {
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[False-False-2-2]":
    "Skip, due to SW-182681",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[False-True-1-2]":
    "Skip, due to SW-182681",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[True-True-1-2]":
    "Skip, due to SW-182681",
    "unit/inference/test_human_eval.py::test_human_eval[codellama/CodeLlama-7b-Python-hf]":
    "HPU is not supported on deepspeed-mii",
}

gpu_skip_tests = {
    "unit/runtime/zero/test_zero.py::TestZeroOffloadOptim::test[True]":
    "Disabled as it is causing test to stuck. SW-163517.",
}
