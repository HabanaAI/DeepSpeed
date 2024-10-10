# Copyright (c) 2023 Habana Labs, Ltd. an Intel Company
# Copyright (c) Microsoft Corporation.
# SPDX-License-Identifier: Apache-2.0

# DeepSpeed Team

hpu_lazy_skip_tests = {}

g1_lazy_skip_tests = {
    "unit/inference/test_human_eval.py::test_human_eval[codellama/CodeLlama-7b-Python-hf]":
    "HPU is not supported on deepspeed-mii",
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-openai-community/gpt2-xl-False]":
    "Skip workload takes longer time to run",
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-EleutherAI/gpt-neo-2.7B-False]":
    "Skip workload takes longer time to run"
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
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-openai-community/gpt2-xl-False]":
    "Skip workload takes longer time to run",
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-EleutherAI/gpt-neo-2.7B-False]":
    "Skip workload takes longer time to run"
}

g3_lazy_skip_tests = {
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-openai-community/gpt2-xl-False]":
    "Skip workload takes longer time to run",
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-EleutherAI/gpt-neo-2.7B-False]":
    "Skip workload takes longer time to run",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[4-9-1024]": "test hang patch:430071",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test_gradient_accumulation[4-9-1024]":
    "test hang patch:430071",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test_eval[4-9-1024]": "test hang patch:430071",
}
hpu_eager_skip_tests = {}

g1_eager_skip_tests = {
    "unit/inference/test_inference.py::TestMPSize::test[fp32-gpt-neo-True]":
    "Flaky Segfault. Stuck",
    "unit/inference/test_inference.py::TestMPSize::test[fp32-gpt-neo-False]":
    "Flaky Segfault. Stuck",
    "unit/inference/test_human_eval.py::test_human_eval[codellama/CodeLlama-7b-Python-hf]":
    "HPU is not supported on deepspeed-mii",
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-openai-community/gpt2-xl-False]":
    "Skip workload takes longer time to run",
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-EleutherAI/gpt-neo-2.7B-False]":
    "Skip workload takes longer time to run",
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-openai-community/gpt2-xl-True]":
    "Skip workload takes longer time to run",
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-EleutherAI/gpt-neo-2.7B-True]":
    "Skip workload takes longer time to run",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test_odd_world_size[bf16-marian-False]":
    "Struck observed",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test[bf16-marian-False]":
    "Flaky struck observed",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-125m-text-generation-fp16-noCG-noTriton-True-True]":
    "Skip due to SW-193097",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-125m-text-generation-fp32-noCG-noTriton-True-True]":
    "Skip due to SW-193097",
    "unit/inference/test_inference.py::TestModelTask::test[Norod78/hebrew-bad_wiki-gpt_neo-tiny-text-generation-fp32-noCG-noTriton-True-True]":
    "Skip due to SW-193097",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert/distilgpt2-text-generation-fp32-noCG-noTriton-True-True]":
    "Skip due to SW-193097",
    "unit/inference/test_inference.py::TestModelTask::test[Norod78/hebrew-bad_wiki-gpt_neo-tiny-text-generation-fp16-noCG-noTriton-True-True]":
    "Skip due to SW-193097",
    "unit/inference/test_inference.py::TestModelTask::test[openai-community/gpt2-text-generation-fp32-noCG-noTriton-True-True]":
    "Skip due to SW-193097",
    "unit/inference/test_inference.py::TestLowCpuMemUsage::test[gpt2-True]":
    "Skip struck for longer duration",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test[fp16-marian-True]":
    "Skip struck and fp16 not supported",
    "unit/inference/test_inference.py::TestModelTask::test[openai-community/gpt2-text-generation-fp16-noCG-noTriton-True-True]":
    "Skip due to SW-193097",
    "unit/runtime/pipe/test_pipe.py::TestPipeCifar10::test_pipe_use_reentrant[topo_config1]":
    "Test Hang",
    "unit/runtime/pipe/test_pipe.py::TestPipeCifar10::test_pipe_use_reentrant[topo_config2]":
    "Test Hang",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-noCG-noTriton-True-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-noCG-noTriton-False-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-noCG-Triton-True-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp32-noCG-noTriton-True-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp32-noCG-Triton-False-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-CG-noTriton-True-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp32-CG-Triton-False-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-CG-Triton-True-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-noCG-Triton-False-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp32-CG-noTriton-False-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp32-CG-Triton-True-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp32-CG-noTriton-True-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp32-noCG-Triton-True-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp32-noCG-noTriton-False-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-CG-Triton-False-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-CG-noTriton-False-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-noCG-noTriton-False-True]":
    "Test Hang",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-noCG-noTriton-True-True]":
    "Test Hang",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp32-CG-Triton-True-True]":
    "Test Hang",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test_odd_world_size[bf16-marian-True]":
    "test Hang",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[facebook/opt-350m-True]":
    "test Hang",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[False-True-False-1-dtype0]":
    "test Hang",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShard::test[EleutherAI/gpt-j-6B-fp16-True]":
    "Skip due to SW-193097",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test[bf16-marian-True]":
    "Skip due to flaky hang",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[EleutherAI/gpt-j-6B-True]":
    "test Hang",
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
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-openai-community/gpt2-xl-False]":
    "Skip workload takes longer time to run",
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-EleutherAI/gpt-neo-2.7B-False]":
    "Skip workload takes longer time to run",
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-openai-community/gpt2-xl-True]":
    "Skip workload takes longer time to run",
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-EleutherAI/gpt-neo-2.7B-True]":
    "Skip workload takes longer time to run",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert/distilgpt2-text-generation-fp16-noCG-noTriton-True-True]":
    "Skip struck for longer duration",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-125m-text-generation-fp16-noCG-noTriton-True-True]":
    "Skip due to SW-193097",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-125m-text-generation-fp32-noCG-noTriton-True-True]":
    "Skip due to SW-193097",
    "unit/inference/test_inference.py::TestModelTask::test[Norod78/hebrew-bad_wiki-gpt_neo-tiny-text-generation-fp16-noCG-noTriton-True-True]":
    "Skip due to SW-193097",
    "unit/inference/test_inference.py::TestModelTask::test[Norod78/hebrew-bad_wiki-gpt_neo-tiny-text-generation-fp32-noCG-noTriton-True-True]":
    "Skip due to SW-193097",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert/distilgpt2-text-generation-fp32-noCG-noTriton-True-True]":
    "Skip due to SW-193097",
    "unit/inference/test_inference.py::TestModelTask::test[openai-community/gpt2-text-generation-fp32-noCG-noTriton-True-True]":
    "Skip due to SW-193097",
    "unit/inference/test_inference.py::TestModelTask::test[openai-community/gpt2-text-generation-fp16-noCG-noTriton-True-True]":
    "Skip due to SW-193097",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-noCG-noTriton-False-True]":
    "Test Hang",
    "unit/inference/test_inference.py::TestLowCpuMemUsage::test[gpt2-True]":
    "Skip struck for longer duration",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-noCG-noTriton-True-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-noCG-noTriton-False-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-noCG-Triton-True-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp32-noCG-noTriton-True-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp32-noCG-Triton-False-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-CG-noTriton-True-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp32-CG-Triton-False-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-CG-Triton-True-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-noCG-Triton-False-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp32-CG-noTriton-False-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp32-CG-Triton-True-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp32-CG-noTriton-True-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp32-noCG-Triton-True-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp32-noCG-noTriton-False-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-CG-Triton-False-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-CG-noTriton-False-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestMPSize::test[fp32-gpt-neo-True]":
    "Flaky Segfault. Stuck",
    "unit/inference/test_inference.py::TestMPSize::test[fp16-gpt-neo-True]":
    "GC failed so skip to check",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-noCG-noTriton-True-True]":
    "Test Hang",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp32-CG-Triton-True-True]":
    "Test Hang",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[False-False-True-1-dtype1]":
    "test Hang",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[bigscience/bloom-560m-fp16-True]":
    "test Hang",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShard::test[EleutherAI/gpt-j-6B-fp16-True]":
    "Skip due to SW-193097",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[EleutherAI/gpt-j-6B-True]":
    "test Hang",
}
g3_eager_skip_tests = {
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-openai-community/gpt2-xl-False]":
    "Skip workload takes longer time to run",
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-EleutherAI/gpt-neo-2.7B-False]":
    "Skip workload takes longer time to run",
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-openai-community/gpt2-xl-True]":
    "Skip workload takes longer time to run",
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-EleutherAI/gpt-neo-2.7B-True]":
    "Skip workload takes longer time to run",
    "unit/inference/test_inference.py::TestLowCpuMemUsage::test[gpt2-True]":
    "Skip struck for longer duration",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert/distilgpt2-text-generation-fp16-noCG-noTriton-True-True]":
    "Skip struck for longer duration",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[4-9-1024]":
    "test hang patch:430071",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test_gradient_accumulation[4-9-1024]":
    "test hang patch:430071",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test_eval[4-9-1024]":
    "test hang patch:430071",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShard::test[EleutherAI/gpt-j-6B-fp16-True]":
    "Skip due to SW-193097",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShard::test[bigscience/bloom-560m-fp16-True]":
    "Skip due to SW-193097",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-125m-text-generation-fp16-noCG-noTriton-True-True]":
    "Skip due to SW-193097",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-125m-text-generation-fp32-noCG-noTriton-True-True]":
    "Skip due to SW-193097",
    "unit/inference/test_inference.py::TestModelTask::test[Norod78/hebrew-bad_wiki-gpt_neo-tiny-text-generation-fp16-noCG-noTriton-True-True]":
    "Skip due to SW-193097",
    "unit/inference/test_inference.py::TestModelTask::test[openai-community/gpt2-text-generation-fp32-noCG-noTriton-True-True]":
    "Skip due to SW-193097",
    "unit/inference/test_inference.py::TestModelTask::test[Norod78/hebrew-bad_wiki-gpt_neo-tiny-text-generation-fp32-noCG-noTriton-True-True]":
    "Skip due to SW-193097",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert/distilgpt2-text-generation-fp32-noCG-noTriton-True-True]":
    "Skip due to SW-193097",
    "unit/inference/test_inference.py::TestModelTask::test[openai-community/gpt2-text-generation-fp16-noCG-noTriton-True-True]":
    "Skip due to SW-193097",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-noCG-noTriton-True-True]":
    "GC failed so skip to check",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-noCG-noTriton-False-True]":
    "GC failed so skip to check",
    "unit/inference/test_inference.py::TestMPSize::test[fp16-gpt-neo-True]":
    "GC failed so skip to check",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-noCG-noTriton-True-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-noCG-noTriton-False-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-noCG-Triton-True-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp32-noCG-noTriton-True-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp32-noCG-Triton-False-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-CG-noTriton-True-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp32-CG-Triton-False-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-CG-Triton-True-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-noCG-Triton-False-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp32-CG-noTriton-False-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp32-CG-Triton-True-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp32-CG-noTriton-True-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp32-noCG-Triton-True-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp32-noCG-noTriton-False-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-CG-Triton-False-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-CG-noTriton-False-False]":
    "Skip bloom due to process struck and also fail",
    "unit/inference/test_inference.py::TestMPSize::test[fp32-gpt-neo-True]":
    "Flaky Segfault. Stuck",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp32-CG-Triton-True-True]":
    "Test Hang",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[facebook/opt-350m-True]":
    "test Hang",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[EleutherAI/gpt-j-6B-True]":
    "test Hang",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[bigscience/bloom-560m-True]":
    "test Hang",
}

gpu_skip_tests = {
    "unit/runtime/zero/test_zero.py::TestZeroOffloadOptim::test[True]":
    "Disabled as it is causing test to stuck. SW-163517.",
    "unit/inference/test_stable_diffusion.py::TestStableDiffusion::test":
    "Xfail not supported",
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-openai-community/gpt2-xl-False]":
    "skip: timeout triggered",
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-EleutherAI/gpt-neo-2.7B-False]":
    "skip: timeout triggered",
}
