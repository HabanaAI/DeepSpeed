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
    "Skip workload takes longer time to run",
    "unit/linear/test_ctx.py::TestEngine::test_model": "Skip on G1 due to SW-209651",
    "unit/linear/test_linear.py::TestOptimizedLinear::test[qbit6-bws2]": "Skip on G1 due to SW-209651",
    "unit/linear/test_linear.py::TestOptimizedLinear::test[qbit8-bws2]": "Skip on G1 due to SW-209651",
    "unit/linear/test_linear.py::TestLoRALinear::test[2]": "Skip on G1 due to SW-209651",
    "unit/linear/test_ctx.py::TestInitTransformers::test_pretrained_init": "Skip on G1 due to SW-209651",
    "unit/linear/test_linear.py::TestBasicLinear::test": "Skip on G1 due to SW-209651",
    "unit/linear/test_linear.py::TestOptimizedLinear::test[qbit8-bws1]": "Skip on G1 due to SW-209651",
    "unit/linear/test_ctx.py::TestInitTransformers::test_config_init": "Skip on G1 due to SW-209651",
    "unit/linear/test_linear.py::TestLoRALinear::test[1]": "Skip on G1 due to SW-209651",
    "unit/linear/test_linear.py::TestQuantLinear::test[8]": "Skip on G1 due to SW-209651",
    "unit/linear/test_quant_param.py::TestQuantParam::test_move_to_accelerator": "Skip on G1 due to SW-209651",
    "unit/linear/test_linear.py::TestQuantLinear::test[6]": "Skip on G1 due to SW-209651",
    "unit/linear/test_quant_param.py::TestQuantParam::test_unsupported_dtypes[dtype0]": "Skip on G1 due to SW-209651",
    "unit/linear/test_linear.py::TestOptimizedLinear::test[qbit6-bws1]": "Skip on G1 due to SW-209651",
    "unit/linear/test_quant_param.py::TestQuantParam::test_requires_grad": "Skip on G1 due to SW-209651",
    "unit/linear/test_quant_param.py::TestQuantParam::test_unsupported_dtypes[dtype1]": "Skip on G1 due to SW-209651",
    "unit/linear/test_quant_param.py::TestQuantParam::test_hf_clone": "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp8_gemm.py::test_fp_quant[2048-qbits8-bf16]": "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp8_gemm.py::test_fp_quant[64-qbits8-bf16]": "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp8_gemm.py::test_fp_quant[2-qbits8-bf16]": "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp8_gemm.py::test_fp_quant[256-qbits8-bf16]": "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp8_gemm.py::test_fp_quant[1-qbits8-bf16]": "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp8_gemm.py::test_fp_quant[128-qbits8-bf16]": "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp8_gemm.py::test_fp_quant[1024-qbits8-bf16]": "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp8_gemm.py::test_fp_quant[8-qbits8-bf16]": "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp8_gemm.py::test_fp_quant[32-qbits8-bf16]": "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp8_gemm.py::test_fp_quant[4-qbits8-bf16]": "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp8_gemm.py::test_fp_quant[512-qbits8-bf16]": "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp_quant.py::test_fp_quant_selective[bf16]": "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp_quant.py::test_fp_quant[qbits12-bf16]": "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp_quant.py::test_fp_quant_meta[bf16]": "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp_quant.py::test_fp_quant[qbits6-bf16]": "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp_quant.py::test_fp_quant[qbits8-bf16]": "Skip on G1 due to SW-209651",
}

g2_lazy_skip_tests = {
    "unit/inference/test_human_eval.py::test_human_eval[codellama/CodeLlama-7b-Python-hf]":
    "HPU is not supported on deepspeed-mii",
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-openai-community/gpt2-xl-False]":
    "Skip workload takes longer time to run",
    "unit/ops/fp_quantizer/test_fp_quant.py::test_fp_quant[qbits12-bf16]": "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp_quant.py::test_fp_quant[qbits6-bf16]": "Skip on G1 due to SW-209651",
    "unit/linear/test_linear.py::TestOptimizedLinear::test[qbit6-bws2]": "Skip on G1 due to SW-209651",
    "unit/linear/test_linear.py::TestOptimizedLinear::test[qbit6-bws1]": "Skip on G1 due to SW-209651",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[2-False-False]":
    "skip due to no support in Lazy mode for moe SW-220259",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[2-True-False]":
    "skip due to no support in Lazy mode for moe SW-220259",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[4-True-False]":
    "skip due to no support in Lazy mode for moe SW-220259",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[4-False-False]":
    "skip due to no support in Lazy mode for moe SW-220259",
    "unit/moe/test_moe.py::TestExpertWeightGradWithZero::test[0]":
    "skip due to no support in Lazy mode for moe SW-220259",
    "unit/moe/test_moe.py::TestSimpleMoE::test[2]": "skip due to no support in Lazy mode for moe SW-220259",
    "unit/moe/test_moe.py::TestSimpleMoE::test[1]": "skip due to no support in Lazy mode for moe SW-220259",
    "unit/moe/test_moe.py::TestExpertWeightGradWithZero::test[1]":
    "skip due to no support in Lazy mode for moe SW-220259",
    "unit/moe/test_moe.py::TestExpertWeightGradWithZero::test[2]":
    "skip due to no support in Lazy mode for moe SW-220259",
    "unit/moe/test_moe.py::TestMoE::test[False-2-4]": "skip due to no support in Lazy mode for moe SW-220259",
    "unit/moe/test_moe.py::TestMoE::test[False-2-2]": "skip due to no support in Lazy mode for moe SW-220259",
    "unit/moe/test_moe.py::TestMoE::test[False-1-2]": "skip due to no support in Lazy mode for moe SW-220259",
    "unit/moe/test_moe.py::TestMoE::test[False-1-4]": "skip due to no support in Lazy mode for moe SW-220259",
    "unit/moe/test_moe.py::TestMoE::test[True-2-2]": "skip due to no support in Lazy mode for moe SW-220259",
    "unit/moe/test_moe.py::TestMoE::test[True-2-4]": "skip due to no support in Lazy mode for moe SW-220259",
    "unit/moe/test_moe.py::TestMoE::test[True-1-4]": "skip due to no support in Lazy mode for moe SW-220259",
    "unit/moe/test_moe.py::TestMoE::test[True-1-2]": "skip due to no support in Lazy mode for moe SW-220259",
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
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test_odd_world_size[bf16-marian-False-False]":
    "Struck observed",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test[bf16-marian-False-False]":
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
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test[fp16-marian-True-True]":
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
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test_odd_world_size[bf16-marian-True-True]":
    "test Hang",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[facebook/opt-350m-True]":
    "test Hang",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[False-True-False-1-dtype0]":
    "test Hang",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShard::test[EleutherAI/gpt-j-6B-fp16-True]":
    "Skip due to SW-193097",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test[bf16-marian-True-True]":
    "Skip due to flaky hang",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[EleutherAI/gpt-j-6B-True]":
    "test Hang",
    "unit/linear/test_ctx.py::TestEngine::test_model":
    "Skip on G1 due to SW-209651",
    "unit/linear/test_linear.py::TestOptimizedLinear::test[qbit6-bws2]":
    "Skip on G1 due to SW-209651",
    "unit/linear/test_linear.py::TestOptimizedLinear::test[qbit8-bws2]":
    "Skip on G1 due to SW-209651",
    "unit/linear/test_linear.py::TestLoRALinear::test[2]":
    "Skip on G1 due to SW-209651",
    "unit/linear/test_ctx.py::TestInitTransformers::test_pretrained_init":
    "Skip on G1 due to SW-209651",
    "unit/linear/test_linear.py::TestBasicLinear::test":
    "Skip on G1 due to SW-209651",
    "unit/linear/test_linear.py::TestOptimizedLinear::test[qbit8-bws1]":
    "Skip on G1 due to SW-209651",
    "unit/linear/test_ctx.py::TestInitTransformers::test_config_init":
    "Skip on G1 due to SW-209651",
    "unit/linear/test_linear.py::TestLoRALinear::test[1]":
    "Skip on G1 due to SW-209651",
    "unit/linear/test_linear.py::TestQuantLinear::test[8]":
    "Skip on G1 due to SW-209651",
    "unit/linear/test_quant_param.py::TestQuantParam::test_move_to_accelerator":
    "Skip on G1 due to SW-209651",
    "unit/linear/test_linear.py::TestQuantLinear::test[6]":
    "Skip on G1 due to SW-209651",
    "unit/linear/test_quant_param.py::TestQuantParam::test_unsupported_dtypes[dtype0]":
    "Skip on G1 due to SW-209651",
    "unit/linear/test_linear.py::TestOptimizedLinear::test[qbit6-bws1]":
    "Skip on G1 due to SW-209651",
    "unit/linear/test_quant_param.py::TestQuantParam::test_requires_grad":
    "Skip on G1 due to SW-209651",
    "unit/linear/test_quant_param.py::TestQuantParam::test_unsupported_dtypes[dtype1]":
    "Skip on G1 due to SW-209651",
    "unit/linear/test_quant_param.py::TestQuantParam::test_hf_clone":
    "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp8_gemm.py::test_fp_quant[2048-qbits8-bf16]":
    "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp8_gemm.py::test_fp_quant[64-qbits8-bf16]":
    "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp8_gemm.py::test_fp_quant[2-qbits8-bf16]":
    "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp8_gemm.py::test_fp_quant[256-qbits8-bf16]":
    "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp8_gemm.py::test_fp_quant[1-qbits8-bf16]":
    "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp8_gemm.py::test_fp_quant[128-qbits8-bf16]":
    "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp8_gemm.py::test_fp_quant[1024-qbits8-bf16]":
    "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp8_gemm.py::test_fp_quant[8-qbits8-bf16]":
    "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp8_gemm.py::test_fp_quant[32-qbits8-bf16]":
    "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp8_gemm.py::test_fp_quant[4-qbits8-bf16]":
    "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp8_gemm.py::test_fp_quant[512-qbits8-bf16]":
    "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp_quant.py::test_fp_quant_selective[bf16]":
    "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp_quant.py::test_fp_quant[qbits12-bf16]":
    "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp_quant.py::test_fp_quant_meta[bf16]":
    "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp_quant.py::test_fp_quant[qbits6-bf16]":
    "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp_quant.py::test_fp_quant[qbits8-bf16]":
    "Skip on G1 due to SW-209651",
}

g2_eager_skip_tests = {
    "unit/inference/test_human_eval.py::test_human_eval[codellama/CodeLlama-7b-Python-hf]":
    "HPU is not supported on deepspeed-mii",
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-openai-community/gpt2-xl-True]":
    "Skip workload takes longer time to run",
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-EleutherAI/gpt-neo-2.7B-True]":
    "Skip workload takes longer time to run",
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
    "unit/inference/test_inference.py::TestMPSize::test[fp16-gpt-neo-True]":
    "GC failed so skip to check",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[bigscience/bloom-560m-fp16-True]":
    "test Hang",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShard::test[EleutherAI/gpt-j-6B-fp16-True]":
    "Skip due to SW-193097",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[EleutherAI/gpt-j-6B-True]":
    "test Hang",
    "unit/ops/fp_quantizer/test_fp_quant.py::test_fp_quant[qbits12-bf16]":
    "Skip on G1 due to SW-209651",
    "unit/ops/fp_quantizer/test_fp_quant.py::test_fp_quant[qbits6-bf16]":
    "Skip on G1 due to SW-209651",
    "unit/linear/test_linear.py::TestOptimizedLinear::test[qbit6-bws2]":
    "Skip on G1 due to SW-209651",
    "unit/linear/test_linear.py::TestOptimizedLinear::test[qbit6-bws1]":
    "Skip on G1 due to SW-209651",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test[fp16-marian-True-True]":
    "Skip struck and fp16 not supported",
    "unit/runtime/pipe/test_pipe.py::TestPipeCifar10::test_pipe_use_reentrant[topo_config2]":
    "Test Hang",
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
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_bf16_fragments[False]":
    "Skip due to hang",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[none-3-full-dtype0]":
    "skip due to hang",
}
