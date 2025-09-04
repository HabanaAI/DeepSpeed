# Copyright (c) 2023 Habana Labs, Ltd. an Intel Company
# Copyright (c) Microsoft Corporation.
# SPDX-License-Identifier: Apache-2.0

# DeepSpeed Team

hpu_lazy_xfail_tests = {}

g1_lazy_xfail_tests = {
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-cased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-large-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-cased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-cased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-base-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-large-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-base-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-uncased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-cased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-cased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-uncased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-base-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-uncased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-uncased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-large-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-cased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-uncased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-large-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-cased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-base-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-cased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-cased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-uncased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[EleutherAI/pythia-70m-deduped-text-generation-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163095.",
    "unit/inference/test_inference.py::TestModelTask::test[EleutherAI/pythia-70m-deduped-text-generation-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163095.",
    "unit/inference/test_inference.py::TestModelTask::test[distilgpt2-text-generation-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_inference.py::TestModelTask::test[distilgpt2-text-generation-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert-base-cased-distilled-squad-question-answering-bf16-noCG-noTriton-True-False]":
    "Xfail, failed on vanilla as well.",
    "unit/inference/test_inference.py::TestModelTask::test[gpt2-text-generation-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert-base-cased-distilled-squad-question-answering-fp32-CG-noTriton-True-False]":
    "Xfail, failed on vanilla as well.",
    "unit/inference/test_inference.py::TestModelTask::test[EleutherAI/gpt-j-6b-text-generation-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert-base-cased-distilled-squad-question-answering-fp32-noCG-noTriton-True-False]":
    "Xfail, failed on vanilla as well.",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert-base-cased-distilled-squad-question-answering-bf16-CG-noTriton-True-False]":
    "Xfail, failed on vanilla as well.",
    "unit/inference/test_inference.py::TestModelTask::test[Norod78/hebrew-bad_wiki-gpt_neo-tiny-text-generation-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_inference.py::TestModelTask::test[EleutherAI/gpt-j-6b-text-generation-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163098.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1024-fp16]":
    "Xfail, due to FP16 not supported.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[64-fp16]":
    "Xfail, due to FP16 not supported.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1048576-fp16]":
    "Xfail, due to FP16 not supported.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[128-fp16]":
    "Xfail, due to FP16 not supported.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[22-fp16]":
    "Xfail, due to FP16 not supported.",
    "unit/runtime/test_ds_initialize.py::TestOptimizerImplementation::test[fp16-fp32-zero3]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_ds_initialize.py::TestOptimizerImplementation::test[fp16-bf16-zero3]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_model_quantization":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_zero3_int4_post_init_quant":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_zero3_int4_quantized_initialization_nvme_offload":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_zero3_int4_post_init_quant_cpu_offload":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_half_int4_quantization":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_zero3_int4_quantized_initialization_cpu_offload":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_quantized_linear":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_half_int8_quantization":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_zero3_int4_quantized_initialization":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_zero3_int4_post_init_quant_nvme_offload":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_pipeline_checkpoint_loading[3-False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-3-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[none-3-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[True-MuAdamW-AdamW]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[True-MuSGD-SGD]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[False-MuAdam-Adam]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[False-MuAdamW-AdamW]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[True-MuAdam-Adam]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[False-MuSGD-SGD]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_save_exclude_frozen_weights[2]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_save_exclude_frozen_weights[1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-1-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-2-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[none-2-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[none-1-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TesthpZeroConfigSweep::test[2-20-2000]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TesthpZeroConfigSweep::test[1-8-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TesthpZeroConfigSweep::test[1-20-2000]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TesthpZeroConfigSweep::test[2-8-2000]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TesthpZeroConfigSweep::test[4-20-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TesthpZeroConfigSweep::test[4-8-2000]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TesthpZeroConfigSweep::test[4-20-2000]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TesthpZeroConfigSweep::test[1-8-2000]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TesthpZeroConfigSweep::test[2-8-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TesthpZeroConfigSweep::test[1-20-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TesthpZeroConfigSweep::test[2-20-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TesthpZeroConfigSweep::test[4-8-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TestSecondaryTensorSize::test[2-8-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TestSecondaryTensorSize::test[2-20-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TestSecondaryTensorSize::test[4-20-4000]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TestSecondaryTensorSize::test[4-8-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TestSecondaryTensorSize::test[2-8-4000]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TestSecondaryTensorSize::test[4-20-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TestSecondaryTensorSize::test[2-20-4000]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TestSecondaryTensorSize::test[4-8-4000]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_qgzero.py::TesthpZeroConfigSweep::test[20-2000]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_qgzero.py::TesthpZeroConfigSweep::test[8-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_qgzero.py::TesthpZeroConfigSweep::test[20-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_qgzero.py::TesthpZeroConfigSweep::test[8-2000]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_qwzero.py::TesthpZeroConfigSweep::test[8-2048]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_qwzero.py::TesthpZeroConfigSweep::test[20-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_qwzero.py::TesthpZeroConfigSweep::test[8-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_qwzero.py::TesthpZeroConfigSweep::test[20-2048]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_not_load_optimizer_state[2]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_load_optimizer_state[1]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_not_load_optimizer_state[1]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_load_module_only[1]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_load_optimizer_state[4]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_not_load_optimizer_state[4]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_load_module_only[2]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_load_optimizer_state[2]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_load_module_only[4]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[facebook/opt-350m-False]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/test_inference.py::TestLowCpuMemUsage::test[gpt2-False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[4-9-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[2-4-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[1-9-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[2-9-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[1-4-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[4-4-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-1232-255-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-4096-1-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-1232-1-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-1232-1-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-4096-255-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-4096-255-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-1232-255-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-1232-1-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-512-255-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-4096-128-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-1232-128-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-1232-128-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-512-1-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-1232-255-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-512-128-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-512-128-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-512-128-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-512-255-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-1232-128-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-1232-128-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-512-255-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-4096-128-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-512-1-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-4096-255-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-512-255-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-512-128-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-4096-1-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-4096-255-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-4096-1-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-1232-1-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-4096-128-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-512-1-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-4096-1-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-512-1-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-4096-128-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-1232-255-2]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/test_inference.py::TestAutoTP::test[falcon-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe[4]":
    "Xfail, FP16 not supported.",
    "unit/moe/test_moe.py::TestPRMoE::test[2-True]":
    "Xfail, FP16 not supported.",
    "unit/moe/test_moe.py::TestPRMoE::test[2-False]":
    "Xfail, FP16 not supported.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[True-False-1-2]":
    "Xfail, FP16 not supported.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[False-True-2-2]":
    "Xfail, FP16 not supported.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[True-False-2-2]":
    "Xfail, FP16 not supported.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[True-True-2-2]":
    "Xfail, FP16 not supported.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[True-False-1-4]":
    "Xfail, FP16 not supported.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[True-True-1-2]":
    "Xfail, FP16 not supported.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[False-False-1-4]":
    "Xfail, FP16 not supported.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[False-False-1-2]":
    "Xfail, FP16 not supported.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[False-False-2-2]":
    "Xfail, FP16 not supported.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[True-True-1-4]":
    "Xfail, FP16 not supported.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[False-True-1-4]":
    "Xfail, FP16 not supported.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[False-True-1-2]":
    "Xfail, FP16 not supported.",
    "unit/runtime/zero/test_zero_context.py::TestSerialContext::test_subclass_param":
    "Xfail, due to FP16 not supported.",
    "unit/runtime/zero/test_zero_context_ancestry.py::TestSerialParamInit::test_subclass_param_init":
    "Xfail, due to FP16 not supported.",
    "unit/inference/test_inference.py::TestMPSize::test[fp32-gpt-j-False]":
    "Xfail, due to SW-162660.",
    "unit/inference/test_inference.py::TestMPSize::test[bf16-gpt-neo-False]":
    "Xfail, due to SW-175376.",
    "unit/inference/test_inference.py::TestMPSize::test[bf16-gpt-j-False]":
    "Xfail, due to SW-162660.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-256-52-4-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-2048-128-32-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-384-16-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1600-128-25-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1600-128-25-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-128-128-2-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-384-16-3-True-True0]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-160-128-2-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-384-16-3-True-True1]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-2560-128-40-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-4096-128-64-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-160-128-2-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-120-16-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-512-16-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-1024-53-16-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1536-128-24-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-160-128-2-24-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-8192-128-64-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-511-16-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[1-256-2048-32-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[3-1024-54-16-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-1024-21-16-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1600-128-2-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[8-1600-128-2-3-True-True-0.05]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[8-160-128-2-3-True-True-0.1]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[8-1600-128-25-3-True-True-0.05]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[64-160-128-2-24-False-True-0.2]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[64-1600-128-2-4-False-True-0.2]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForwardSmallBatchSize::test_forward_with_small_bsz[8-7-1024-512-16-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForwardSmallBatchSize::test_forward_with_small_bsz[8-7-1024-512-16-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/hybrid_engine/test_he_llama.py::TestHybridEngineLlama::test_functionality[huggyllama/llama-7b-bsz=1]":
    "Xfail, due to FP16 not supported.",
    "unit/hybrid_engine/test_he_llama.py::TestHybridEngineLlama::test_functionality[huggyllama/llama-7b-bsz=2]":
    "Xfail, due to FP16 not supported.",
    "unit/hybrid_engine/test_he_all.py::TestHybridEngineTextGen::test_functionality[facebook/opt-1.3b-bsz=1]":
    "Xfail, due to FP16 not supported.",
    "unit/hybrid_engine/test_he_all.py::TestHybridEngineTextGen::test_functionality[facebook/opt-1.3b-bsz=2]":
    "Xfail, due to FP16 not supported.",
    "unit/hybrid_engine/test_he_all.py::TestHybridEngineTextGen::test_functionality[EleutherAI/gpt-neo-1.3B-bsz=1]":
    "Xfail, due to FP16 not supported.",
    "unit/hybrid_engine/test_he_all.py::TestHybridEngineTextGen::test_functionality[EleutherAI/gpt-neo-1.3B-bsz=2]":
    "Xfail, due to FP16 not supported.",
    "unit/inference/test_stable_diffusion.py::TestStableDiffusion::test":
    "Xfail, due to SW-170181.",
    "unit/runtime/zero/test_zero_offloadpp.py::TestZeroPartialOffloadConfigSweep::test[8-1024]":
    "Xfail, due to FP16 not supported.",
    "unit/runtime/zero/test_zero_offloadpp.py::TestZeroPartialOffloadConfigSweep::test[4-1024]":
    "Xfail, due to FP16 not supported.",
    "unit/compression/test_dequantization.py::TestDequantization::test_dequantize":
    "Xfail, due to SW-168442.",
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[8-fp16]":
    "Xfail, due to Gaudi1 does not support FP16.",
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[16-fp16]":
    "Xfail, due to Gaudi1 does not support FP16.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[none-3-full-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-3-full-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-3-local-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[none-3-local-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestEmptyParameterGroup::test_empty_param_groups[dtype1-True-True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestEmptyParameterGroup::test_empty_param_groups[dtype1-True-False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestEmptyParameterGroup::test_empty_param_groups[dtype1-False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestEmptyParameterGroup::test_empty_param_groups[dtype1-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_model_quantization[8bits]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_half_int8_quantization":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant_nvme_offload":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization_nvme_offload":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant_cpu_offload[4bits]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization[4bits]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_half_int4_quantization":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_quantized_linear[8bits-1]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_quantized_linear[8bits-0]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization_cpu_offload[8bits]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant_cpu_offload[8bits]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization_cpu_offload[4bits]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_quantized_linear[4bits-1]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_quantized_linear[4bits-0]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant[8bits]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization[8bits]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_model_quantization[4bits]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant[4bits]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[none-1-full-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-1-full-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[none-2-full-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-2-full-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[2-True]":
    "Xfail, FP16 not supported.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[2-False]":
    "Xfail, FP16 not supported.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[4-False]":
    "Xfail, FP16 not supported.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[4-True]":
    "Xfail, FP16 not supported.",
    "unit/runtime/half_precision/test_bf16.py::TestZeroDtypeCocktail::test[default-fp16]":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_compile_wrapper.py::TestCustomMethod::test_custom_function":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-1-dtype1]":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-1-dtype1]":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-3-dtype1]":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-2-dtype1]":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[nvme-3-dtype1]":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-2-dtype1]":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-3-dtype1]":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[nvme-2-dtype1]":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_load_config.py::TestConfigLoad::test_set_compiler_fn":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_load_config.py::TestConfigLoad::test_compile_kwargs":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_load_config.py::TestConfigLoad::test_compile":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_load_config.py::TestConfigLoad::test_compile_disabled":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_load_config.py::TestConfigLoad::test_custom_backend":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_load_config.py::TestConfigLoad::test_set_compile_kwargs":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[nvme-3-dtype0]":
    "Not supported on Gaudi1",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[nvme-3-dtype2]":
    "Not supported on Gaudi1",
    "unit/runtime/pipe/test_pipe.py::TestPipeCifar10::test_pipe_use_reentrant[topo_config1]":
    " Comm Init Rank Error.",
    "unit/runtime/pipe/test_pipe.py::TestPipeCifar10::test_pipe_use_reentrant[topo_config2]":
    " Comm Init Rank Error.",
    "unit/utils/test_init_on_device.py::TestOnDevice::test_on_device[hpu]":
    "Xfail, due to SW-178730.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[2-False-False]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[4-True-False]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[4-False-False]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[2-True-False]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_save_exclude_frozen_weights[2-False]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_save_exclude_frozen_weights[1-False]":
    "Fp16 not supported by Gaudi1",
    "unit/moe/test_moe.py::TestMoE::test[True-0-4]":
    "Xfail, due to FP16 not supported",
    "unit/moe/test_moe.py::TestMoE::test[False-0-2]":
    "Xfail, due to FP16 not supported.",
    "unit/moe/test_moe.py::TestMoE::test[True-0-2]":
    "Xfail, due to FP16 not supported.",
    "unit/moe/test_moe.py::TestMoE::test[False-0-4]":
    "Xfail, due to FP16 not supported.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[3-True-True]":
    "Xfail, due to SW-179864.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[3-False-True]":
    "Xfail, due to SW-179864.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[3-True-True]":
    "Xfail, due to SW-179864.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[3-False-True]":
    "Xfail, due to SW-179864.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[3-False-Adam-True]":
    "Xfail, due to SW-179864.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_module_only[3-True]":
    "Xfail, due to SW-179864.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[3-True-deepspeed_adam-True]":
    "Xfail, due to SW-179864.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_load_immediate_save[3-True]":
    "Xfail, due to SW-179864.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_immediate_save_load[3-True]":
    "Xfail, due to SW-179864.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_not_load_optimizer_state[3-True]":
    "Xfail, due to SW-179864.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_module_only[3-True]":
    "Xfail, due to SW-179864.",
    "unit/checkpoint/test_shared_weights.py::TestCheckpointSharedWeights::test_checkpoint_shared_weights[True]":
    "Xfail, due to SW-179861.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[4-False-True]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[2-False-True]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[4-True-True]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[2-True-True]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_pipeline.py::TestPipelineCheckpoint::test_checkpoint_pipe_engine[0-True]":
    "Xfail, due to SW-179868.",
    "unit/checkpoint/test_pipeline.py::TestPipelineCheckpoint::test_checkpoint_pipe_engine[1-True]":
    "Xfail, due to SW-179868.",
    "unit/checkpoint/test_zero_optimizer.py::TestSaveTensorClone::test_save_tensor_clone[True-1-True]":
    "Xfail, due to SW-179873.",
    "unit/checkpoint/test_zero_optimizer.py::TestSaveTensorClone::test_save_tensor_clone[True-2-True]":
    "Xfail, due to SW-179873.",
    "unit/checkpoint/test_zero_optimizer.py::TestSaveTensorClone::test_save_tensor_clone[False-2-True]":
    "Xfail, due to SW-179873.",
    "unit/checkpoint/test_zero_optimizer.py::TestSaveTensorClone::test_save_tensor_clone[False-1-True]":
    "Xfail, due to SW-179873.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_save_exclude_frozen_weights[2-True]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_save_exclude_custom_frozen_weights[1-True]":
    "Xfail, due to SW-179873.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_save_exclude_custom_frozen_weights[2-True]":
    "Xfail, due to SW-179873.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_save_exclude_frozen_weights[1-True]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_pipeline_checkpoint_loading[3-True]":
    "Fp16 not supported by Gaudi1.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[True-False-True-True]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[True-True-True-True]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[True-True-True-True]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[True-True-False-True]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[False-True-True-True]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[True-True-False-True]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[False-False-True-True]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[False-True-False-True]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[True-False-False-True]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[True-False-False-True]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[False-True-True-True]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[False-True-False-True]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[False-False-True-True]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[False-False-False-True]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[False-False-False-True]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[True-False-True-True]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[True-False-True-False]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[True-True-True-False]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[True-True-True-False]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[True-True-False-False]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[False-True-True-False]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[True-True-False-False]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[False-False-True-False]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[False-True-False-False]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[True-False-False-False]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[True-False-False-False]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[False-True-True-False]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[False-True-False-False]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[False-False-True-False]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[False-False-False-False]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[False-False-False-False]":
    "Fp16 not supported by Gaudi1",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[True-False-True-False]":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/comm/test_coalesced_collectives.py::TestReduceScatterCoalescedTensorSmallerThanWorldSize::test":
    "fp16 is not supported Gaudi.",
    "unit/runtime/comm/test_coalesced_collectives.py::TestReduceScatterCoalesced::test_single_input":
    "fp16 is not supported Gaudi.",
    "unit/runtime/comm/test_coalesced_collectives.py::TestReduceScatterCoalesced::test_two_inputs":
    "fp16 is not supported Gaudi.",
    "unit/runtime/test_ds_initialize.py::TestNoOptim::test[3]":
    "fp16 is not supported Gaudi.",
    "unit/runtime/zero/test_zero_context.py::TestGatherUpdate::test":
    "fp16 is not supported Gaudi.",
    "unit/runtime/zero/test_zero_context.py::TestScatterGather::test":
    "fp16 is not supported Gaudi.",
    "unit/runtime/zero/test_zero_context_ancestry.py::TestDSInitWZinit::test":
    "fp16 is not supported Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[cpu-3-full-True]":
    "fp16 is not supported Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[none-3-full-True]":
    "fp16 is not supported Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[none-3-local-True]":
    "fp16 is not supported Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[cpu-3-local-True]":
    "fp16 is not supported Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[cpu-3-local-False]":
    "fp16 is not supported Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[none-3-local-False]":
    "fp16 is not supported Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[none-3-full-False]":
    "fp16 is not supported Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[cpu-3-full-False]":
    "fp16 is not supported Gaudi.",
    "unit/runtime/test_data_efficiency.py::TestLegacyCurriculumScheduler::test_fixed_discrete":
    "fp16 is not supported Gaudi.",
    "unit/runtime/test_data_efficiency.py::TestLegacyCurriculumScheduler::test_fixed_linear":
    "fp16 is not supported Gaudi.",
    "unit/runtime/test_data_efficiency.py::TestDataEfficiency::test_curriculum_learning":
    "fp16 is not supported Gaudi.",
    "unit/runtime/test_ds_config_dict.py::TestConfigLoad::test_hjson":
    "fp16 is not supported Gaudi.",
    "unit/runtime/test_ds_config_dict.py::TestConfigLoad::test_dict":
    "fp16 is not supported Gaudi.",
    "unit/runtime/test_ds_config_dict.py::TestConfigLoad::test_json":
    "fp16 is not supported Gaudi.",
    "unit/runtime/test_ds_config_dict.py::TestDistInit::test":
    "fp16 is not supported Gaudi.",
    "unit/runtime/test_ds_config_dict.py::TestDeprecatedDeepScaleConfig::test":
    "fp16 is not supported Gaudi.",
    "unit/runtime/test_ds_config_dict.py::TestArgs::test_none_args":
    "fp16 is not supported Gaudi.",
    "unit/runtime/test_ds_config_dict.py::TestArgs::test_no_args":
    "fp16 is not supported Gaudi.",
    "unit/runtime/test_ds_config_dict.py::TestInitNoOptimizer::test":
    "fp16 is not supported Gaudi.",
    "unit/runtime/test_ds_initialize.py::TestNoOptim::test[0]":
    "fp16 is not supported Gaudi.",
    "unit/runtime/zero/test_ignore_unused_parameters.py::TestStage2IgnoreUnusedParameters::test[True]":
    "fp16 is not supported Gaudi.",
    "unit/runtime/zero/test_ignore_unused_parameters.py::TestStage2IgnoreUnusedParameters::test[False]":
    "fp16 is not supported Gaudi.",
    "unit/checkpoint/test_other_optimizer.py::TestOtherOptimizerCheckpoint::test_checkpoint_fused_optimizer[False]":
    "fp16 is not supported Gaudi.",
    "unit/runtime/test_pld.py::TestNonPLDModel::test_non_pld_model":
    "fp16 is not supported Gaudi.",
    "unit/runtime/test_pld.py::TestPLDModel::test_pld_model[0.1]":
    "fp16 is not supported Gaudi.",
    "unit/runtime/test_pld.py::TestPLDModel::test_pld_model[1.0]":
    "fp16 is not supported Gaudi.",
    "unit/runtime/test_pld.py::TestPLDModel::test_pld_model[0.9]":
    "fp16 is not supported Gaudi.",
    "unit/runtime/test_pld.py::TestPLDModel::test_pld_model[0]":
    "fp16 is not supported Gaudi.",
    "unit/runtime/zero/test_zero_context.py::TestSerialContext::test_ext_param_getattr":
    "fp16 is not supported Gaudi.",
    "unit/runtime/zero/test_zero_context_return.py::TestReturnParam::test_stage_3_output_type[dict]":
    "fp16 is not supported Gaudi.",
    "unit/runtime/zero/test_zero_context_return.py::TestReturnParam::test_ext_param_return":
    "fp16 is not supported Gaudi.",
    "unit/runtime/zero/test_zero_context_return.py::TestReturnParam::test_stage_3_output_type[tensor]":
    "fp16 is not supported Gaudi.",
    "unit/runtime/zero/test_zero_context_return.py::TestReturnParam::test_stage_3_output_type[None]":
    "fp16 is not supported Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[none-1-full-False]":
    "fp16 is not supported Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[cpu-1-full-False]":
    "fp16 is not supported Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[cpu-2-full-False]":
    "fp16 is not supported Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[cpu-2-full-True]":
    "fp16 is not supported Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[none-1-full-True]":
    "fp16 is not supported Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[cpu-1-full-True]":
    "fp16 is not supported Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[none-2-full-True]":
    "fp16 is not supported Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[none-2-full-False]":
    "fp16 is not supported Gaudi.",
    "unit/hybrid_engine/test_he_lora.py::TestHybridEngineLoRA::test_lora[cpu-facebook/opt-350m-zero_stage=2-bsz=1]":
    "fp16 is not supported Gaudi.",
    "unit/hybrid_engine/test_he_lora.py::TestHybridEngineLoRA::test_lora[cpu-EleutherAI/gpt-neo-125m-zero_stage=3-bsz=1]":
    "fp16 is not supported Gaudi.",
    "unit/hybrid_engine/test_he_lora.py::TestHybridEngineLoRA::test_lora[cpu-EleutherAI/gpt-neo-125m-zero_stage=2-bsz=1]":
    "fp16 is not supported Gaudi.",
    "unit/hybrid_engine/test_he_lora.py::TestHybridEngineLoRA::test_lora[none-facebook/opt-350m-zero_stage=3-bsz=1]":
    "fp16 is not supported Gaudi.",
    "unit/hybrid_engine/test_he_lora.py::TestHybridEngineLoRA::test_lora[none-facebook/opt-350m-zero_stage=2-bsz=1]":
    "fp16 is not supported Gaudi.",
    "unit/hybrid_engine/test_he_lora.py::TestHybridEngineLoRA::test_lora[cpu-bigscience/bloom-560m-zero_stage=2-bsz=1]":
    "fp16 is not supported Gaudi.",
    "unit/hybrid_engine/test_he_lora.py::TestHybridEngineLoRA::test_lora[none-EleutherAI/gpt-neo-125m-zero_stage=3-bsz=1]":
    "fp16 is not supported Gaudi.",
    "unit/hybrid_engine/test_he_lora.py::TestHybridEngineLoRA::test_lora[cpu-facebook/opt-350m-zero_stage=3-bsz=1]":
    "fp16 is not supported Gaudi.",
    "unit/hybrid_engine/test_he_lora.py::TestHybridEngineLoRA::test_lora[none-EleutherAI/gpt-neo-125m-zero_stage=2-bsz=1]":
    "fp16 is not supported Gaudi.",
    "unit/hybrid_engine/test_he_lora.py::TestHybridEngineLoRA::test_lora[none-bigscience/bloom-560m-zero_stage=2-bsz=1]":
    "fp16 is not supported Gaudi.",
    "unit/hybrid_engine/test_he_lora.py::TestHybridEngineLoRA::test_lora[none-bigscience/bloom-560m-zero_stage=3-bsz=1]":
    "fp16 is not supported Gaudi.",
    "unit/hybrid_engine/test_he_lora.py::TestHybridEngineLoRA::test_lora[cpu-bigscience/bloom-560m-zero_stage=3-bsz=1]":
    "fp16 is not supported Gaudi.",
    "unit/checkpoint/test_other_optimizer.py::TestOtherOptimizerCheckpoint::test_checkpoint_fused_optimizer[True]":
    "fp16 is not supported Gaudi.",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[EleutherAI/gpt-j-6B-False]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[EleutherAI/gpt-neo-125M-False]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[bigscience/bloom-560m]-False":
    "float16/half is not supported on Gaudi.",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[facebook/opt-125m-False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_autocast.py::TestAutoCastDisable::test_missing_amp_autocast[True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[3-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[3-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[3-True-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[3-True-False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZero3InitForParentWeightInitialization::test":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningManyParams::test[True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroPartitionCache::test_training_partition_cache[False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroPartitionCache::test_training_partition_cache[True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZero3DictFwd::test[list]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZero3DictFwd::test[tuple]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZero3DictFwd::test[dict]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningLargeParam::test[True-True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningLargeParam::test[False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroFrozenWeights::test[3]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_context.py::TestSerialContext::test_scatter_halftype":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_module_only[3-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_optimizer_state[3-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_not_load_optimizer_state[3-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[3-True-deepspeed_adam-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_module_only[3-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[3-False-Adam-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[3-True-deepspeed_adam-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[3-False-Adam-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestSaveTensorClone::test_save_tensor_clone[False-1-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestSaveTensorClone::test_save_tensor_clone[True-1-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestSaveTensorClone::test_save_tensor_clone[False-2-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestSaveTensorClone::test_save_tensor_clone[True-2-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[2-True-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[1-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[2-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[0-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[1-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[0-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[2-True-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[2-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe.py::TestMoE::test[False-2-2]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe.py::TestMoE::test[False-2-4]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe.py::TestMoE::test[True-1-2]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe.py::TestMoE::test[True-2-2]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe.py::TestMoE::test[False-1-2]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe.py::TestMoE::test[True-2-4]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe.py::TestMoE::test[False-1-4]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe.py::TestMoE::test[True-1-4]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_pipeline.py::TestPipelineCheckpoint::test_checkpoint_pipe_engine[1-False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestPartitionNcclAlignment::test":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroUnbalancedGradients::test[3]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroUnbalancedGradients::test[1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroUnbalancedGradients::test[2]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningManyParams::test[False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroOffloadStage1::test":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroToFP32::test_2_param_groups[False-2]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroToFP32::test_2_param_groups[True-3]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroToFP32::test_2_param_groups[True-2]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroToFP32::test_1_param_group[False-2]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroToFP32::test_1_param_group[True-2]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroToFP32::test_1_param_group[True-3]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroToFP32::test_2_param_groups[False-3]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroToFP32::test_1_param_group[False-3]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestIncorectAllgatherBucketSize::test[1001]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestIncorectAllgatherBucketSize::test[1000]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroAdamOptimizerStepCount::test[1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroAdamOptimizerStepCount::test[2]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroAdamOptimizerStepCount::test[3]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningLargeParam::test[True-False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningLargeParam::test[False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZero3RepeatForwardLoop::test":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroFrozenWeights::test[2]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroFrozenWeights::test[1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningBase::test_fp16_enabled[True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroOffloadOptim::test[True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroOffloadOptim::test[False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_module_only[2-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_not_load_optimizer_state[1-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_optimizer_state[1-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_module_only[1-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_not_load_optimizer_state[2-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_save_exclude_custom_frozen_weights[2-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_save_exclude_custom_frozen_weights[1-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_optimizer_state[2-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_immediate_save_load[0-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_load_immediate_save[3-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_save_before_accum_grad_is_done[3-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_save_before_accum_grad_is_done[2-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_save_before_accum_grad_is_done[0-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_load_immediate_save[1-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_load_immediate_save[2-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_immediate_save_load[3-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_load_immediate_save[0-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_immediate_save_load[1-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_immediate_save_load[2-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_save_before_accum_grad_is_done[1-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_module_only[0-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[2-True-deepspeed_adam-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[1-False-Adam-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_module_only[1-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[2-False-Adam-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[1-False-Adam-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[2-True-deepspeed_adam-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_hybrid_optimizer_state[2-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_hybrid_optimizer_state[1-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[2-False-Adam-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_module_only[2-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_module_only[2-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[1-False-Adam-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[1-False-Adam-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_module_only[1-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_module_only[0-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[2-False-Adam-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_hybrid_optimizer_state[2-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[2-True-deepspeed_adam-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[2-True-deepspeed_adam-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_hybrid_optimizer_state[1-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[2-False-Adam-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_load_immediate_save[2-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_load_immediate_save[1-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_load_immediate_save[0-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_save_before_accum_grad_is_done[3-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_immediate_save_load[2-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_save_before_accum_grad_is_done[2-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_save_before_accum_grad_is_done[1-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_immediate_save_load[0-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_save_before_accum_grad_is_done[0-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_immediate_save_load[1-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_not_load_optimizer_state[2-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_optimizer_state[2-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_optimizer_state[1-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_not_load_optimizer_state[1-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_module_only[1-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_module_only[2-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[2-False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[1-False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[0-False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[2-True-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[0-False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[2-False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[2-True-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[1-False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[3-False-Adam-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[3-True-deepspeed_adam-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_optimizer_state[3-True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test_gradient_accumulation[1-9-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test_eval[2-9-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test_gradient_accumulation[4-9-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test_eval[1-9-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test_eval[4-9-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test_gradient_accumulation[2-9-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert/distilgpt2-text-generation-bf16-noCG-noTriton-False-False]":
    "Xfail due to SW-182748",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/accelerator/test_accelerator.py::test_abstract_methods_defined[deepspeed.accelerator.xpu_accelerator]":
    "Xfail due to SW-182749",
    "unit/runtime/comm/test_coalesced_collectives.py::TestAllToAllQuantReduceFallback::test_non_divisible":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/comm/test_coalesced_collectives.py::TestAllToAllQuantReduceFallback::test_1d_tensor":
    "float16/half is not supported on Gaudi.",
    "unit/utils/test_init_on_device.py::TestOnDevice::test_on_device[hpu:0]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestParamPartitioningSkipInit::test":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZero3RepeatForwardLoop::test[True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZero3RepeatForwardLoop::test[False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_leaf_module.py::TestSetZ3LeafModule::test_no_grad_input_error":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_leaf_module.py::TestSetZ3LeafModule::test_choose_module_by_counter":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_leaf_module.py::TestSetZ3LeafModule::test_choose_module_by_rank":
    "float16/half is not supported on Gaudi.",
    "unit/launcher/test_user_args.py::test_user_args[True-I'm going to tell them \"DeepSpeed is the best\"]":
    "Xfail due to SW-182753",
    "unit/launcher/test_user_args.py::test_user_args[True-'\"translate English to Romanian: \"']":
    "Xfail due to SW-182753",
    "unit/launcher/test_user_args.py::test_user_args[True-'I am 72\" tall']":
    "Xfail due to SW-182753",
    "unit/launcher/test_user_args.py::test_user_args[True-\"I am 6' tall\"]":
    "Xfail due to SW-182753",
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-openai-community/gpt2-xl]":
    "xfail due to model download",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-bf16-CG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-bf16-noCG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-bf16-noCG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-bf16-noCG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-bf16-CG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-bf16-CG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-bf16-CG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-bf16-noCG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-bf16-noCG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-bf16-CG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-bf16-noCG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-bf16-noCG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-bf16-CG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-bf16-CG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert/distilgpt2-text-generation-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-125m-text-generation-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[Norod78/hebrew-bad_wiki-gpt_neo-tiny-text-generation-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[openai-community/gpt2-text-generation-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported on Gaudi",
    "unit/inference/test_inference.py::TestMPSize::test[fp16-gpt-neo-False]":
    "Xfail due to FP16 not supported on gaudi",
    "unit/inference/test_inference.py::TestMPSize::test[fp16-bloom-False]":
    "Xfail due to FP16 not supported on gaudi",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[False-False-False-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[False-False-False-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[False-True-False-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[False-True-True-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[False-True-False-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[False-False-True-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[False-False-False-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[False-True-True-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[False-True-False-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[False-True-True-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[False-False-True-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[False-False-True-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[bigscience/bloom-560m-False]":
    "Xfail due to FP16 not supported",
    "unit/moe/test_moe.py::TestSimpleMoE::test[2]":
    "Xfail due to fp16 not supported",
    "unit/moe/test_moe.py::TestSimpleMoE::test[1]":
    "Xfail due to fp16 not supported",
    "unit/moe/test_moe.py::TestSimpleMoE::test[0]":
    "Xfail due to fp16 not supported",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test_odd_world_size[fp16-marian-True-False]":
    "Xfail due to fp16 not supported",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test[fp16-marian-True-False]":
    "Xfail due to fp16 not supported",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test[fp16-marian-False-False]":
    "Xfail due to fp16 not supported",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test_odd_world_size[fp16-marian-False-False]":
    "Xfail due to fp16 not supported",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test[bf16-marian-True-False]":
    "Xfail due to SW-205776",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test_odd_world_size[bf16-marian-True-False]":
    "Xfail due to SW-205776",
}

g2_lazy_xfail_tests = {
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[8-fp16]":"Xfail, due to SW-201661.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-uncased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-cased-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-uncased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-uncased-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-large-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-base-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-cased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-base-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-uncased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-cased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-cased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-large-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-cased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-uncased-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-uncased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-cased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-base-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-cased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-large-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-uncased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-cased-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-cased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-uncased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-cased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-cased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-large-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-base-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-base-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-uncased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-large-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-uncased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-base-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-cased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-large-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-cased-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-cased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-cased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[EleutherAI/pythia-70m-deduped-text-generation-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163095.",
    "unit/inference/test_inference.py::TestModelTask::test[EleutherAI/pythia-70m-deduped-text-generation-fp16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163095.",
    "unit/inference/test_inference.py::TestModelTask::test[EleutherAI/pythia-70m-deduped-text-generation-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163095.",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert-base-cased-distilled-squad-question-answering-fp16-noCG-noTriton-True-False]":
    "Xfail, failed on vanilla as well.",
    "unit/inference/test_inference.py::TestModelTask::test[EleutherAI/gpt-j-6b-text-generation-fp16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert-base-cased-distilled-squad-question-answering-fp32-CG-noTriton-True-False]":
    "Xfail, failed on vanilla as well.",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert-base-cased-distilled-squad-question-answering-fp32-noCG-noTriton-True-False]":
    "Xfail, failed on vanilla as well.",
    "unit/inference/test_inference.py::TestModelTask::test[EleutherAI/gpt-j-6b-text-generation-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert-base-cased-distilled-squad-question-answering-bf16-noCG-noTriton-True-False]":
    "Xfail, failed on vanilla as well.",
    "unit/inference/test_inference.py::TestModelTask::test[Norod78/hebrew-bad_wiki-gpt_neo-tiny-text-generation-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert-base-cased-distilled-squad-question-answering-bf16-CG-noTriton-True-False]":
    "Xfail, failed on vanilla as well.",
    "unit/inference/test_inference.py::TestModelTask::test[EleutherAI/gpt-j-6b-text-generation-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_inference.py::TestModelTask::test[gpt2-text-generation-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert-base-cased-distilled-squad-question-answering-fp16-CG-noTriton-True-False]":
    "Xfail, failed on vanilla as well.",
    "unit/inference/test_model_profiling.py::TestModelProfiling::test[False-False]": # noqa: F601
    "Xfail, due to SW-163097.",
    "unit/inference/test_model_profiling.py::TestModelProfiling::test[False-True]": # noqa: F601
    "Xfail, due to SW-163097.",
    "unit/inference/test_model_profiling.py::TestModelProfiling::test[True-False]": # noqa: F601
    "Xfail, due to SW-163097.",
    "unit/inference/test_model_profiling.py::TestModelProfiling::test[True-True]": # noqa: F601
    "Xfail, due to SW-163097.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-512-16-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-384-16-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1600-128-2-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-120-16-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-160-128-2-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-256-52-4-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-8192-128-64-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-1024-53-16-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-160-128-2-24-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-128-128-2-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1600-128-25-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-4096-128-64-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1536-128-24-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-384-16-3-True-True0]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-160-128-2-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-2048-128-32-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-2560-128-40-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1600-128-25-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[1-256-2048-32-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-1024-21-16-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-384-16-3-True-True1]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[3-1024-54-16-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-511-16-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[8-1600-128-2-3-True-True-0.05]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[64-1600-128-2-4-False-True-0.2]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[8-160-128-2-3-True-True-0.1]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[8-1600-128-25-3-True-True-0.05]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[64-160-128-2-24-False-True-0.2]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForwardSmallBatchSize::test_forward_with_small_bsz[8-7-1024-512-16-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForwardSmallBatchSize::test_forward_with_small_bsz[8-7-1024-512-16-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/inference/test_inference.py::TestMPSize::test[fp32-gpt-j-False]":
    "Xfail, due to SW-162660.",
    "unit/inference/test_inference.py::TestMPSize::test[bf16-gpt-neo-False]":
    "Xfail, due to SW-.",
    "unit/inference/test_inference.py::TestMPSize::test[bf16-gpt-j-False]":
    "Xfail, due to SW-162660.",
    "unit/inference/test_inference.py::TestMPSize::test[fp16-bloom-False]":
    "Xfail, due to SW-.",
    "unit/inference/test_inference.py::TestMPSize::test[fp16-gpt-j-False]":
    "Xfail, due to SW-162660.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[4-4-1024]":
    "Xfail, due to SW-164239.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[2-4-1024]":
    "Xfail, due to SW-164239.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[1-9-1024]":
    "Xfail, due to SW-164239.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[4-9-1024]":
    "Xfail, due to SW-164239.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[1-4-1024]":
    "Xfail, due to SW-164239.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[2-9-1024]":
    "Xfail, due to SW-164239.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[22-fp16]":
    "Xfail, due to SW-162575.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1048576-fp16]":
    "Xfail, due to SW-162575.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1024-fp16]":
    "Xfail, due to SW-162575.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[128-fp16]":
    "Xfail, due to SW-162575.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[64-fp16]":
    "Xfail, due to SW-162575.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_zero3_int4_post_init_quant_cpu_offload":
    "Xfail, due to SW-162660.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_zero3_int4_quantized_initialization":
    "Xfail, due to SW-162660.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_zero3_int4_post_init_quant":
    "Xfail, due to SW-162660.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_zero3_int4_quantized_initialization_cpu_offload":
    "Xfail, due to SW-162660.",
    "unit/runtime/zero/test_zero_context.py::TestSerialContext::test_subclass_param":
    "Xfail, due to SW-156783.",
    "unit/runtime/zero/test_zero_context_ancestry.py::TestSerialParamInit::test_subclass_param_init":
    "Xfail, due to SW-143227.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-1-dtype1]":
    "Xfail, due to SW-145262.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-3-dtype1]":
    "Xfail, due to SW-145262.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-2-dtype1]":
    "Xfail, due to SW-145262.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_zero3_int4_quantized_initialization_nvme_offload":
    "Xfail, due to SW-164545.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_zero3_int4_post_init_quant_nvme_offload":
    "Xfail, due to SW-164545.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[False-MuSGD-SGD]":
    "Xfail, due to SW-164551.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[True-MuSGD-SGD]":
    "Xfail, due to SW-164551.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[True-MuAdam-Adam]":
    "Xfail, due to SW-164551.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[False-MuAdam-Adam]":
    "Xfail, due to SW-164551.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[True-MuAdamW-AdamW]":
    "Xfail, due to SW-164551.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[False-MuAdamW-AdamW]":
    "Xfail, due to SW-164551.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_load_optimizer_state[4]":
    "Xfail, due to SW-164577.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_not_load_optimizer_state[4]":
    "Xfail, due to SW-164577.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_not_load_optimizer_state[1]":
    "Xfail, due to SW-164577.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_load_optimizer_state[2]":
    "Xfail, due to SW-164577.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_load_module_only[4]":
    "Xfail, due to SW-164577.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_load_module_only[1]":
    "Xfail, due to SW-164577.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_not_load_optimizer_state[2]":
    "Xfail, due to SW-164577.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_load_optimizer_state[1]":
    "Xfail, due to SW-164577.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_load_module_only[2]":
    "Xfail, due to SW-164577.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[none-3-dtype1]":
    "Xfail, due to SW-164593.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_quantized_linear":
    "Xfail, due to SW-164606.",
    "unit/runtime/zero/test_qwzero.py::TesthpZeroConfigSweep::test[20-1024]":
    "Xfail, due to SW-156782.",
    "unit/runtime/zero/test_qwzero.py::TesthpZeroConfigSweep::test[20-2048]":
    "Xfail, due to SW-156782.",
    "unit/runtime/zero/test_qwzero.py::TesthpZeroConfigSweep::test[8-2048]":
    "Xfail, due to SW-156782.",
    "unit/runtime/zero/test_qwzero.py::TesthpZeroConfigSweep::test[8-1024]":
    "Xfail, due to SW-156782.",
    "unit/inference/test_inference.py::TestModelTask::test[EleutherAI/gpt-j-6b-text-generation-fp32-noCG-noTriton-False-False]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_stable_diffusion.py::TestStableDiffusion::test": # noqa: F601
    "Xfail, due to SW-170181.",
    "unit/compression/test_dequantization.py::TestDequantization::test_dequantize": # noqa: F601
    "Xfail, due to SW-168442.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_quantized_linear[4bits-0]":
    "Xfail, due to SW-168583.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_quantized_linear[8bits-1]":
    "Xfail, due to SW-168583.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_quantized_linear[4bits-1]":
    "Xfail, due to SW-168583.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_quantized_linear[8bits-0]":
    "Xfail, due to SW-168583.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant[4bits]":
    "Xfail, due to SW-162660.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant_cpu_offload[4bits]":
    "Xfail, due to SW-162660.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization[8bits]":
    "Xfail, due to SW-162660.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization_cpu_offload[4bits]":
    "Xfail, due to SW-162660.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant_cpu_offload[8bits]":
    "Xfail, due to SW-162660.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization[4bits]":
    "Xfail, due to SW-162660.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization_cpu_offload[8bits]":
    "Xfail, due to SW-162660.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant[8bits]":
    "Xfail, due to SW-162660.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant_nvme_offload":
    "Xfail, due to SW-164545.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization_nvme_offload":
    "Xfail, due to SW-164545.",
    "unit/ops/lion/test_lion.py::TestLionConfigs::test[Lion-True-DeepSpeedCPULion]":
    "skipping due to HPU is not supported FusedLion, SW-176903",
    "unit/ops/lion/test_lion.py::TestLionConfigs::test[Lion-False-FusedLion]":
    "skipping due to HPU is not supported FusedLion, SW-176903",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForwardSmallBatchSize::test_forward_with_small_bsz[8-3-1024-512-16-3-True-False]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForwardSmallBatchSize::test_forward_with_small_bsz[8-3-1024-512-16-3-False-False]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-128-128-2-3-True-False]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1536-128-24-3-False-False]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-509-16-3-True-False]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-1024-24-16-3-False-False]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-2048-128-32-3-False-False]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-381-16-3-True-False]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-384-16-3-False-False]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-1024-56-16-3-False-False]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[3-1024-51-16-3-True-False]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-119-16-3-True-False]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-512-16-3-False-False]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-2560-128-40-3-False-False]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/utils/test_init_on_device.py::TestOnDevice::test_on_device[hpu]" : "Xfail, due to SW-178730.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[3-True-True]" : "Xfail, due to SW-179864.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[3-False-True]" : "Xfail, due to SW-179864.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[3-True-True]" : "Xfail, due to SW-179864.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[3-False-True]" : "Xfail, due to SW-179864.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[3-False-Adam-True]" : "Xfail, due to SW-179864.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_module_only[3-True]" : "Xfail, due to SW-179864.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[3-True-deepspeed_adam-True]" : "Xfail, due to SW-179864.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_load_immediate_save[3-True]" : "Xfail, due to SW-179864.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_immediate_save_load[3-True]" : "Xfail, due to SW-179864.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[False-False-False-True]" : "Xfail, due to SW-179864.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[False-False-True-True]" : "Xfail, due to SW-179864.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[False-True-True-True]" : "Xfail, due to SW-179864.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[False-True-False-True]" : "Xfail, due to SW-179864.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_not_load_optimizer_state[3-True]" : "Xfail, due to SW-179864.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_module_only[3-True]" : "Xfail, due to SW-179864.",
    "unit/checkpoint/test_shared_weights.py::TestCheckpointSharedWeights::test_checkpoint_shared_weights[True]" : "Xfail, due to SW-179861.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[4-False-True]" :  "Xfail, due to SW-179867.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[2-False-True]" : "Xfail, due to SW-179867.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[4-True-True]" : "Xfail, due to SW-179867.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[2-True-True]" : "Xfail, due to SW-179867.",
    "unit/checkpoint/test_pipeline.py::TestPipelineCheckpoint::test_checkpoint_pipe_engine[0-True]" : "Xfail, due to SW-179868.",
    "unit/checkpoint/test_pipeline.py::TestPipelineCheckpoint::test_checkpoint_pipe_engine[1-True]" : "Xfail, due to SW-179868.",
    "unit/checkpoint/test_zero_optimizer.py::TestSaveTensorClone::test_save_tensor_clone[True-1-True]" : "Xfail, due to SW-179873.",
    "unit/checkpoint/test_zero_optimizer.py::TestSaveTensorClone::test_save_tensor_clone[True-2-True]" : "Xfail, due to SW-179873.",
    "unit/checkpoint/test_zero_optimizer.py::TestSaveTensorClone::test_save_tensor_clone[False-2-True]" : "Xfail, due to SW-179873.",
    "unit/checkpoint/test_zero_optimizer.py::TestSaveTensorClone::test_save_tensor_clone[False-1-True]" : "Xfail, due to SW-179873.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_save_exclude_frozen_weights[2-True]" : "Xfail, due to SW-179873.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_save_exclude_custom_frozen_weights[1-True]" : "Xfail, due to SW-179873.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_save_exclude_custom_frozen_weights[2-True]" : "Xfail, due to SW-179873.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_save_exclude_frozen_weights[1-True]" : "Xfail, due to SW-179873.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_pipeline_checkpoint_loading[3-True]" : "Xfail, due to SW-175716.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-3-dtype1]" : "Xfail, due to SW-175716.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[nvme-3-dtype2]" : "Xfail, due to SW-175716.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-3-dtype1]" : "Xfail, due to SW-175716.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[nvme-3-dtype0]" : "Xfail, due to SW-175716.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[nvme-3-dtype1]" : "Xfail, due to SW-175716.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[True-False-True-True]" : "Xfail, due to SW-180488.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[True-True-True-True]" : "Xfail, due to SW-180488.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[True-True-False-True]" : "Xfail, due to SW-180488.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[True-False-False-True]" : "Xfail, due to SW-180488.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[True-True-True-True]" : "Xfail, due to SW-179873.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[True-True-False-True]" : "Xfail, due to SW-179873.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[True-False-False-True]" : "Xfail, due to SW-179873.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[True-False-True-True]" : "Xfail, due to SW-179873.",
    "unit/checkpoint/test_other_optimizer.py::TestOtherOptimizerCheckpoint::test_checkpoint_fused_optimizer[True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_other_optimizer.py::TestOtherOptimizerCheckpoint::test_checkpoint_fp32_optimizer[True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[False-True-False-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[False-False-True-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[False-False-False-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[False-True-True-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[2-True-deepspeed_adam-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[2-True-deepspeed_adam-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[2-False-Adam-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_module_only[2-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_module_only[1-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_hybrid_optimizer_state[2-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[1-False-Adam-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_hybrid_optimizer_state[1-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[2-False-Adam-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[1-False-Adam-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_module_only[0-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_not_load_optimizer_state[2-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_module_only[2-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_optimizer_state[2-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_module_only[1-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_not_load_optimizer_state[1-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_optimizer_state[1-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_save_before_accum_grad_is_done[2-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_save_before_accum_grad_is_done[0-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_save_before_accum_grad_is_done[1-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_save_before_accum_grad_is_done[3-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_load_immediate_save[1-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_load_immediate_save[2-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_load_immediate_save[0-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_latest_checkpoint.py::TestLatestCheckpoint::test_existing_latest[True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[0-False-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[1-False-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[1-False-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[2-True-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[0-False-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[2-False-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[2-True-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[2-False-True]" : "Xfail, due to SW-180868.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[3-True-deepspeed_adam-True]" : "Xfail, due to SW-175716.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[3-False-Adam-True]" : "Xfail, due to SW-175716.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_optimizer_state[3-True]" : "Xfail, due to SW-175716.",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert/distilgpt2-text-generation-bf16-noCG-noTriton-False-False]":"Xfail due to SW-182748",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-bf16-noCG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-bf16-noCG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp16-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp32-noCG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-bf16-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp16-noCG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp16-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp16-noCG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp16-noCG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-bf16-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp16-noCG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-bf16-noCG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-bf16-noCG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-bf16-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-bf16-noCG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp16-noCG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-bf16-noCG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-noCG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-bf16-noCG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp16-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp32-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-bf16-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp32-noCG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp32-noCG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp16-noCG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp16-noCG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp32-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp16-noCG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-bf16-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp32-noCG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp32-noCG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-bf16-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-bf16-noCG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp32-noCG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp16-noCG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp32-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp32-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp16-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-bf16-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp32-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-bf16-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp32-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp32-noCG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp32-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp32-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp16-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp32-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-bf16-noCG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp16-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp16-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp16-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp32-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp16-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-bf16-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp16-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp16-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-bf16-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp32-noCG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-bf16-CG-noTriton-True-False]":"xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[openai-community/gpt2-text-generation-bf16-noCG-noTriton-True-False]":"Xfail due to SW-181935",
    "unit/launcher/test_user_args.py::test_user_args[True-I'm going to tell them \"DeepSpeed is the best\"]":"Xfail due to SW-182753",
    "unit/launcher/test_user_args.py::test_user_args[True-'\"translate English to Romanian: \"']":"Xfail due to SW-182753",
    "unit/launcher/test_user_args.py::test_user_args[True-'I am 72\" tall']":"Xfail due to SW-182753",
    "unit/launcher/test_user_args.py::test_user_args[True-\"I am 6' tall\"]":"Xfail due to SW-182753",
    "unit/runtime/zero/test_zero.py::TestParamPartitioningSkipInit::test":"Xfail due to SW-",
    "unit/inference/test_human_eval.py::test_human_eval[codellama/CodeLlama-7b-Python-hf]":"Xfail due to SW-182759",
    "unit/runtime/comm/test_coalesced_collectives.py::TestAllToAllQuantReduceFallback::test_1d_tensor":"Xfail due to SW-182766",
    "unit/runtime/comm/test_coalesced_collectives.py::TestAllToAllQuantReduceFallback::test_non_divisible":"Xfail due to SW-182766",
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-openai-community/gpt2-xl]":"xfail due to model download",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert/distilgpt2-text-generation-bf16-noCG-noTriton-True-False]":"Xfail due to SW-181935",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-bf16-CG-noTriton-False-False]": "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-bf16-noCG-noTriton-False-False]": "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-bf16-noCG-noTriton-False-False]": "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-bf16-noCG-noTriton-False-False]": "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-bf16-CG-noTriton-False-False]": "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-bf16-CG-noTriton-False-False]": "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-bf16-CG-noTriton-False-False]": "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-bf16-noCG-noTriton-False-False]": "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-bf16-noCG-noTriton-False-False]": "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-bf16-CG-noTriton-False-False]": "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-bf16-noCG-noTriton-False-False]": "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-bf16-noCG-noTriton-False-False]": "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-bf16-CG-noTriton-False-False]": "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-bf16-CG-noTriton-False-False]": "xfail due to SW-184834",
    "unit/hybrid_engine/test_he_llama.py::TestHybridEngineLlama::test_functionality[huggyllama/llama-7b-bsz=2]":" xfail due to SW-185015",
    "unit/hybrid_engine/test_he_llama.py::TestHybridEngineLlama::test_functionality[huggyllama/llama-7b-bsz=1]":" xfail due to SW-185015",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_half_int8_quantization":"Xfail due to SW-182766",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_half_int4_quantization":"Xfail due to SW-182766",
    "unit/runtime/zero/test_zero.py::TestZeroToFP32::test_1_param_group[False-3]":"Xfail due to sw-201549",
    "unit/runtime/zero/test_zero.py::TestZeroToFP32::test_2_param_groups[True-3]":"Xfail due to sw-201549",
    "unit/runtime/zero/test_zero.py::TestZeroToFP32::test_1_param_group[True-2]":"Xfail due to sw-201549",
    "unit/runtime/zero/test_zero.py::TestZeroToFP32::test_2_param_groups[False-3]":"Xfail due to sw-201549",
    "unit/runtime/zero/test_zero.py::TestZeroToFP32::test_2_param_groups[True-2]":"Xfail due to sw-201549",
    "unit/runtime/zero/test_zero.py::TestZeroToFP32::test_1_param_group[True-3]":"Xfail due to sw-201549",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[3-False-Adam-False]":"Xfail due to sw-201549",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[3-True-deepspeed_adam-False]":"Xfail due to sw-201549",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_module_only[3-False]":"Xfail due to sw-201549",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_pipeline_checkpoint_loading[3-False]":"Xfail due to sw-201549",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_module_only[3-False]":"Xfail due to sw-201549",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_not_load_optimizer_state[3-False]":"Xfail due to sw-201549",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_immediate_save_load[3-False]":"Xfail due to sw-201549",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_load_immediate_save[3-False]":"Xfail due to sw-201549",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[3-True-False]":"Xfail due to sw-201549",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[3-False-False]":"Xfail due to sw-201549",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[3-True-False]":"Xfail due to sw-201549",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[3-False-False":"Xfail due to sw-201549",
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[16-fp16]":"Xfail due to SW-200127",
    "unit/linear/test_linear.py::TestQuantLinear::test[6]": "AttributeError: 'Parameter' object has no attribute 'dequantized'",
    "unit/linear/test_linear.py::TestQuantLinear::test[8]": "AttributeError: 'Parameter' object has no attribute 'dequantized'",
    "unit/linear/test_linear.py::TestOptimizedLinear::test[qbit8-bws1]": "AttributeError: 'Parameter' object has no attribute 'dequantized'",
    "unit/linear/test_linear.py::TestOptimizedLinear::test[qbit6-bws1]": "AttributeError: 'Parameter' object has no attribute 'dequantized'",
    "unit/linear/test_quant_param.py::TestQuantParam::test_hf_clone": "AssertionError: Quantize fallback only supports quantization to FP8",
    "unit/linear/test_ctx.py::TestEngine::test_model": "Xfail due to SW-209267",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test[bf16-marian-True-False]":"Xfail due to SW-205776",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test_odd_world_size[fp16-marian-True-False]":"Xfail due to SW-205776",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test[fp16-marian-True-False]":"Xfail due to SW-205776",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test_odd_world_size[bf16-marian-True-False]":"Xfail due to SW-205776",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[3-False-False]":"Xfail due to SW-201549",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[True-False-lp_params]":"Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[False-False-lp_params]":"Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[False-True-lp_params]":"Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[True-True-hp_params]":"Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[False-True-optim_states]":"Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[True-False-hp_params]":"Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[False-True-hp_params]":"Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[False-False-hp_params]":"Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[True-False-contiguous_grad_buffer]":"Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[True-True-contiguous_grad_buffer]":"Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[True-True-optim_states]":"Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[False-False-lp_grads]":"Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[True-True-lp_params]":"Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[False-True-lp_grads]":"Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[False-True-contiguous_grad_buffer]":"Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[True-False-optim_states]":"Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[True-False-lp_grads]":"Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[False-False-optim_states]":"Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[True-True-lp_grads]":"Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[False-False-contiguous_grad_buffer]":"Xfail due to SW-212099",
    "unit/checkpoint/test_convert_checkpoint.py::TestCheckpointConvert::test_convert_zero_checkpoint_to_fp32_state_dict":"Xfail due to SW-212963",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[True-True-None]":"xfail due to SW-212964",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[False-True-None]":"xfail due to SW-212964",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[True-False-None]":"xfail due to SW-212964",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[False-False-None]":"xfail due to SW-212964",
    "unit/linear/test_ctx.py::TestInitTransformers::test_config_init":"Xfail due to SW-215738",
    "unit/linear/test_ctx.py::TestInitTransformers::test_pretrained_init":"Xfail due to SW-215738",
    "unit/ops/fp_quantizer/test_fp_quant.py::test_fp_quant[qbits8-bf16]":"Xfail due to SW-215507",
    "unit/ops/fp_quantizer/test_fp_quant.py::test_fp_quant_meta[bf16]":"Xfail due to SW-215507",

}

g3_lazy_xfail_tests = {
    "unit/accelerator/test_accelerator.py::test_abstract_methods_defined[deepspeed.accelerator.xpu_accelerator]":
    "Xfail due to SW-182749",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[True-True-1-dtype2]":
    "Xfail due to SW-187590",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[True-True-1-dtype1]":
    "Xfail due to SW-187590",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[False-True-1-dtype2]":
    "Xfail due to SW-187590",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[True-True-1-dtype2]":
    "Xfail due to SW-187590",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[True-True-1-dtype0]":
    "Xfail due to SW-187590",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[False-True-1-dtype0]":
    "Xfail due to SW-187590",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[False-True-1-dtype0]":
    "Xfail due to SW-187590",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[False-True-1-dtype0]":
    "Xfail due to SW-187590",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[True-True-1-dtype0]":
    "Xfail due to SW-187590",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[False-True-1-dtype1]":
    "Xfail due to SW-187590",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[True-True-1-dtype2]":
    "Xfail due to SW-187590",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[True-True-1-dtype0]":
    "Xfail due to SW-187590",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[True-True-1-dtype1]":
    "Xfail due to SW-187590",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[False-True-1-dtype2]":
    "Xfail due to SW-187590",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[True-True-1-dtype1]":
    "Xfail due to SW-187590",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[False-True-1-dtype2]":
    "Xfail due to SW-187590",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[False-True-1-dtype1]":
    "Xfail due to SW-187590",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[False-True-1-dtype1]":
    "Xfail due to SW-187590",
    "unit/compression/test_dequantization.py::TestDequantization::test_dequantize":
    "Xfail due to SW-168442",
    "unit/hybrid_engine/test_he_llama.py::TestHybridEngineLlama::test_functionality[huggyllama/llama-7b-bsz=2]":
    "xfail due to SW-185015",
    "unit/hybrid_engine/test_he_llama.py::TestHybridEngineLlama::test_functionality[huggyllama/llama-7b-bsz=1]":
    "xfail due to SW-185015",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_quantized_linear[8bits-0]":
    "Xfail, due to SW-168583",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant_nvme_offload":
    "Xfail, due to SW-168583",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_quantized_linear[4bits-1]":
    "Xfail, due to SW-168583",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_quantized_linear[4bits-0]":
    "Xfail, due to SW-168583",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant[8bits]":
    "Xfail, due to SW-168583",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant_cpu_offload[4bits]":
    "Xfail, due to SW-168583",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization[4bits]":
    "Xfail, due to SW-168583",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization_cpu_offload[4bits]":
    "Xfail, due to SW-168583",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization_nvme_offload":
    "Xfail, due to SW-168583",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant_cpu_offload[8bits]":
    "Xfail, due to SW-168583",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant[4bits]":
    "Xfail, due to SW-168583",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization_cpu_offload[8bits]":
    "Xfail, due to SW-168583",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization[8bits]":
    "Xfail, due to SW-168583",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_quantized_linear[8bits-1]":
    "Xfail, due to SW-168583",
    "unit/inference/test_model_profiling.py::TestModelProfiling::test[True-True]":
    "Xfail, due to SW-163097",
    "unit/inference/test_model_profiling.py::TestModelProfiling::test[True-False]":
    "Xfail, due to SW-163097",
    "unit/inference/test_model_profiling.py::TestModelProfiling::test[False-True]":
    "Xfail, due to SW-163097",
    "unit/inference/test_model_profiling.py::TestModelProfiling::test[False-False]":
    "Xfail, due to SW-163097",
    "unit/inference/test_stable_diffusion.py::TestStableDiffusion::test":
    "Xfail, due to SW-170181.",
    "unit/launcher/test_user_args.py::test_user_args[True-I'm going to tell them \"DeepSpeed is the best\"]":
    "Xfail due to SW-182753",
    "unit/launcher/test_user_args.py::test_user_args[True-'\"translate English to Romanian: \"']":
    "Xfail due to SW-182753",
    "unit/launcher/test_user_args.py::test_user_args[True-'I am 72\" tall']":
    "Xfail due to SW-182753",
    "unit/launcher/test_user_args.py::test_user_args[True-\"I am 6' tall\"]":
    "Xfail due to SW-182753",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-160-128-2-3-False-True]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-512-16-3-False-False]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-1024-56-16-3-False-False]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-2048-128-32-3-False-False]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-160-128-2-24-False-True]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-511-16-3-False-True]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-384-16-3-False-True]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-509-16-3-True-False]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-119-16-3-True-False]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[3-1024-51-16-3-True-False]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-384-16-3-True-True0]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-256-52-4-3-True-True]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1536-128-24-3-False-True]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-2560-128-40-3-False-True]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1600-128-2-3-True-True]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-4096-128-64-3-True-True]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-1024-24-16-3-False-False]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1600-128-25-3-True-True]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1600-128-25-3-False-True]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-381-16-3-True-False]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[3-1024-54-16-3-True-True]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-2048-128-32-3-False-True]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-160-128-2-3-True-True]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-384-16-3-True-True1]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-1024-53-16-3-False-True]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-120-16-3-True-True]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-128-128-2-3-True-False]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-512-16-3-True-True]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-384-16-3-False-False]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-2560-128-40-3-False-False]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-8192-128-64-3-False-True]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[1-256-2048-32-3-True-True]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1536-128-24-3-False-False]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-128-128-2-3-True-True]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-1024-21-16-3-False-True]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForwardSmallBatchSize::test_forward_with_small_bsz[8-7-1024-512-16-3-True-True]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForwardSmallBatchSize::test_forward_with_small_bsz[8-7-1024-512-16-3-False-True]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForwardSmallBatchSize::test_forward_with_small_bsz[8-3-1024-512-16-3-True-False]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForwardSmallBatchSize::test_forward_with_small_bsz[8-3-1024-512-16-3-False-False]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[64-1600-128-2-4-False-True-0.2]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[8-1600-128-2-3-True-True-0.05]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[64-160-128-2-24-False-True-0.2]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[8-1600-128-25-3-True-True-0.05]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[8-160-128-2-3-True-True-0.1]":
    "skipping due to TransformerBuilder is not supported by HPU, SW-176906",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[64-fp16]":
    "Xfail, due to SW-182502",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[128-fp16]":
    "Xfail, due to SW-182502",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[22-fp16]":
    "Xfail, due to SW-182502",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1048576-fp16]":
    "Xfail, due to SW-182502",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1024-fp16]":
    "Xfail, due to SW-182502",
    "unit/ops/lion/test_lion.py::TestLionConfigs::test[Lion-False-FusedLion]":
    "Xfail, due to SW-176903",
    "unit/ops/lion/test_lion.py::TestLionConfigs::test[Lion-True-DeepSpeedCPULion]":
    "Xfail, due to SW-176903",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_bias_geglu[dtype1-512-1-1]":
    "Xfail flaky",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_gated_silu[dtype0-512-1-1]":
    "Xfail flaky",
    "unit/runtime/zero/test_zero.py::TestParamPartitioningSkipInit::test":
    "Xfail due to SW-181939",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[1-9-1024]":
    "Xfail, due to SW-164239",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[4-9-1024]":
    "Xfail, due to SW-164239",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[2-9-1024]":
    "Xfail, due to SW-164239",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConvergence::test[gpt2]":
    "XFail for now",
    "unit/runtime/zero/test_zero_context.py::TestSerialContext::test_subclass_param":
    "Xfail, due to SW-156783",
    "unit/runtime/zero/test_zero_context_ancestry.py::TestSerialParamInit::test_subclass_param_init":
    "Xfail, due to SW-143227.",
    "unit/runtime/zero/test_zero_nesting_init.py::TestNestedParallelInit::test_nested_parallel_init":
    "Xfail download issue",
    "unit/runtime/comm/test_coalesced_collectives.py::TestAllToAllQuantReduceFallback::test_non_divisible":
    "Xfail due to SW-182766",
    "unit/runtime/comm/test_coalesced_collectives.py::TestAllToAllQuantReduceFallback::test_1d_tensor":
    "Xfail due to SW-182766",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[True-MuAdam-Adam]":
    "Xfail, due to SW-164551",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[False-MuAdam-Adam]":
    "Xfail, due to SW-164551",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[False-MuSGD-SGD]":
    "Xfail, due to SW-164551",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[False-MuAdamW-AdamW]":
    "Xfail, due to SW-164551",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[True-MuSGD-SGD]":
    "Xfail, due to SW-164551",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[True-MuAdamW-AdamW]":
    "Xfail, due to SW-164551",
    "unit/inference/test_inference.py::TestMPSize::test[fp16-bloom]":
    "Xfail due to RuntimeError: Incompatible input shapes, broadcast not possible. Tensor1 Size: 5 5 16 1 Tensor2 Size: 5 1 8During handling of the above exception, another exception occurred",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_human_eval.py::test_human_eval[codellama/CodeLlama-7b-Python-hf]":
    "Xfail due to SW-182759",
    "unit/utils/test_init_on_device.py::TestOnDevice::test_on_device[hpu]":
    "Xfail, due to SW-178730.",
    "unit/inference/test_inference.py::TestMPSize::test[fp16-bloom-False]":
    "Xfail due to SW-188513",
    "unit/runtime/pipe/test_pipe.py::TestPipeCifar10::test_pipe_use_reentrant[topo_config1]":
    "xfail due to SW-194902",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_half_int8_quantization":
    "Xfail due to SW-182766",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_half_int4_quantization":
    "Xfail due to SW-182766",
    "unit/runtime/zero/test_zero.py::TestZeroToFP32::test_1_param_group[False-3]":
    "Xfail due to sw-201549",
    "unit/runtime/zero/test_zero.py::TestZeroToFP32::test_2_param_groups[True-3]":
    "Xfail due to sw-201549",
    "unit/runtime/zero/test_zero.py::TestZeroToFP32::test_1_param_group[True-2]":
    "Xfail due to sw-201549",
    "unit/runtime/zero/test_zero.py::TestZeroToFP32::test_2_param_groups[False-3]":
    "Xfail due to sw-201549",
    "unit/runtime/zero/test_zero.py::TestZeroToFP32::test_2_param_groups[True-2]":
    "Xfail due to sw-201549",
    "unit/runtime/zero/test_zero.py::TestZeroToFP32::test_1_param_group[True-3]":
    "Xfail due to sw-201549",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[3-False-Adam-False]":
    "Xfail due to sw-201549",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[3-True-deepspeed_adam-False]":
    "Xfail due to sw-201549",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_module_only[3-False]":
    "Xfail due to sw-201549",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_pipeline_checkpoint_loading[3-False]":
    "Xfail due to sw-201549",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_module_only[3-False]":
    "Xfail due to sw-201549",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_not_load_optimizer_state[3-False]":
    "Xfail due to sw-201549",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_immediate_save_load[3-False]":
    "Xfail due to sw-201549",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_load_immediate_save[3-False]":
    "Xfail due to sw-201549",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[3-True-False]":
    "Xfail due to sw-201549",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[3-False-False]":
    "Xfail due to sw-201549",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[3-True-False]":
    "Xfail due to sw-201549",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[3-False-False":
    "Xfail due to sw-201549",
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[16-fp16]":
    "Xfail due to SW-200127",
    "unit/runtime/pipe/test_pipe.py::TestPipeCifar10::test_pipe_use_reentrant[topo_config2]":
    "Xfail due to SW-203893",
    "unit/linear/test_linear.py::TestQuantLinear::test[6]":
    "AttributeError: 'Parameter' object has no attribute 'dequantized'",
    "unit/linear/test_linear.py::TestQuantLinear::test[8]":
    "AttributeError: 'Parameter' object has no attribute 'dequantized'",
    "unit/linear/test_linear.py::TestOptimizedLinear::test[qbit8-bws1]":
    "AttributeError: 'Parameter' object has no attribute 'dequantized'",
    "unit/linear/test_linear.py::TestOptimizedLinear::test[qbit6-bws1]":
    "AttributeError: 'Parameter' object has no attribute 'dequantized'",
    "unit/linear/test_quant_param.py::TestQuantParam::test_hf_clone":
    "AssertionError: Quantize fallback only supports quantization to FP8",
    "unit/linear/test_ctx.py::TestEngine::test_model":
    "Xfail due to SW-209267",
    "unit/linear/test_ctx.py::TestInitTransformers::test_config_init":
    "Xfail due to SW-215738",
    "unit/linear/test_ctx.py::TestInitTransformers::test_pretrained_init":
    "Xfail due to SW-215738",
}

hpu_eager_xfail_tests = {}

g1_eager_xfail_tests = {
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_stable_diffusion.py::TestStableDiffusion::test":
    "Xfail, due to SW-170181.",
    "unit/runtime/test_autocast.py::TestAutoCastDisable::test_missing_amp_autocast[True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/comm/test_coalesced_collectives.py::TestReduceScatterCoalescedTensorSmallerThanWorldSize::test":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/comm/test_coalesced_collectives.py::TestReduceScatterCoalesced::test_two_inputs":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/comm/test_coalesced_collectives.py::TestReduceScatterCoalesced::test_single_input":
    "float16/half is not supported on Gaudi.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[64-fp16]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1024-fp16]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[22-fp16]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1048576-fp16]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[128-fp16]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_ds_initialize.py::TestNoOptim::test[3]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_ds_initialize.py::TestOptimizerImplementation::test[fp16-fp32-zero3]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_ds_initialize.py::TestOptimizerImplementation::test[fp16-bf16-zero3]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[8-fp16]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[16-fp16]":
    "float16/half is not supported on Gaudi.",
    "unit/utils/test_init_on_device.py::TestOnDevice::test_on_device[hpu]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization_cpu_offload[4bits]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant[4bits]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_quantized_linear[4bits-1]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_half_int8_quantization":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_model_quantization[8bits]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization[8bits]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_model_quantization[4bits]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_half_int4_quantization":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant_cpu_offload[8bits]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant_nvme_offload":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_quantized_linear[8bits-1]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant[8bits]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization_nvme_offload":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant_cpu_offload[4bits]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization_cpu_offload[8bits]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_quantized_linear[4bits-0]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization[4bits]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_quantized_linear[8bits-0]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[3-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[3-True-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[3-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[3-True-False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroFrozenWeights::test[3]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZero3DictFwd::test[dict]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZero3DictFwd::test[tuple]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZero3DictFwd::test[list]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZero3InitForParentWeightInitialization::test":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningLargeParam::test[False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningLargeParam::test[True-True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningManyParams::test[True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroPartitionCache::test_training_partition_cache[False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroPartitionCache::test_training_partition_cache[True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_context.py::TestScatterGather::test":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_context.py::TestGatherUpdate::test":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_context.py::TestSerialContext::test_scatter_halftype":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_context.py::TestSerialContext::test_subclass_param":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_context_ancestry.py::TestDSInitWZinit::test":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_context_ancestry.py::TestSerialParamInit::test_subclass_param_init":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_module_only[3-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_optimizer_state[3-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_not_load_optimizer_state[3-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestSaveTensorClone::test_save_tensor_clone[False-2-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestSaveTensorClone::test_save_tensor_clone[True-2-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestSaveTensorClone::test_save_tensor_clone[False-1-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestSaveTensorClone::test_save_tensor_clone[True-1-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[3-True-deepspeed_adam-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_pipeline_checkpoint_loading[3-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[3-False-Adam-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[3-False-Adam-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_module_only[3-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[3-True-deepspeed_adam-False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[cpu-3-full-True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[none-3-local-False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[none-3-local-True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[none-3-full-False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[cpu-3-local-True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[none-3-full-True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[cpu-3-local-False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[cpu-3-full-False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-3-local-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-3-full-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[none-3-local-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[none-3-full-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/half_precision/test_bf16.py::TestZeroDtypeCocktail::test[default-fp16]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_data_efficiency.py::TestDataEfficiency::test_curriculum_learning":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_data_efficiency.py::TestLegacyCurriculumScheduler::test_fixed_linear":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_data_efficiency.py::TestLegacyCurriculumScheduler::test_fixed_discrete":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_ds_config_dict.py::TestDeprecatedDeepScaleConfig::test":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_ds_config_dict.py::TestDistInit::test":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_ds_config_dict.py::TestConfigLoad::test_hjson":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_ds_config_dict.py::TestConfigLoad::test_json":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_ds_config_dict.py::TestConfigLoad::test_dict":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_ds_config_dict.py::TestArgs::test_no_args":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_ds_config_dict.py::TestArgs::test_none_args":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_ds_config_dict.py::TestInitNoOptimizer::test":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_ds_initialize.py::TestNoOptim::test[0]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_ignore_unused_parameters.py::TestStage2IgnoreUnusedParameters::test[False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_ignore_unused_parameters.py::TestStage2IgnoreUnusedParameters::test[True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[0-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[2-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[1-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[0-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[2-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[2-True-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[1-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[2-True-False]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe.py::TestMoE::test[False-0-4]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe.py::TestMoE::test[True-0-4]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe.py::TestMoE::test[False-0-2]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe.py::TestMoE::test[False-1-4]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe.py::TestMoE::test[False-1-2]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe.py::TestMoE::test[True-2-2]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe.py::TestMoE::test[True-1-4]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe.py::TestMoE::test[True-1-2]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe.py::TestMoE::test[True-0-2]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe.py::TestMoE::test[False-2-2]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe.py::TestMoE::test[False-2-4]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe.py::TestMoE::test[True-2-4]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe.py::TestPRMoE::test[2-False]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe.py::TestPRMoE::test[2-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[4-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[4-True-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[2-True-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[2-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe[4]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[True-False-1-4]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[False-False-1-2]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[False-False-2-2]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[True-False-1-2]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[True-True-2-2]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[False-True-1-4]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[False-True-1-2]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[False-False-1-4]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[False-True-2-2]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[True-True-1-2]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[True-True-1-4]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[True-False-2-2]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[True-MuAdamW-AdamW]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[False-MuSGD-SGD]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[True-MuSGD-SGD]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[False-MuAdamW-AdamW]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[False-MuAdam-Adam]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[True-MuAdam-Adam]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_other_optimizer.py::TestOtherOptimizerCheckpoint::test_checkpoint_fused_optimizer[False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_pipeline.py::TestPipelineCheckpoint::test_checkpoint_pipe_engine[1-False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_pld.py::TestNonPLDModel::test_non_pld_model":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_pld.py::TestPLDModel::test_pld_model[0.1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_pld.py::TestPLDModel::test_pld_model[0.9]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_pld.py::TestPLDModel::test_pld_model[1.0]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_pld.py::TestPLDModel::test_pld_model[0]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestPartitionNcclAlignment::test":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroOffloadOptim::test[True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroOffloadOptim::test[False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestEmptyParameterGroup::test_empty_param_groups[dtype1-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestEmptyParameterGroup::test_empty_param_groups[dtype1-True-False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestEmptyParameterGroup::test_empty_param_groups[dtype1-True-True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestEmptyParameterGroup::test_empty_param_groups[dtype1-False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningBase::test_fp16_enabled[True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroFrozenWeights::test[2]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroFrozenWeights::test[1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroAdamOptimizerStepCount::test[3]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroAdamOptimizerStepCount::test[2]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroAdamOptimizerStepCount::test[1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZero3RepeatForwardLoop::test":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestIncorectAllgatherBucketSize::test[1000]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestIncorectAllgatherBucketSize::test[1001]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroToFP32::test_2_param_groups[True-2]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroToFP32::test_1_param_group[True-2]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroToFP32::test_1_param_group[False-3]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroToFP32::test_2_param_groups[False-2]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroToFP32::test_1_param_group[False-2]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroToFP32::test_1_param_group[True-3]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroToFP32::test_2_param_groups[False-3]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroToFP32::test_2_param_groups[True-3]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningLargeParam::test[False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningLargeParam::test[True-False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningManyParams::test[False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroOffloadStage1::test":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroUnbalancedGradients::test[1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroUnbalancedGradients::test[2]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZeroUnbalancedGradients::test[3]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_context.py::TestSerialContext::test_ext_param_getattr":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_context_return.py::TestReturnParam::test_stage_3_output_type[tensor]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_context_return.py::TestReturnParam::test_stage_3_output_type[None]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_context_return.py::TestReturnParam::test_stage_3_output_type[dict]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_context_return.py::TestReturnParam::test_ext_param_return":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_offloadpp.py::TestZeroPartialOffloadConfigSweep::test[4-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_offloadpp.py::TestZeroPartialOffloadConfigSweep::test[8-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_save_exclude_custom_frozen_weights[2-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_optimizer_state[2-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_save_exclude_custom_frozen_weights[1-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_not_load_optimizer_state[1-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_not_load_optimizer_state[2-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_save_exclude_frozen_weights[1-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_save_exclude_frozen_weights[2-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_module_only[2-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_module_only[1-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_optimizer_state[1-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_load_immediate_save[2-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_save_before_accum_grad_is_done[3-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_immediate_save_load[3-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_immediate_save_load[0-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_save_before_accum_grad_is_done[1-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_immediate_save_load[2-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_load_immediate_save[3-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_save_before_accum_grad_is_done[0-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_save_before_accum_grad_is_done[2-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_immediate_save_load[1-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_load_immediate_save[0-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_load_immediate_save[1-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_hybrid_optimizer_state[2-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_module_only[2-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[2-False-Adam-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_module_only[1-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[2-False-Adam-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[2-True-deepspeed_adam-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_hybrid_optimizer_state[1-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_module_only[0-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[2-True-deepspeed_adam-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[1-False-Adam-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[1-False-Adam-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[True-False-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[True-True-True-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[False-True-True-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[True-False-True-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[False-False-True-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[False-True-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[False-False-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[True-True-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[cpu-1-full-True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[cpu-2-full-False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[none-2-full-False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[cpu-2-full-True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[cpu-1-full-False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[none-1-full-False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[none-2-full-True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_zero_fragments[none-1-full-True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[none-1-full-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[none-2-full-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-1-full-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-2-full-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[False-True-True-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[True-True-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[True-False-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[True-False-True-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[True-True-True-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[False-False-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[False-False-True-False]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[False-True-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/compression/test_dequantization.py::TestDequantization::test_dequantize":
    "Xfail, due to SW-168442.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[3-False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[3-True-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[3-False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[3-True-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[3-False-Adam-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[3-True-deepspeed_adam-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_module_only[3-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[3-True-deepspeed_adam-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[3-False-Adam-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_pipeline_checkpoint_loading[3-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestSaveTensorClone::test_save_tensor_clone[True-1-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestSaveTensorClone::test_save_tensor_clone[False-1-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestSaveTensorClone::test_save_tensor_clone[True-2-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestSaveTensorClone::test_save_tensor_clone[False-2-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_not_load_optimizer_state[3-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_optimizer_state[3-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_module_only[3-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_pipeline.py::TestPipelineCheckpoint::test_checkpoint_pipe_engine[1-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[0-False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[1-False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[1-False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[2-True-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[2-False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[2-False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[2-True-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[0-False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/compile/test_load_config.py::TestConfigLoad::test_set_compile_kwargs":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/compile/test_load_config.py::TestConfigLoad::test_compile_disabled":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/compile/test_load_config.py::TestConfigLoad::test_set_compiler_fn":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/compile/test_load_config.py::TestConfigLoad::test_compile_kwargs":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/compile/test_load_config.py::TestConfigLoad::test_compile":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/compile/test_load_config.py::TestConfigLoad::test_custom_backend":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_other_optimizer.py::TestOtherOptimizerCheckpoint::test_checkpoint_fused_optimizer[True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/compile/test_compile_wrapper.py::TestCustomMethod::test_custom_function":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[4-False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[2-False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[4-True-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[2-True-True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-1-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-2-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-3-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-3-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-1-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-2-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[nvme-3-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[1-False-Adam-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_module_only[1-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_module_only[0-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[2-True-deepspeed_adam-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[2-False-Adam-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_hybrid_optimizer_state[1-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[2-False-Adam-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[1-False-Adam-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_hybrid_optimizer_state[2-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[2-True-deepspeed_adam-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_module_only[2-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[False-False-False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[False-True-False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[True-False-True-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[True-True-False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[True-False-False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[False-True-True-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[False-False-True-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[True-True-True-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_not_load_optimizer_state[1-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_save_exclude_frozen_weights[1-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_save_exclude_frozen_weights[2-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_optimizer_state[2-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_not_load_optimizer_state[2-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_module_only[2-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_module_only[1-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_save_exclude_custom_frozen_weights[1-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_save_exclude_custom_frozen_weights[2-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_optimizer_state[1-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_immediate_save_load[0-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_immediate_save_load[2-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_load_immediate_save[2-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_load_immediate_save[3-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_load_immediate_save[1-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_immediate_save_load[1-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_save_before_accum_grad_is_done[1-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_save_before_accum_grad_is_done[2-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_save_before_accum_grad_is_done[3-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_save_before_accum_grad_is_done[0-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_immediate_save_load[3-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_load_immediate_save[0-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[False-True-False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[True-False-True-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[True-True-False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[True-False-False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[True-True-True-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[False-False-False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[False-False-True-True]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_change_dp[False-True-True-True]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[EleutherAI/gpt-j-6B-False]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[EleutherAI/gpt-neo-125M-False]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[bigscience/bloom-560m-False]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[facebook/opt-125m-False]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[facebook/opt-350m-False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[2-4-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[4-4-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[4-9-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[1-4-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[1-9-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[2-9-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-1232-128-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-1232-1-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-4096-128-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-1232-1-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-1232-1-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-512-128-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-1232-128-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-4096-255-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-1232-128-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-512-128-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-4096-255-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-512-1-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-1232-255-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-1232-255-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-4096-1-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-4096-1-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-512-1-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-512-255-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-512-128-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-512-255-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-4096-255-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-4096-128-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-512-128-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-512-255-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-4096-128-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-4096-1-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-1232-1-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-512-1-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-1232-255-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-512-255-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-512-1-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-4096-128-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-4096-1-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-4096-255-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-1232-128-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-1232-255-2]":
    "float16/half is not supported on Gaudi.",
    "unit/hybrid_engine/test_he_all.py::TestHybridEngineTextGen::test_functionality[EleutherAI/gpt-neo-1.3B-bsz=2]":
    "float16/half is not supported on Gaudi.",
    "unit/hybrid_engine/test_he_all.py::TestHybridEngineTextGen::test_functionality[facebook/opt-1.3b-bsz=1]":
    "float16/half is not supported on Gaudi.",
    "unit/hybrid_engine/test_he_all.py::TestHybridEngineTextGen::test_functionality[facebook/opt-1.3b-bsz=2]":
    "float16/half is not supported on Gaudi.",
    "unit/hybrid_engine/test_he_all.py::TestHybridEngineTextGen::test_functionality[EleutherAI/gpt-neo-1.3B-bsz=1]":
    "float16/half is not supported on Gaudi.",
    "unit/hybrid_engine/test_he_llama.py::TestHybridEngineLlama::test_functionality[huggyllama/llama-7b-bsz=2]":
    "float16/half is not supported on Gaudi.",
    "unit/hybrid_engine/test_he_llama.py::TestHybridEngineLlama::test_functionality[huggyllama/llama-7b-bsz=1]":
    "float16/half is not supported on Gaudi.",
    "unit/hybrid_engine/test_he_lora.py::TestHybridEngineLoRA::test_lora[none-bigscience/bloom-560m-zero_stage=2-bsz=1]":
    "float16/half is not supported on Gaudi.",
    "unit/hybrid_engine/test_he_lora.py::TestHybridEngineLoRA::test_lora[cpu-bigscience/bloom-560m-zero_stage=3-bsz=1]":
    "float16/half is not supported on Gaudi.",
    "unit/hybrid_engine/test_he_lora.py::TestHybridEngineLoRA::test_lora[cpu-facebook/opt-350m-zero_stage=3-bsz=1]":
    "float16/half is not supported on Gaudi.",
    "unit/hybrid_engine/test_he_lora.py::TestHybridEngineLoRA::test_lora[none-facebook/opt-350m-zero_stage=2-bsz=1]":
    "float16/half is not supported on Gaudi.",
    "unit/hybrid_engine/test_he_lora.py::TestHybridEngineLoRA::test_lora[cpu-EleutherAI/gpt-neo-125m-zero_stage=3-bsz=1]":
    "float16/half is not supported on Gaudi.",
    "unit/hybrid_engine/test_he_lora.py::TestHybridEngineLoRA::test_lora[cpu-facebook/opt-350m-zero_stage=2-bsz=1]":
    "float16/half is not supported on Gaudi.",
    "unit/hybrid_engine/test_he_lora.py::TestHybridEngineLoRA::test_lora[none-EleutherAI/gpt-neo-125m-zero_stage=3-bsz=1]":
    "float16/half is not supported on Gaudi.",
    "unit/hybrid_engine/test_he_lora.py::TestHybridEngineLoRA::test_lora[cpu-EleutherAI/gpt-neo-125m-zero_stage=2-bsz=1]":
    "float16/half is not supported on Gaudi.",
    "unit/hybrid_engine/test_he_lora.py::TestHybridEngineLoRA::test_lora[cpu-bigscience/bloom-560m-zero_stage=2-bsz=1]":
    "float16/half is not supported on Gaudi.",
    "unit/hybrid_engine/test_he_lora.py::TestHybridEngineLoRA::test_lora[none-bigscience/bloom-560m-zero_stage=3-bsz=1]":
    "float16/half is not supported on Gaudi.",
    "unit/hybrid_engine/test_he_lora.py::TestHybridEngineLoRA::test_lora[none-facebook/opt-350m-zero_stage=3-bsz=1]":
    "float16/half is not supported on Gaudi.",
    "unit/hybrid_engine/test_he_lora.py::TestHybridEngineLoRA::test_lora[none-EleutherAI/gpt-neo-125m-zero_stage=2-bsz=1]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/test_inference.py::TestMPSize::test[bf16-gpt-neo-False]":
    "Xfail, due to SW-175376.",
    "unit/inference/test_inference.py::TestMPSize::test[fp32-gpt-neo-False]":
    "Xfail, due to SW-175376.",
    "unit/launcher/test_user_args.py::test_user_args[True-I'm going to tell them \"DeepSpeed is the best\"]":
    "Xfail due to SW-182753",
    "unit/launcher/test_user_args.py::test_user_args[True-'\"translate English to Romanian: \"']":
    "Xfail due to SW-182753",
    "unit/launcher/test_user_args.py::test_user_args[True-'I am 72\" tall']":
    "Xfail due to SW-182753",
    "unit/launcher/test_user_args.py::test_user_args[True-\"I am 6' tall\"]":
    "Xfail due to SW-182753",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test_gradient_accumulation[1-9-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test_gradient_accumulation[4-9-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test_gradient_accumulation[2-9-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test_eval[1-9-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test_eval[2-9-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test_eval[4-9-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/comm/test_coalesced_collectives.py::TestAllToAllQuantReduceFallback::test_1d_tensor":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/comm/test_coalesced_collectives.py::TestAllToAllQuantReduceFallback::test_non_divisible":
    "float16/half is not supported on Gaudi.",
    "unit/utils/test_init_on_device.py::TestOnDevice::test_on_device[hpu:0]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestParamPartitioningSkipInit::test":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZero3RepeatForwardLoop::test[True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestZero3RepeatForwardLoop::test[False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_leaf_module.py::TestSetZ3LeafModule::test_choose_module_by_counter":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_leaf_module.py::TestSetZ3LeafModule::test_choose_module_by_rank":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_leaf_module.py::TestSetZ3LeafModule::test_no_grad_input_error":
    "float16/half is not supported on Gaudi.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert/distilgpt2-text-generation-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-182671",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert/distilgpt2-text-generation-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-182748",
    "unit/accelerator/test_accelerator.py::test_abstract_methods_defined[deepspeed.accelerator.xpu_accelerator]":
    "Xfail due to SW-182749",
    "unit/inference/test_inference.py::TestInjectionPolicy::test[fp32-t5-False]":
    "Xfail, due to SW-182668",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp32-noCG-noTriton-False-False]":
    "Xfail due to SW-182671",
    "unit/inference/test_inference.py::TestModelTask::test[openai-community/gpt2-text-generation-fp32-noCG-noTriton-False-False]":
    "Xfail due to SW-182671",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-bf16-noCG-noTriton-False-False]":
    "Xfail due to SW-182671",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-125m-text-generation-bf16-noCG-noTriton-False-False]":
    "Xfail due to SW-182671",
    "unit/inference/test_inference.py::TestModelTask::test[openai-community/gpt2-text-generation-bf16-noCG-noTriton-False-False]":
    "Xfail due to SW-182671",
    "unit/inference/test_inference.py::TestModelTask::test[Norod78/hebrew-bad_wiki-gpt_neo-tiny-text-generation-bf16-noCG-noTriton-False-False]":
    "Xfail due to SW-182671",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-125m-text-generation-fp32-noCG-noTriton-False-False]":
    "Xfail due to SW-182671",
    "unit/inference/test_inference.py::TestModelTask::test[Norod78/hebrew-bad_wiki-gpt_neo-tiny-text-generation-fp32-noCG-noTriton-False-False]":
    "Xfail due to SW-182671",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-125m-text-generation-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-182671",
    "unit/inference/test_inference.py::TestModelTask::test[openai-community/gpt2-text-generation-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-182671",
    "unit/inference/test_inference.py::TestModelTask::test[Norod78/hebrew-bad_wiki-gpt_neo-tiny-text-generation-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-182671",
    "unit/inference/test_inference.py::TestModelTask::test[Norod78/hebrew-bad_wiki-gpt_neo-tiny-text-generation-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-182671",
    "unit/inference/test_inference.py::TestModelTask::test[openai-community/gpt2-text-generation-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-182671",
    "unit/runtime/pipe/test_pipe.py::TestPipeCifar10::test_pipe_use_reentrant[topo_config2]":
    "Xfail due to SW-182509",
    "unit/runtime/pipe/test_pipe.py::TestPipeCifar10::test_pipe_use_reentrant[topo_config1]":
    "Xfail due to SW-182509",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-3-dtype2]":
    "Xfail due to SW-181951",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-3-dtype0]":
    "Xfail due to SW-181951",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[nvme-3-dtype2]":
    "Xfail due to OP not implemented on HPU",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[nvme-3-dtype0]":
    "Xfail due to OP not implemented on HPU",
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-openai-community/gpt2-xl-False]":
    "xfail due to model download",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-bf16-CG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-bf16-noCG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-bf16-noCG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-bf16-noCG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-bf16-CG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-bf16-CG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-bf16-CG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-bf16-noCG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-bf16-noCG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-bf16-CG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-bf16-noCG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-bf16-noCG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-bf16-CG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-bf16-CG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert/distilgpt2-text-generation-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-125m-text-generation-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[Norod78/hebrew-bad_wiki-gpt_neo-tiny-text-generation-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[openai-community/gpt2-text-generation-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp16-CG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp16-noCG-noTriton-False-False]":
    "Xfail due to FP16 not supported to gaudi1",
    "unit/inference/test_inference.py::TestMPSize::test[fp16-gpt-neo]":
    "Xfail due to FP16 not supported on gaudi",
    "unit/inference/test_inference.py::TestMPSize::test[fp16-bloom]":
    "Xfail due to FP16 not supported on gaudi",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[False-False-False-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[False-False-False-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[False-True-False-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[False-True-True-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[False-True-False-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[False-False-True-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[False-False-False-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[False-True-True-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[False-True-False-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[False-True-True-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[False-False-True-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[False-False-True-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/inference/test_inference.py::TestInjectionPolicy::test[ws2-fp32-t5-False]":
    "Xfail, due to SW-.",
    "unit/inference/test_inference.py::TestInjectionPolicy::test[ws1-fp32-t5-False]":
    "Xfail, due to SW-.",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[True-False-True-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[True-True-False-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[True-True-False-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[True-False-False-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[True-True-False-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[True-False-False-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[True-False-True-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[True-True-True-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[True-True-True-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[True-True-True-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[True-False-True-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[True-False-False-1-dtype1]":
    "Xfail due to fp16 not supported",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-125m-text-generation-fp16-noCG-noTriton-False-True]":
    "Xfail due to SW-189257",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp32-noCG-noTriton-False-True]":
    "Xfail due to SW-189257",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp16-noCG-noTriton-False-True]":
    "Xfail due to SW-189257",
    "unit/inference/test_inference.py::TestMPSize::test[fp16-bloom-True]":
    "Fp16 not supported",
    "unit/inference/test_inference.py::TestMPSize::test[fp16-bloom-False]":
    "FP16 not supported",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[facebook/opt-125m-True]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[EleutherAI/gpt-neo-125M-True]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[EleutherAI/gpt-j-6B-True]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[bigscience/bloom-560m-True]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[facebook/opt-350m-True]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/test_inference.py::TestMPSize::test[fp16-gpt-neo-True]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/test_inference.py::TestMPSize::test[fp16-gpt-neo-False]":
    "Xfail due to FP16 not supported",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert/distilgpt2-text-generation-fp32-noCG-noTriton-False-False]":
    "Xfail due to sw-182671",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert/distilgpt2-text-generation-fp32-noCG-noTriton-False-True]":
    "Xfail due to SW-196571",
    "unit/inference/test_inference.py::TestModelTask::test[openai-community/gpt2-text-generation-fp32-noCG-noTriton-False-True]":
    "Xfail due to SW-196571",
    "unit/inference/test_inference.py::TestInjectionPolicy::test[ws2-fp32-roberta-True]":
    "Xfail due to sw-193404",
    "unit/inference/test_inference.py::TestInjectionPolicy::test[ws2-fp32-t5-True]":
    "Xfail due to sw-193404",
    "unit/inference/test_inference.py::TestInjectionPolicy::test[ws1-fp32-t5-True]":
    "xfail due to sw-187946",
    "unit/moe/test_moe.py::TestSimpleMoE::test[2]":
    "Xfail due to fp16 not supported",
    "unit/moe/test_moe.py::TestSimpleMoE::test[1]":
    "Xfail due to fp16 not supported",
    "unit/moe/test_moe.py::TestSimpleMoE::test[0]":
    "Xfail due to fp16 not supported",
    "unit/inference/test_inference.py::TestModelTask::test[Norod78/hebrew-bad_wiki-gpt_neo-tiny-text-generation-fp32-noCG-noTriton-False-True]":
    "Xfail due to SW-195011",
    "unit/runtime/test_multi_output_model.py::TestThreeOutputModel::test":
    "xfail due to 198794",
    "unit/runtime/test_multi_output_model.py::TestTwoOutputModel::test":
    "xfail due to 198794",
    "unit/checkpoint/test_pipeline.py::TestPipelineCheckpoint::test_checkpoint_pipe_engine[0-True]":
    "xfail due to SW-199012",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-125m-text-generation-fp32-noCG-noTriton-False-True]":
    "xfail due to SW-189257",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-125m-text-generation-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-182671",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentGet::test_bf16_fragments[False]":
    "Xfail due to SW-201247",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test_odd_world_size[fp16-marian-True-False]":
    "Xfail due to fp16 not supported",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test[fp16-marian-True-False]":
    "Xfail due to fp16 not supported",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test[fp16-marian-False-False]":
    "Xfail due to fp16 not supported",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test_odd_world_size[fp16-marian-False-False]":
    "Xfail due to fp16 not supported",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test[fp16-marian-True-True]":
    "Xfail due to fp16 not supported",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test[fp16-marian-False-True]":
    "Xfail due to fp16 not supported",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test_odd_world_size[fp16-marian-True-True]":
    "Xfail due to fp16 not supported",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test_odd_world_size[fp16-marian-False-True]":
    "Xfail due to fp16 not supported",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test[bf16-marian-False-True]":
    "Xfail due to SW-203016",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test_odd_world_size[bf16-marian-True-True]":
    "Xfail due to SW-203016",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test_odd_world_size[bf16-marian-False-True]":
    "Xfail due to SW-203016",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test[bf16-marian-True-True]":
    "Xfail due to SW-203016",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test_odd_world_size[bf16-marian-True-False]":
    "Xfail due to SW-203016",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test[bf16-marian-False-False]":
    "Xfail due to SW-203016",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test[bf16-marian-True-False]":
    "Xfail due to SW-203016",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test_odd_world_size[bf16-marian-False-False]":
    "Xfail due to SW-203016",
}

g2_eager_xfail_tests = {
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-125m-text-generation-fp16-noCG-noTriton-False-True]":
    "Xfail, due to SW-223539.",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp16-noCG-noTriton-False-True]":
    "Xfail,due to SW-223539.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Norod78/hebrew-bad_wiki-gpt_neo-tiny-text-generation-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp32-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp32-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-bf16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-bf16-CG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp16-noCG-noTriton-True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_stable_diffusion.py::TestStableDiffusion::test":
    "Xfail, due to SW-170181.",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[64-160-128-2-24-False-True-0.2]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[64-1600-128-2-4-False-True-0.2]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[8-1600-128-2-3-True-True-0.05]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[8-1600-128-25-3-True-True-0.05]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[8-160-128-2-3-True-True-0.1]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForwardSmallBatchSize::test_forward_with_small_bsz[8-3-1024-512-16-3-False-False]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForwardSmallBatchSize::test_forward_with_small_bsz[8-7-1024-512-16-3-False-True]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForwardSmallBatchSize::test_forward_with_small_bsz[8-7-1024-512-16-3-True-True]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForwardSmallBatchSize::test_forward_with_small_bsz[8-3-1024-512-16-3-True-False]":
    "Xfail, due to SW-176905.",
    "unit/compression/test_dequantization.py::TestDequantization::test_dequantize":
    "Xfail, due to SW-168442.",
    "unit/utils/test_init_on_device.py::TestOnDevice::test_on_device[hpu]":
    "Xfail, due to SW-178730.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant_nvme_offload":
    "Xfail, due to SW-164545.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization_nvme_offload":
    "Xfail, due to SW-164545.",
    "unit/ops/lion/test_lion.py::TestLionConfigs::test[Lion-True-DeepSpeedCPULion]":
    "Xfail, due to SW-176903.",
    "unit/ops/lion/test_lion.py::TestLionConfigs::test[Lion-False-FusedLion]":
    "Xfail, due to SW-176903.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-512-16-3-False-False]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-1024-56-16-3-False-False]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-384-16-3-False-True]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-119-16-3-True-False]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-128-128-2-3-True-True]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-2560-128-40-3-False-True]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1600-128-25-3-False-True]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1600-128-2-3-True-True]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-509-16-3-True-False]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-120-16-3-True-True]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[1-256-2048-32-3-True-True]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-2560-128-40-3-False-False]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1536-128-24-3-False-True]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-128-128-2-3-True-False]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-256-52-4-3-True-True]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-512-16-3-True-True]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-160-128-2-3-False-True]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-511-16-3-False-True]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[3-1024-54-16-3-True-True]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-384-16-3-True-True0]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-384-16-3-True-True1]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1536-128-24-3-False-False]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-1024-53-16-3-False-True]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-381-16-3-True-False]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-160-128-2-24-False-True]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-384-16-3-False-False]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-4096-128-64-3-True-True]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-2048-128-32-3-False-True]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-1024-24-16-3-False-False]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-2048-128-32-3-False-False]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-1024-21-16-3-False-True]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1600-128-25-3-True-True]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-8192-128-64-3-False-True]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-160-128-2-3-True-True]":
    "Xfail, due to SW-176905.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[3-1024-51-16-3-True-False]":
    "Xfail, due to SW-176905.",
    "unit/inference/test_inference.py::TestMPSize::test[fp16-bloom-False]":
    "Xfail, due to SW-196522",
    "unit/inference/test_model_profiling.py::TestModelProfiling::test[False-True]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_model_profiling.py::TestModelProfiling::test[False-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_model_profiling.py::TestModelProfiling::test[True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_model_profiling.py::TestModelProfiling::test[True-True]":
    "Xfail, due to SW-163097.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[1-9-1024]":
    "Xfail, due to SW-164239.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[4-9-1024]":
    "Xfail, due to SW-164239.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[4-4-1024]":
    "Xfail, due to SW-164239.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[2-9-1024]":
    "Xfail, due to SW-164239.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[1-4-1024]":
    "Xfail, due to SW-164239.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[2-4-1024]":
    "Xfail, due to SW-164239.",
    "unit/launcher/test_user_args.py::test_user_args[True-I'm going to tell them \"DeepSpeed is the best\"]":
    "Xfail due to SW-182753",
    "unit/launcher/test_user_args.py::test_user_args[True-'\"translate English to Romanian: \"']":
    "Xfail due to SW-182753",
    "unit/launcher/test_user_args.py::test_user_args[True-'I am 72\" tall']":
    "Xfail due to SW-182753",
    "unit/launcher/test_user_args.py::test_user_args[True-\"I am 6' tall\"]":
    "Xfail due to SW-182753",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert/distilgpt2-text-generation-bf16-noCG-noTriton-False-False]":
    "Xfail due to SW-182748",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-bf16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/runtime/comm/test_coalesced_collectives.py::TestAllToAllQuantReduceFallback::test_1d_tensor":
    "Xfail due to SW-182766",
    "unit/runtime/comm/test_coalesced_collectives.py::TestAllToAllQuantReduceFallback::test_non_divisible":
    "Xfail due to SW-182766",
    "unit/inference/test_inference.py::TestModelTask::test[openai-community/gpt2-text-generation-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-181935",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert/distilgpt2-text-generation-bf16-noCG-noTriton-True-False]":
    "Xfail due to SW-181935",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[22-fp16]":
    "Xfail, due to SW-182502",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1024-fp16]":
    "Xfail, due to SW-182502",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[128-fp16]":
    "Xfail, due to SW-182502",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[64-fp16]":
    "Xfail, due to SW-182502",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1048576-fp16]":
    "Xfail, due to SW-182502",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[nvme-3-dtype2]":
    "Xfail due to op not been implemented on HPU",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[nvme-3-dtype1]":
    "Xfail due to op not been implemented on HPU",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[nvme-3-dtype0]":
    "Xfail due to op not been implemented on HPU",
    "unit/inference/test_inference.py::TestLMCorrectness::test[lambada_standard-gpt2-openai-community/gpt2-xl-False]":
    "xfail due to model download",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-bf16-CG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-bf16-noCG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-bf16-noCG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-bf16-noCG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-bf16-CG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-bf16-CG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-bf16-CG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-bf16-noCG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-bf16-noCG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-bf16-CG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-bf16-noCG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-bf16-noCG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-bf16-CG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-bf16-CG-noTriton-False-False]":
    "xfail due to SW-184834",
    "unit/hybrid_engine/test_he_llama.py::TestHybridEngineLlama::test_functionality[huggyllama/llama-7b-bsz=2]":
    " xfail due to SW-185015",
    "unit/hybrid_engine/test_he_llama.py::TestHybridEngineLlama::test_functionality[huggyllama/llama-7b-bsz=1]":
    " xfail due to SW-185015",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inf.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp32-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp16-CG-noTriton-True-False]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp32-noCG-noTriton-False-True]":
    "Xfail due to SW-189257",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-125m-text-generation-fp32-noCG-noTriton-False-True]":
    "Xfail due to SW-189257",
    "unit/inference/test_inference.py::TestMPSize::test[fp16-bloom-True]":
    "Xfail due to 189259",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization_cpu_offload[8bits]":
    "Xfail due to SW-182766",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_quantized_linear[4bits-1]":
    "Xfail due to SW-182766",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_half_int4_quantization":
    "Xfail due to SW-182766",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization[8bits]":
    "Xfail due to SW-182766",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant_cpu_offload[4bits]":
    "Xfail due to SW-182766",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant_cpu_offload[8bits]":
    "Xfail due to SW-182766",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization[4bits]":
    "Xfail due to SW-182766",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_quantized_linear[8bits-1]":
    "Xfail due to SW-182766",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization_cpu_offload[4bits]":
    "Xfail due to SW-182766",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_half_int8_quantization":
    "Xfail due to SW-182766",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant[4bits]":
    "Xfail due to SW-182766",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant[8bits]":
    "Xfail due to SW-182766",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp32-CG-noTriton-True-True]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test_odd_world_size[fp16-marian-True-True]":
    "Xfail due to sw-203720",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test[fp16-marian-True-True]":
    "Xfail due to sw-203720",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test[bf16-marian-True-False]":
    "Xfail due to SW-203720",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test_odd_world_size[fp16-marian-True-False]":
    "Xfail due to SW-203720",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test_odd_world_size[bf16-marian-True-False]":
    "Xfail due to SW-203720",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test[fp16-marian-True-False]":
    "Xfail due to SW-203720",
    "unit/linear/test_quant_param.py::TestQuantParam::test_hf_clone":
    "AssertionError: Quantize fallback only supports quantization to FP8",
    "unit/linear/test_linear.py::TestQuantLinear::test[6]":
    "AssertionError: Quantize fallback only supports quantization to FP8",
    "unit/linear/test_linear.py::TestOptimizedLinear::test[qbit6-bws2]":
    "AssertionError: Quantize fallback only supports quantization to FP8",
    "unit/linear/test_linear.py::TestOptimizedLinear::test[qbit6-bws1]":
    "AssertionError: Quantize fallback only supports quantization to FP8",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[3-True-False]":
    "Xfail due to SW-209651",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[3-True-deepspeed_adam-False]":
    "Xfail due to SW-209651",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[3-True-True]":
    "Flaky xfail due to SW-210176",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[3-True-True]":
    "Flaky xfail due to SW-210176",
    "unit/ops/fp_quantizer/test_fp_quant.py::test_fp_quant_meta[bf16]":
    "xfail due to SW-209649",
    "unit/ops/fp_quantizer/test_fp_quant.py::test_fp_quant[qbits8-bf16]":
    "xfail due to SW-209649",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[True-False-lp_params]":
    "Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[False-False-lp_params]":
    "Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[False-True-lp_params]":
    "Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[True-True-hp_params]":
    "Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[False-True-optim_states]":
    "Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[True-False-hp_params]":
    "Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[False-True-hp_params]":
    "Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[False-False-hp_params]":
    "Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[True-False-contiguous_grad_buffer]":
    "Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[True-True-contiguous_grad_buffer]":
    "Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[True-True-optim_states]":
    "Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[False-False-lp_grads]":
    "Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[True-True-lp_params]":
    "Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[False-True-lp_grads]":
    "Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[False-True-contiguous_grad_buffer]":
    "Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[True-False-optim_states]":
    "Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[True-False-lp_grads]":
    "Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[False-False-optim_states]":
    "Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[True-True-lp_grads]":
    "Xfail due to SW-212099",
    "unit/runtime/zero/test_offload_states.py::TestOffloadStates::test_offload_states[False-False-contiguous_grad_buffer]":
    "Xfail due to SW-212099",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[3-True-False]":
    "Xfail due to SW-210176",
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[16-fp16]":
    "Flaky failure",
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[8-fp16]":
    "Flaky failure",
    "unit/linear/test_ctx.py::TestInitTransformers::test_config_init":
    "Xfail due to SW-215738",
    "unit/linear/test_ctx.py::TestInitTransformers::test_pretrained_init":
    "Xfail due to SW-215738",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[3-True-deepspeed_adam-True]":
    "Xfail, due to SW-179864.",
}
g3_eager_xfail_tests = {
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[nvme-1-dtype1]":
    "Xfail due to SW-196568 This op had not been implemented on HPU backend",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[nvme-3-dtype2]":
    "Xfail due to SW-196568 This op had not been implemented on HPU backend",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[nvme-1-dtype0]":
    "Xfail due to SW-196568 This op had not been implemented on HPU backend",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[nvme-3-dtype1]":
    "Xfail due to SW-196568 This op had not been implemented on HPU backend",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[nvme-3-dtype0]":
    "Xfail due to SW-196568 This op had not been implemented on HPU backend",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[64-160-128-2-24-False-True-0.2]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[8-1600-128-25-3-True-True-0.05]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[8-160-128-2-3-True-True-0.1]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[8-1600-128-2-3-True-True-0.05]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[64-1600-128-2-4-False-True-0.2]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForwardSmallBatchSize::test_forward_with_small_bsz[8-3-1024-512-16-3-False-False]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForwardSmallBatchSize::test_forward_with_small_bsz[8-7-1024-512-16-3-True-True]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForwardSmallBatchSize::test_forward_with_small_bsz[8-3-1024-512-16-3-True-False]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForwardSmallBatchSize::test_forward_with_small_bsz[8-7-1024-512-16-3-False-True]":
    "xfail due to SW-176905",
    "unit/runtime/comm/test_coalesced_collectives.py::TestAllToAllQuantReduceFallback::test_1d_tensor":
    "xfail due to SW-182766",
    "unit/runtime/comm/test_coalesced_collectives.py::TestAllToAllQuantReduceFallback::test_non_divisible":
    "xfail due to SW-182766",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant_nvme_offload":
    "xfail due to SW-168596",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization_nvme_offload":
    "xfail due to SW-168596",
    "unit/ops/lion/test_lion.py::TestLionConfigs::test[Lion-False-FusedLion]":
    "xfail due to SW-176903",
    "unit/ops/lion/test_lion.py::TestLionConfigs::test[Lion-True-DeepSpeedCPULion]":
    "xfail due to SW-176903",
    "unit/accelerator/test_accelerator.py::test_abstract_methods_defined[deepspeed.accelerator.xpu_accelerator]":
    "Xfail due to SW-182749",
    "unit/launcher/test_user_args.py::test_user_args[True-I'm going to tell them \"DeepSpeed is the best\"]":
    "Xfail due to SW-182753",
    "unit/launcher/test_user_args.py::test_user_args[True-'\"translate English to Romanian: \"']":
    "Xfail due to SW-182753",
    "unit/launcher/test_user_args.py::test_user_args[True-'I am 72\" tall']":
    "Xfail due to SW-182753",
    "unit/launcher/test_user_args.py::test_user_args[True-\"I am 6' tall\"]":
    "Xfail due to SW-182753",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[22-fp16]":
    "Xfail due to SW-188274",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1024-fp16]":
    "Xfail due to SW-188274",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1048576-fp16]":
    "Xfail due to SW-188274",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[64-fp16]":
    "Xfail due to SW-188274",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[128-fp16]":
    "Xfail due to SW-188274",
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[16-fp16]":
    "Xfail due to SW-188274",
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[8-fp16]":
    "Xfail due to SW-188274",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[True-False-1-dtype1]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[True-False-1-dtype2]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[False-True-1-dtype1]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[False-False-1-dtype0]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[True-True-1-dtype0]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[True-False-1-dtype1]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[False-True-1-dtype1]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[False-True-1-dtype2]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[True-True-1-dtype1]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[False-True-1-dtype2]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[True-False-1-dtype2]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[True-True-1-dtype2]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[True-False-1-dtype0]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[False-False-1-dtype1]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[False-True-1-dtype0]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[True-True-1-dtype0]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[False-False-1-dtype1]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[False-False-1-dtype2]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[False-True-1-dtype0]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[True-True-1-dtype2]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[False-True-1-dtype1]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[True-True-1-dtype1]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[True-True-1-dtype2]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[False-True-1-dtype2]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[False-False-1-dtype1]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[True-False-1-dtype0]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[False-False-1-dtype2]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[False-False-1-dtype0]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[True-False-1-dtype0]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[True-True-1-dtype0]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[True-False-1-dtype2]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[False-True-1-dtype0]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[True-False-1-dtype1]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to4[False-False-1-dtype2]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_4to2[True-True-1-dtype1]":
    "Xfail due to SW-187821",
    "unit/checkpoint/test_universal_checkpoint.py::TestZeROUniversalCheckpointDP::test_dp_world_size_2to2[False-False-1-dtype0]":
    "Xfail due to SW-187821",
    "unit/compression/test_dequantization.py::TestDequantization::test_dequantize":
    "Xfail due to SW-168442",
    "unit/inference/test_human_eval.py::test_human_eval[codellama/CodeLlama-7b-Python-hf]":
    "Xfail due to SW-182759",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp16-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp32-CG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp32-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp16-noCG-noTriton-True-False]":
    "xfail due to SW-163097",
    "unit/inference/test_stable_diffusion.py::TestStableDiffusion::test":
    "Xfail, due to SW-170181.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-160-128-2-24-False-True]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1600-128-25-3-True-True]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-384-16-3-False-True]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-509-16-3-True-False]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-4096-128-64-3-True-True]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-384-16-3-True-True1]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-1024-21-16-3-False-True]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[3-1024-51-16-3-True-False]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1536-128-24-3-False-True]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-1024-53-16-3-False-True]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-381-16-3-True-False]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-512-16-3-True-True]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-120-16-3-True-True]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-512-16-3-False-False]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1600-128-25-3-False-True]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-2048-128-32-3-False-False]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-384-16-3-True-True0]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[1-256-2048-32-3-True-True]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-119-16-3-True-False]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-160-128-2-3-False-True]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-384-16-3-False-False]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1536-128-24-3-False-False]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-2560-128-40-3-False-True]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[3-1024-54-16-3-True-True]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-511-16-3-False-True]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-160-128-2-3-True-True]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-1024-24-16-3-False-False]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-1024-56-16-3-False-False]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-128-128-2-3-True-False]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-256-52-4-3-True-True]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-8192-128-64-3-False-True]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-128-128-2-3-True-True]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-2560-128-40-3-False-False]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-2048-128-32-3-False-True]":
    "xfail due to SW-176905",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1600-128-2-3-True-True]":
    "xfail due to SW-176905",
    "unit/inference/test_model_profiling.py::TestModelProfiling::test[True-True]":
    "Xfail, due to SW-163097",
    "unit/inference/test_model_profiling.py::TestModelProfiling::test[True-False]":
    "Xfail, due to SW-163097",
    "unit/inference/test_model_profiling.py::TestModelProfiling::test[False-True]":
    "Xfail, due to SW-163097",
    "unit/inference/test_model_profiling.py::TestModelProfiling::test[False-False]":
    "Xfail, due to SW-163097",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[1-9-1024]":
    "Xfail, due to SW-164239",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[4-9-1024]":
    "Xfail, due to SW-164239",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[2-9-1024]":
    "Xfail, due to SW-164239",
    "unit/inference/test_inference.py::TestMPSize::test[fp16-bloom-False]":
    "Xfail, due to SW-196522.",
    "unit/hybrid_engine/test_he_llama.py::TestHybridEngineLlama::test_functionality[huggyllama/llama-7b-bsz=2]":
    "xfail due to SW-185015",
    "unit/hybrid_engine/test_he_llama.py::TestHybridEngineLlama::test_functionality[huggyllama/llama-7b-bsz=1]":
    "xfail due to SW-185015",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-noCG-noTriton-True-False]":
    "Graphic compile failed",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-noCG-noTriton-False-False]":
    "Graph compile failed",
    "unit/utils/test_init_on_device.py::TestOnDevice::test_on_device[hpu]":
    "Xfail, due to SW-178730.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp16-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp16-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp32-CG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp32-noCG-noTriton-True-True]":
    "Xfail due to SW-163097",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-125m-text-generation-fp32-noCG-noTriton-False-True]":
    "Xfail due to SW-196571 Assertion error",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp16-noCG-noTriton-False-True]":
    "Xfail due to SW-196571 Assertion error",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp32-noCG-noTriton-False-True]":
    "Xfail due to SW-196571 Assertion error",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-125m-text-generation-fp16-noCG-noTriton-False-True]":
    "Xfail due to SW-196571 Assertion error",
    "unit/inference/test_inference.py::TestMPSize::test[fp16-bloom-True]":
    "Xfail due to SW-196522",
    "unit/inference/test_inference.py::TestInjectionPolicy::test[ws2-fp32-roberta-True]":
    "Xfail due to sw-193404",
    "unit/inference/test_inference.py::TestInjectionPolicy::test[ws2-fp32-t5-True]":
    "Xfail due to sw-193404",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization_cpu_offload[8bits]":
    "Xfail due to SW-182766",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_quantized_linear[4bits-1]":
    "Xfail due to SW-182766",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_half_int4_quantization":
    "Xfail due to SW-182766",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization[8bits]":
    "Xfail due to SW-182766",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant_cpu_offload[4bits]":
    "Xfail due to SW-182766",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant_cpu_offload[8bits]":
    "Xfail due to SW-182766",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization[4bits]":
    "Xfail due to SW-182766",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_quantized_linear[8bits-1]":
    "Xfail due to SW-182766",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization_cpu_offload[4bits]":
    "Xfail due to SW-182766",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_half_int8_quantization":
    "Xfail due to SW-182766",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant[4bits]":
    "Xfail due to SW-182766",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant[8bits]":
    "Xfail due to SW-182766",
    "unit/checkpoint/test_pipeline.py::TestPipelineCheckpoint::test_checkpoint_pipe_engine[0-True]":
    "Xfail due to SW-199012",
    "unit/checkpoint/test_pipeline.py::TestPipelineCheckpoint::test_checkpoint_pipe_engine[1-True]":
    "Xfail due to SW-199012",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[2-True-True]":
    "xfail due to sw-201097",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[4-False-True]":
    "xfail due to sw-201097",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[4-True-True]":
    "xfail due to sw-201097",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[2-False-True]":
    "xfail due to sw-201097",
    "unit/linear/test_quant_param.py::TestQuantParam::test_hf_clone":
    "AssertionError: Quantize fallback only supports quantization to FP8",
    "unit/linear/test_linear.py::TestQuantLinear::test[6]":
    "AssertionError: Quantize fallback only supports quantization to FP8",
    "unit/linear/test_linear.py::TestOptimizedLinear::test[qbit6-bws2]":
    "AssertionError: Quantize fallback only supports quantization to FP8",
    "unit/linear/test_linear.py::TestOptimizedLinear::test[qbit6-bws1]":
    "AssertionError: Quantize fallback only supports quantization to FP8",
    "unit/linear/test_ctx.py::TestInitTransformers::test_config_init":
    "Xfail due to SW-215738",
    "unit/linear/test_ctx.py::TestInitTransformers::test_pretrained_init":
    "Xfail due to SW-215738",
}
gpu_xfail_tests = {
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test_odd_world_size[bf16-marian-False-False]":
    "bfloat16 is not supported",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-2-full-dtype0]":
    "bf16 is not supported",
    "unit/runtime/test_ds_initialize.py::TestConfigOptimizer::test[False]":
    "Xfail due to Cuda OOM",
    "unit/runtime/test_ds_initialize.py::TestConfigOptimizer::test[True]":
    "Xfail due to Cuda OOM",
    "unit/runtime/test_ds_initialize.py::TestClientLrScheduler::test[None-_LRScheduler]":
    "Xfail due to Cuda OOM",
    "unit/hybrid_engine/test_he_llama.py::TestHybridEngineLlama::test_functionality[huggyllama/llama-7b-bsz=2]":
    "Test requires higher memory.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_zero3_int4_post_init_quant_nvme_offload":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_zero3_int4_quantized_initialization_nvme_offload":
    "Xfailed. failure observed on vanilla as well.",
    "unit/ops/quantizer/test_fake_quantization.py::test_fake_quant_dequant[16-tensor_shape0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/ops/quantizer/test_fake_quantization.py::test_fake_quant_dequant[1-tensor_shape0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/ops/quantizer/test_fake_quantization.py::test_fake_quant_dequant[16-tensor_shape1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/ops/quantizer/test_fake_quantization.py::test_fake_quant_dequant[1-tensor_shape1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/hybrid_engine/test_he_llama.py::TestHybridEngineLlama::test_functionality[huggyllama/llama-7b-bsz=1]":
    "Test requires higher memory.",
    "unit/inference/v2/kernels/ragged_ops/test_atom_builder.py::test_single_sequence[seq_params2]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_atom_builder.py::test_single_sequence[seq_params0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_atom_builder.py::test_single_sequence[seq_params3]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_atom_builder.py::test_single_sequence[seq_params1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_multiple_prompts[prompt_lengths3]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_multiple_prompts[prompt_lengths1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_continuation[seq_params1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_single_prompt[2037]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_rotary_emb[False]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_gqa[head_config0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_rotary_emb[True]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_single_prompt[65]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_single_prompt[128]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_single_prompt[256]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_head_size[128]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_single_prompt[33]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_single_prompt[2]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_continuation[seq_params4]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_gqa[head_config2]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_head_size[64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_multiple_prompts[prompt_lengths2]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_fully_composed":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_gqa[head_config1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_multiple_prompts[prompt_lengths0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_continuation[seq_params0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_continuation[seq_params3]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_continuation[seq_params2]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_kv_copy.py::test_single_sequence_multiple_blocks[177-0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_kv_copy.py::test_single_sequence_multiple_blocks[117-88]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_kv_copy.py::test_single_sequence_single_block[33-8]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_kv_copy.py::test_single_sequence_multiple_blocks[169-8]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_kv_copy.py::test_single_sequence_single_block[17-0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_kv_copy.py::test_single_sequence_multiple_blocks[128-0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_kv_copy.py::test_multi_sequence":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_kv_copy.py::test_single_sequence_single_block[1-0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_kv_copy.py::test_single_sequence_single_block[63-1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_multiple_blocks[False-169-8]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_multi_sequences[True]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_single_block[False-1-0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_multiple_blocks[True-169-8]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_single_block[True-1-0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_multiple_blocks[False-177-0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_multi_sequences[False]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_single_block[True-33-15]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_single_block[True-17-0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_single_block[False-33-15]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_multiple_blocks[False-128-0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_multiple_blocks[True-117-88]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_single_block[False-17-0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_single_block[False-1-63]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_multiple_blocks[True-128-0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_multiple_blocks[False-117-88]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_single_block[True-1-63]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_multiple_blocks[True-177-0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_logits_gather.py::test_supported_dtypes[dtype0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_logits_gather.py::test_problem_size_permutations[1024]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_logits_gather.py::test_multiple_sequences[seq_lens0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_logits_gather.py::test_problem_size_permutations[6144]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_logits_gather.py::test_multiple_sequences[seq_lens3]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_logits_gather.py::test_supported_dtypes[dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_logits_gather.py::test_problem_size_permutations[6784]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_logits_gather.py::test_multiple_sequences[seq_lens2]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_logits_gather.py::test_multiple_sequences[seq_lens1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_moe_gather.py::test_moe_gather[False-278-64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_moe_gather.py::test_moe_gather[False-13-64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_moe_gather.py::test_moe_gather[False-1977-64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_moe_gather.py::test_moe_gather[True-278-64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_moe_gather.py::test_moe_gather[True-13-64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_moe_gather.py::test_moe_gather[True-1977-64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_multi_expert[1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_moe_scatter.py::test_moe_scatter[True-13-64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_moe_scatter.py::test_moe_scatter[False-13-64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_moe_scatter.py::test_moe_scatter[True-1977-64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_moe_scatter.py::test_moe_scatter[True-278-64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_moe_scatter.py::test_moe_scatter[False-278-64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_moe_scatter.py::test_moe_scatter[False-1977-64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_positional_embedding[seq_lens0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_problem_size_permutations[50304-6144]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_dtype_permutations[embed_dtype1-token_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_positional_embedding[seq_lens1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_complex_sequences[True-seq_lens1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_positional_embedding_offset":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_problem_size_permutations[32000-5120]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_complex_sequences[True-seq_lens0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_problem_size_permutations[1024-1024]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_positional_embedding[seq_lens3]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_dtype_permutations[embed_dtype0-token_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_complex_sequences[False-seq_lens0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_dtype_permutations[embed_dtype0-token_dtype0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_positional_embedding[seq_lens2]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_dtype_permutations[embed_dtype1-token_dtype0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_complex_sequences[False-seq_lens1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_top_1_gating.py::test_single_mapping_gating[433-128]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_top_1_gating.py::test_score_accuracy[32-128]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_top_1_gating.py::test_negative_logits":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_top_1_gating.py::test_score_accuracy[89-128]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_top_1_gating.py::test_single_mapping_gating[32-128]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_top_1_gating.py::test_single_mapping_gating[89-128]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_top_1_gating.py::test_single_mapping_gating[17-16]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_top_1_gating.py::test_single_mapping_gating[1-16]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_top_1_gating.py::test_score_accuracy[433-2]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_top_1_gating.py::test_score_accuracy[17-16]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_top_1_gating.py::test_determinism":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_top_1_gating.py::test_score_accuracy[1-16]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear_t[problem_shape0-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear_t[problem_shape4-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear_t[problem_shape7-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear[problem_shape5-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear_t[problem_shape1-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear[problem_shape3-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear[problem_shape2-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear[problem_shape4-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear_t[problem_shape3-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear[problem_shape6-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear_t[problem_shape5-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear[problem_shape7-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear_t[problem_shape6-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear[problem_shape1-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear_t[problem_shape2-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear[problem_shape0-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_multiple_prompts[prompt_lengths3]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_single_prompt[256]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_gqa[head_config0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_continuation[seq_params2]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_multiple_prompts[prompt_lengths1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_single_prompt[65]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_continuation[seq_params0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_head_size[128]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_continuation[seq_params4]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_single_prompt[2]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_fully_composed":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_head_size[64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_continuation[seq_params1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_multiple_prompts[prompt_lengths0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_continuation[seq_params3]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_gqa[head_config2]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_single_prompt[128]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_single_prompt[33]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_single_prompt[2037]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_multiple_prompts[prompt_lengths2]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_gqa[head_config1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_cutlass_moe.py::test_expert_variance[64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_cutlass_moe.py::test_in_out_channels[2048-8192]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_cutlass_moe.py::test_expert_variance[32]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_cutlass_moe.py::test_activation_types[ActivationType.RELU]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_cutlass_moe.py::test_dtypes[dtype0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_cutlass_moe.py::test_activation_types[ActivationType.GELU]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_cutlass_moe.py::test_activation_types[ActivationType.SILU]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_cutlass_moe.py::test_successive_inputs":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_cutlass_moe.py::test_in_out_channels[4096-2048]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_cutlass_moe.py::test_in_out_channels[6144-3072]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_cutlass_moe.py::test_expert_variance[2]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_dtypes[DtypeEnum.bf16]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_act_fns[ActivationType.GELU]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_dtypes[DtypeEnum.fp16]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_single_expert[13-2048-2048]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_act_fns[ActivationType.SILU]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_multi_expert[64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_single_expert[256-1024-4096]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_multi_expert[4]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_single_expert[893-5120-2560]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_multi_expert[16]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_multi_expert[128]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_act_fns[ActivationType.RELU]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_single_expert[278-5120-2048]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_multi_expert[1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant_nvme_offload":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization_nvme_offload":
    "Xfailed. failure observed on vanilla as well.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-8192-128-64-3-False-True]":
    "Test requires higher memory.",
    "unit/ops/adam/test_adamw/TestAdamConfigs/test[AdamW-True-False-True-resulting_optimizer6]":
    "Xfail, due to SW-176845",
    "unit/ops/adam/test_adamw/TestAdamConfigs/test[AdamW-True-False-False-resulting_optimizer2]":
    "Xfail, due to SW-176845",
    "unit/ops/adam/test_adamw/TestAdamConfigs/test[Adam-True-False-True-resulting_optimizer14]":
    "Xfail, due to SW-176845",
    "unit/ops/adam/test_adamw/TestAdamConfigs/test[Adam-True-False-False-resulting_optimizer10]":
    "Xfail, due to SW-176845",
    "unit/inference/test_inference.py::TestMPSize::test[fp32-gpt-neo]":
    "Xfail due to SW-177890 and SW-177889",
    "unit/hybrid_engine/test_he_all.py::TestHybridEngineTextGen::test_functionality[facebook/opt-1.3b-bsz=1]":
    "Xfail due to SW-177889",
    "unit/hybrid_engine/test_he_all.py::TestHybridEngineTextGen::test_functionality[EleutherAI/gpt-neo-1.3B-bsz=2]":
    "Xfail due to SW-177889",
    "unit/hybrid_engine/test_he_all.py::TestHybridEngineTextGen::test_functionality[facebook/opt-1.3b-bsz=2]":
    "Xfail due to SW-177889",
    "unit/hybrid_engine/test_he_all.py::TestHybridEngineTextGen::test_functionality[EleutherAI/gpt-neo-1.3B-bsz=1]":
    "Xfail due to SW-177889",
    "unit/inference/test_inference.py::TestMPSize::test[fp16-gpt-neo]":
    "Xfail due to SW-177889",
    "unit/inference/test_inference.py::TestLowCpuMemUsage::test[gpt2-False]":
    "Xfail due to SW-177889",
    "unit/inference/test_model_profiling.py::TestModelProfiling::test[False-False]":
    "Xfail due to SW-177889",
    "unit/inference/test_model_profiling.py::TestModelProfiling::test[False-True]":
    "Xfail due to SW-177889",
    "unit/inference/test_model_profiling.py::TestModelProfiling::test[True-False]":
    "Xfail due to SW-177889",
    "unit/inference/test_model_profiling.py::TestModelProfiling::test[True-True]":
    "Xfail due to SW-177889",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-2-dtype2]":
    "Xfail due to pytorch>2.0 is required and Nvidia Titan XP GPU not supported",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[nvme-3-dtype2]":
    "Xfail due to pytorch>2.0 is required and Nvidia Titan XP GPU not supported",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-1-dtype1]":
    "Xfail due to pytorch>2.0 is required and Nvidia Titan XP GPU not supported",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-2-dtype1]":
    "Xfail due to pytorch>2.0 is required and Nvidia Titan XP GPU not supported",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[nvme-3-dtype1]":
    "Xfail due to pytorch>2.0 is required and Nvidia Titan XP GPU not supported",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-1-dtype2]":
    "Xfail due to pytorch>2.0 is required and Nvidia Titan XP GPU not supported",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-2-dtype1]":
    "Xfail due to pytorch>2.0 is required and Nvidia Titan XP GPU not supported",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-1-dtype1]":
    "Xfail due to pytorch>2.0 is required and Nvidia Titan XP GPU not supported",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-2-dtype2]":
    "Xfail due to pytorch>2.0 is required and Nvidia Titan XP GPU not supported",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-1-dtype2]":
    "Xfail due to pytorch>2.0 is required and Nvidia Titan XP GPU not supported",
    "unit/runtime/compile/test_load_config.py::TestConfigLoad::test_compile":
    "Nvidia Titan XP GPU not supported",
    "unit/runtime/compile/test_load_config.py::TestConfigLoad::test_set_compile_kwargs":
    "Nvidia Titan XP GPU not supported",
    "unit/runtime/compile/test_load_config.py::TestConfigLoad::test_set_compiler_fn":
    "Nvidia Titan XP GPU not supported",
    "unit/runtime/compile/test_load_config.py::TestConfigLoad::test_compile_kwargs":
    "Nvidia Titan XP GPU not supported",
    "unit/inference/test_model_profiling.py::TestModelProfiling::test[True-True]":
    "Xfail due to SW-177889",
    "unit/inference/test_model_profiling.py::TestModelProfiling::test[False-True]":
    "Xfail due to SW-177889",
    "unit/inference/test_model_profiling.py::TestModelProfiling::test[True-False]":
    "Xfail due to SW-177889",
    "unit/inference/test_model_profiling.py::TestModelProfiling::test[False-False]":
    "Xfail due to SW-177889",
    "unit/inference/v2/ragged/test_manager_configs.py::test_too_small_max_ragged_batch_size":
    "Xfail due to ValidationError if the input data cannot be parsed to form a valid model",
    "unit/inference/v2/ragged/test_manager_configs.py::test_zero_max_tracked_sequences":
    "Xfail due to ValidationError if the input data cannot be parsed to form a valid model",
    "unit/inference/v2/ragged/test_manager_configs.py::test_zero_max_ragged_batch_size":
    "Xfail due to ValidationError if the input data cannot be parsed to form a valid model",
    "unit/inference/v2/ragged/test_manager_configs.py::test_negative_max_ragged_batch_size":
    "Xfail due to ValidationError if the input data cannot be parsed to form a valid model",
    "unit/inference/v2/ragged/test_manager_configs.py::test_too_small_max_tracked_sequences":
    "Xfail due to ValidationError if the input data cannot be parsed to form a valid model",
    "unit/inference/v2/ragged/test_manager_configs.py::test_negative_max_tracked_sequences":
    "Xfail due to ValidationError if the input data cannot be parsed to form a valid model",
    "unit/inference/v2/ragged/test_manager_configs.py::test_zero_max_ragged_sequence_count":
    "Xfail due to ValidationError if the input data cannot be parsed to form a valid model",
    "unit/inference/v2/ragged/test_manager_configs.py::test_negative_max_ragged_sequence_count":
    "Xfail due to ValidationError if the input data cannot be parsed to form a valid model",
    "unit/checkpoint/test_latest_checkpoint.py::TestLatestCheckpoint::test_existing_latest[True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[1-False-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[3-False-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[3-True-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[2-True-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[1-False-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[0-False-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[2-False-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_lr_scheduler[3-False-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[2-False-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[0-False-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[3-True-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_lr_scheduler.py::TestLRSchedulerCheckpoint::test_checkpoint_no_lr_scheduler[2-True-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[4-True-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[2-True-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[2-False-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[4-False-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_other_optimizer.py::TestOtherOptimizerCheckpoint::test_checkpoint_unfused_optimizer[True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_other_optimizer.py::TestOtherOptimizerCheckpoint::test_checkpoint_fused_optimizer[True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_other_optimizer.py::TestOtherOptimizerCheckpoint::test_checkpoint_fp32_optimizer[True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_load_immediate_save[0-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_save_before_accum_grad_is_done[0-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_load_immediate_save[2-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_save_before_accum_grad_is_done[1-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_save_before_accum_grad_is_done[2-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_save_before_accum_grad_is_done[3-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_load_immediate_save[3-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROSaveLoadEdgeCase::test_load_immediate_save[1-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[True-True-True-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[False-False-False-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[False-True-False-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[False-True-True-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[True-False-False-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[False-False-True-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[True-True-False-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[True-False-True-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_not_load_optimizer_state[3-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_module_only[3-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_module_only[2-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_optimizer_state[2-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_optimizer_state[3-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_not_load_optimizer_state[1-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_module_only[1-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_load_optimizer_state[1-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_not_load_optimizer_state[2-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[3-True-deepspeed_adam-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[3-False-Adam-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[3-True-deepspeed_adam-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[2-True-deepspeed_adam-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[2-True-deepspeed_adam-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[1-False-Adam-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_module_only[2-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_optimizer_state[2-False-Adam-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[1-False-Adam-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[3-False-Adam-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_module_only[1-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_module_only[3-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_hybrid_optimizer_state[1-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_hybrid_optimizer_state[2-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_not_load_optimizer_state[2-False-Adam-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_load_module_only[0-True]":
    "Compile tests not supported on Titan-XP",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_pipeline_checkpoint_loading[3-True]":
    "Compile tests not supported on Titan-XP",
    "unit/inference/test_human_eval.py::test_human_eval[codellama/CodeLlama-7b-Python-hf]":
    "Xfail due to SW-182759",
    "unit/launcher/test_user_args.py::test_user_args[True-I'm going to tell them \"DeepSpeed is the best\"]":
    "Xfail due to SW-182753",
    "unit/launcher/test_user_args.py::test_user_args[True-'\"translate English to Romanian: \"']":
    "Xfail due to SW-182753",
    "unit/launcher/test_user_args.py::test_user_args[True-'I am 72\" tall']":
    "Xfail due to SW-182753",
    "unit/launcher/test_user_args.py::test_user_args[True-\"I am 6' tall\"]":
    "Xfail due to SW-182753",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-CG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp32-CG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp32-CG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp32-CG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp32-CG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp32-CG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp16-CG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp16-CG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp16-CG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp16-CG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp16-noCG-noTriton-False-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp16-noCG-noTriton-False-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp16-CG-noTriton-False-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp16-CG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp16-CG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp16-CG-noTriton-False-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp16-CG-noTriton-False-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp16-CG-noTriton-False-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp16-CG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp16-CG-noTriton-False-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp16-CG-noTriton-False-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp16-noCG-noTriton-False-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp16-CG-noTriton-False-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp16-CG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp16-noCG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-base-fill-mask-fp16-noCG-noTriton-False-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp16-noCG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-uncased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-cased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp16-CG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp16-CG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp16-CG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp16-noCG-noTriton-False-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-large-cased-fill-mask-fp16-CG-noTriton-False-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-uncased-fill-mask-fp16-noCG-noTriton-False-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[FacebookAI/roberta-large-fill-mask-fp16-noCG-noTriton-False-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-cased-fill-mask-fp16-CG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp16-noCG-noTriton-False-False]":
    "Same failure in Vanilla.",
    "unit/inference/test_inference.py::TestModelTask::test[google-bert/bert-base-multilingual-uncased-fill-mask-fp16-noCG-noTriton-True-False]":
    "Same failure in Vanilla.",
    "unit/utils/test_init_on_device.py::TestOnDevice::test_on_device[hpu]":
    "Xfail, due to SW-178730.",
    "unit/inference/test_inference.py::TestMPSize::test[fp16-bloom-False]":
    "Xfail due to SW-196379",
    "unit/inference/test_inference.py::TestModelTask::test[bigscience/bloom-560m-text-generation-fp16-noCG-noTriton-True-False]":
    "Xfail due to SW-196379",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test_odd_world_size[bf16-marian-True-False]":
    "Xfail due to SW-203720",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test[fp16-marian-True-False]":
    "Xfail due to SW-203720",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test_odd_world_size[fp16-marian-True-False]":
    "Xfail due to SW-203720",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[True-dtype2-384-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm_residual[True-dtype2-512-128-32]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm_residual[True-dtype2-1024-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[True-dtype2-384-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm_residual[True-dtype2-1024-1-32]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm_residual[True-dtype2-8192-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[True-dtype2-2048-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm_residual[True-dtype2-512-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm_residual[True-dtype2-384-1-32]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm_residual[True-dtype2-8192-1-32]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[True-dtype2-8192-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm_residual[True-dtype2-2048-128-32]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[True-dtype2-2048-1-32]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm_residual[True-dtype2-2048-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm_residual[True-dtype2-14432-1-32]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm_residual[True-dtype2-384-128-32]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[True-dtype2-8192-1-32]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm_residual[True-dtype2-768-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[True-dtype2-14432-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[True-dtype2-512-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[True-dtype2-768-128-32]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[True-dtype2-14432-128-32]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[True-dtype2-1024-128-32]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[True-dtype2-2048-128-32]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm_residual[True-dtype2-14432-128-32]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[True-dtype2-1024-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[True-dtype2-384-1-32]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[True-dtype2-768-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm_residual[True-dtype2-8192-128-32]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[True-dtype2-512-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm_residual[True-dtype2-8192-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[True-dtype2-2048-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[True-dtype2-8192-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm_residual[True-dtype2-512-1-32]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm_residual[True-dtype2-768-128-32]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[True-dtype2-14432-1-32]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[True-dtype2-512-128-32]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[True-dtype2-1024-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm_residual[True-dtype2-384-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[True-dtype2-768-1-32]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm_residual[True-dtype2-384-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[True-dtype2-512-1-32]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm_residual[True-dtype2-2048-1-32]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm_residual[True-dtype2-1024-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[True-dtype2-1024-1-32]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[True-dtype2-384-128-32]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[True-dtype2-8192-128-32]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm_residual[True-dtype2-768-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm_residual[True-dtype2-512-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm_residual[True-dtype2-14432-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm_residual[True-dtype2-14432-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm_residual[True-dtype2-768-1-32]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[True-dtype2-768-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[True-dtype2-14432-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm_residual[True-dtype2-2048-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm_residual[True-dtype2-1024-128-32]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-True-dtype2-512-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-True-dtype2-4096-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-False-dtype2-4096-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-False-dtype2-4096-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-True-dtype2-512-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-True-dtype2-512-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-False-dtype2-1232-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-False-dtype2-1232-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-False-dtype2-512-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-False-dtype2-512-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-False-dtype2-512-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-False-dtype2-512-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-True-dtype2-4096-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-True-dtype2-512-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-True-dtype2-4096-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-False-dtype2-512-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-True-dtype2-1232-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-False-dtype2-1232-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-False-dtype2-1232-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-True-dtype2-4096-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-True-dtype2-512-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-True-dtype2-1232-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-False-dtype2-4096-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-False-dtype2-4096-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-False-dtype2-1232-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-False-dtype2-512-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-False-dtype2-512-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-False-dtype2-1232-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-True-dtype2-512-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-True-dtype2-1232-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-True-dtype2-4096-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-True-dtype2-4096-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-True-dtype2-1232-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-True-dtype2-4096-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-False-dtype2-1232-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-True-dtype2-4096-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-False-dtype2-512-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-True-dtype2-512-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-False-dtype2-1232-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-False-dtype2-4096-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-False-dtype2-4096-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-True-dtype2-4096-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-True-dtype2-512-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-False-dtype2-4096-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-False-dtype2-4096-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-True-dtype2-4096-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-False-dtype2-512-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-False-dtype2-512-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-True-dtype2-4096-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-True-dtype2-1232-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-True-dtype2-4096-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-True-dtype2-4096-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-True-dtype2-1232-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-True-dtype2-512-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-True-dtype2-1232-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-True-dtype2-4096-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-True-dtype2-512-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-True-dtype2-1232-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-False-dtype2-4096-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-False-dtype2-4096-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-False-dtype2-4096-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-False-dtype2-1232-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-False-dtype2-1232-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-True-dtype2-512-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-True-dtype2-4096-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-False-dtype2-1232-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-True-dtype2-512-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-True-dtype2-1232-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-False-dtype2-512-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-False-dtype2-4096-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-False-dtype2-512-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-False-dtype2-1232-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-True-dtype2-512-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-True-dtype2-512-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-False-dtype2-4096-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-False-dtype2-4096-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-False-dtype2-4096-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-True-dtype2-4096-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-True-dtype2-1232-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-True-dtype2-512-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-False-dtype2-1232-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-False-dtype2-4096-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-True-dtype2-1232-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-False-dtype2-1232-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-False-dtype2-512-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-False-dtype2-512-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-False-dtype2-4096-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-False-dtype2-1232-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-False-dtype2-1232-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-False-dtype2-512-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-True-dtype2-4096-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-False-dtype2-512-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-False-dtype2-512-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-True-dtype2-512-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-True-dtype2-4096-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-False-dtype2-512-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-False-dtype2-1232-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-True-dtype2-1232-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-False-dtype2-1232-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-False-dtype2-4096-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-False-dtype2-1232-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-True-dtype2-1232-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-False-dtype2-4096-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-False-dtype2-1232-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-True-dtype2-4096-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-False-dtype2-512-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-True-dtype2-4096-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-True-dtype2-4096-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-False-dtype2-512-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-False-dtype2-1232-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-False-dtype2-4096-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-False-dtype2-512-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-True-dtype2-512-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-True-dtype2-4096-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-False-dtype2-4096-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-False-dtype2-512-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-True-dtype2-1232-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-True-dtype2-4096-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-True-dtype2-512-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-False-dtype2-1232-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-False-dtype2-512-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-False-dtype2-512-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-False-dtype2-1232-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-True-dtype2-512-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-True-dtype2-1232-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-False-dtype2-1232-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-False-dtype2-4096-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-False-dtype2-512-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-True-dtype2-4096-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-True-dtype2-512-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-False-dtype2-512-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-True-dtype2-512-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-False-dtype2-512-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-False-dtype2-1232-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-False-dtype2-1232-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-True-dtype2-1232-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-False-dtype2-4096-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-False-dtype2-4096-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-True-dtype2-1232-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-False-dtype2-4096-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-False-dtype2-512-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-True-dtype2-512-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-True-dtype2-512-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-False-dtype2-4096-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-True-dtype2-1232-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-True-dtype2-4096-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-True-dtype2-4096-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-True-dtype2-512-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-True-dtype2-4096-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-True-dtype2-4096-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-False-dtype2-512-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-False-dtype2-1232-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-True-dtype2-1232-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-False-dtype2-1232-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-True-dtype2-1232-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-False-dtype2-4096-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-False-dtype2-1232-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-False-dtype2-512-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-True-dtype2-4096-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-False-dtype2-4096-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-False-dtype2-4096-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-True-dtype2-4096-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-True-dtype2-512-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-True-dtype2-1232-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-True-dtype2-4096-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-False-dtype2-4096-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-True-dtype2-512-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-False-dtype2-512-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-True-dtype2-4096-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-False-dtype2-4096-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-False-dtype2-1232-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-True-dtype2-1232-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-False-dtype2-512-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-False-dtype2-4096-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-False-dtype2-1232-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-False-dtype2-4096-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-True-dtype2-512-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-False-dtype2-512-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-True-dtype2-512-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-True-dtype2-1232-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-True-dtype2-512-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-True-dtype2-1232-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-True-dtype2-1232-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-False-dtype2-1232-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-True-dtype2-1232-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-False-dtype2-1232-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-True-dtype2-1232-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-False-dtype2-4096-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-False-dtype2-512-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-False-dtype2-512-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-True-dtype2-4096-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-True-dtype2-1232-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-True-dtype2-512-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-False-dtype2-1232-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-True-dtype2-1232-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-True-dtype2-512-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-False-dtype2-1232-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-True-dtype2-4096-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-False-dtype2-4096-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-False-dtype2-4096-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-True-dtype2-4096-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-True-dtype2-512-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-True-dtype2-512-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-True-dtype2-512-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-True-dtype2-1232-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-False-dtype2-1232-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-False-dtype2-512-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-True-dtype2-1232-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-True-dtype2-4096-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-True-dtype2-4096-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-True-dtype2-4096-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-False-dtype2-512-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-False-dtype2-1232-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-False-dtype2-512-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-True-dtype2-4096-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-False-dtype2-1232-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-False-dtype2-512-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-True-dtype2-512-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-False-dtype2-4096-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-False-dtype2-4096-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-True-dtype2-1232-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-True-dtype2-1232-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-False-dtype2-1232-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-False-dtype2-1232-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-False-dtype2-1232-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-True-dtype2-1232-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-True-dtype2-4096-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-False-dtype2-4096-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-True-dtype2-4096-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-True-dtype2-1232-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-True-dtype2-512-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-False-dtype2-512-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-False-dtype2-1232-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-True-dtype2-1232-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-False-dtype2-4096-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-True-dtype2-1232-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-False-dtype2-1232-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-False-dtype2-1232-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-True-dtype2-1232-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-True-dtype2-4096-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-False-dtype2-4096-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-False-dtype2-512-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-True-dtype2-512-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-True-dtype2-512-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-True-dtype2-1232-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-False-dtype2-4096-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-False-dtype2-4096-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-True-dtype2-1232-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-True-dtype2-512-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-False-dtype2-4096-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-True-dtype2-512-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-True-dtype2-512-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-True-dtype2-4096-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-False-True-dtype2-1232-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-False-dtype2-4096-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-True-dtype2-1232-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-True-dtype2-512-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-False-dtype2-4096-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-True-dtype2-512-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-False-dtype2-1232-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-False-dtype2-1232-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-True-dtype2-512-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-True-dtype2-4096-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-True-dtype2-512-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-False-dtype2-512-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-False-dtype2-512-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-True-dtype2-1232-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-True-dtype2-1232-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-False-dtype2-512-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-True-dtype2-1232-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-True-dtype2-4096-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-False-dtype2-512-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-False-dtype2-1232-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-True-dtype2-512-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-True-dtype2-1232-128-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-True-dtype2-512-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-True-dtype2-1232-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-True-False-dtype2-4096-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-True-dtype2-4096-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-False-True-dtype2-1232-255-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-True-dtype2-4096-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-False-dtype2-512-1-1]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-1-True-True-dtype2-4096-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-True-True-dtype2-512-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-2-False-False-dtype2-512-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-False-dtype2-4096-1-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-True-1-False-False-dtype2-512-128-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_residual_add.py::test_residual_add[True-False-2-True-False-dtype2-1232-255-2]":
    "Xfail due to SW-211815",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_gated_silu[dtype2-512-255-2]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_bias_geglu[dtype2-1232-1-2]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_bias_geglu[dtype2-512-128-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_gated_silu[dtype2-512-128-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_gated_silu[dtype2-1232-128-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_gated_silu[dtype2-1232-255-2]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_gated_silu[dtype2-512-128-2]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_gated_silu[dtype2-4096-255-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_bias_geglu[dtype2-4096-255-2]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_gated_silu[dtype2-512-1-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_gated_silu[dtype2-512-1-2]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_gated_silu[dtype2-1232-255-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_bias_geglu[dtype2-1232-255-2]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_bias_geglu[dtype2-1232-255-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_bias_geglu[dtype2-4096-1-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_gated_silu[dtype2-4096-255-2]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_bias_geglu[dtype2-4096-1-2]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_gated_silu[dtype2-4096-128-2]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_gated_silu[dtype2-4096-1-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_bias_geglu[dtype2-1232-128-2]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_bias_geglu[dtype2-1232-128-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_bias_geglu[dtype2-512-255-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_bias_geglu[dtype2-1232-1-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_bias_geglu[dtype2-4096-128-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_gated_silu[dtype2-1232-1-2]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_bias_geglu[dtype2-512-1-2]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_bias_geglu[dtype2-4096-255-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_bias_geglu[dtype2-512-1-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_bias_geglu[dtype2-512-128-2]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_bias_geglu[dtype2-512-255-2]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_gated_silu[dtype2-1232-128-2]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_gated_silu[dtype2-512-255-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_gated_silu[dtype2-4096-1-2]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_gated_silu[dtype2-4096-128-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_gated_silu[dtype2-1232-1-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_bias_geglu.py::test_bias_geglu[dtype2-4096-128-2]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[False-dtype2-1024-128-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[False-dtype2-384-1-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[False-dtype2-14432-1-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[False-dtype2-14432-1-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[False-dtype2-8192-1-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[False-dtype2-1024-1-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[False-dtype2-512-1-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[False-dtype2-512-128-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[False-dtype2-768-128-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[False-dtype2-2048-1-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[False-dtype2-1024-1-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[False-dtype2-2048-128-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[False-dtype2-512-1-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[False-dtype2-14432-128-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[False-dtype2-768-1-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[False-dtype2-384-128-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[False-dtype2-14432-128-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[False-dtype2-1024-128-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[False-dtype2-512-128-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[False-dtype2-2048-1-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[False-dtype2-8192-1-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[False-dtype2-768-128-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[False-dtype2-2048-128-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[False-dtype2-768-1-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[False-dtype2-384-128-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[False-dtype2-8192-128-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[False-dtype2-8192-128-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_layer_norm.py::test_layer_norm[False-dtype2-384-1-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_moe_res_matmult.py::test_moe_residual_matmul[dtype2-1-64]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_moe_res_matmult.py::test_moe_residual_matmul[dtype2-4-16]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_moe_res_matmult.py::test_moe_residual_matmul[dtype2-1-16]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_moe_res_matmult.py::test_moe_residual_matmul[dtype2-4-64]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_rms_norm[dtype2-2048-1-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_pre_norm[dtype2-14432-128-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_rms_norm[dtype2-512-1-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_pre_norm[dtype2-384-128-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_pre_norm[dtype2-2048-1-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_rms_norm[dtype2-1024-128-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_pre_norm[dtype2-512-128-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_rms_norm[dtype2-8192-1-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_rms_norm[dtype2-512-128-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_rms_norm[dtype2-384-1-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_pre_norm[dtype2-768-1-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_rms_norm[dtype2-512-128-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_pre_norm[dtype2-8192-128-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_rms_norm[dtype2-384-1-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_rms_norm[dtype2-2048-1-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_rms_norm[dtype2-2048-128-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_rms_norm[dtype2-384-128-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_rms_norm[dtype2-2048-128-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_pre_norm[dtype2-768-128-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_rms_norm[dtype2-14432-1-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_rms_norm[dtype2-768-1-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_rms_norm[dtype2-768-128-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_pre_norm[dtype2-512-128-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_pre_norm[dtype2-384-1-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_pre_norm[dtype2-2048-1-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_pre_norm[dtype2-8192-1-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_pre_norm[dtype2-512-1-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_pre_norm[dtype2-1024-128-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_pre_norm[dtype2-14432-128-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_pre_norm[dtype2-8192-1-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_pre_norm[dtype2-1024-1-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_rms_norm[dtype2-8192-128-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_rms_norm[dtype2-512-1-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_pre_norm[dtype2-768-128-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_rms_norm[dtype2-8192-1-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_pre_norm[dtype2-384-128-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_pre_norm[dtype2-2048-128-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_rms_norm[dtype2-1024-1-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_pre_norm[dtype2-14432-1-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_pre_norm[dtype2-1024-1-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_rms_norm[dtype2-14432-128-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_pre_norm[dtype2-1024-128-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_pre_norm[dtype2-384-1-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_pre_norm[dtype2-8192-128-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_rms_norm[dtype2-14432-1-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_pre_norm[dtype2-14432-1-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_rms_norm[dtype2-1024-128-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_rms_norm[dtype2-768-128-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_rms_norm[dtype2-768-1-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_rms_norm[dtype2-384-128-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_pre_norm[dtype2-512-1-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_rms_norm[dtype2-1024-1-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_rms_norm[dtype2-14432-128-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_rms_norm[dtype2-8192-128-32]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_pre_norm[dtype2-768-1-1]":
    "Xfail due to SW-211828",
    "unit/ops/transformer/inference/test_rms_norm.py::test_pre_norm[dtype2-2048-128-32]":
    "Xfail due to SW-211828",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test[bf16-marian-True-False]":
    "Xfail due to SW-211832",
    "unit/checkpoint/test_convert_checkpoint.py::TestCheckpointConvert::test_convert_zero_checkpoint_to_fp32_state_dict":
    "Xfail due to SW-215491",
    "unit/runtime/test_ds_initialize.py::TestClientLrScheduler::test[Optimizer-None]":
    "Xfail due to Cuda OOM",
    "unit/runtime/test_ds_initialize.py::TestClientLrScheduler::test[None-None]":
    "Xfail due to Cuda OOM",
    "unit/runtime/test_ds_initialize.py::TestClientLrScheduler::test[None-Callable]":
    "Xfail due to Cuda OOM",
    "unit/runtime/test_ds_initialize.py::TestClientLrScheduler::test[Optimizer-Callable]":
    "Xfail due to Cuda OOM",
    "unit/runtime/test_ds_initialize.py::TestClientLrScheduler::test[Callable-None]":
    "Xfail due to Cuda OOM",
    "unit/runtime/test_ds_initialize.py::TestClientLrScheduler::test[Callable-Callable]":
    "Xfail due to Cuda OOM",
    "unit/runtime/test_ds_initialize.py::TestClientLrScheduler::test[Optimizer-_LRScheduler]":
    "Xfail due to Cuda OOM",
    "unit/runtime/test_ds_initialize.py::TestClientLrScheduler::test[Callable-_LRScheduler]":
    "Xfail due to Cuda OOM",
    "unit/runtime/test_ds_initialize.py::TestClientLrSchedulerInit::test_diff_lrscheler_and_callable_onecyclelr_steplr[_LRScheduler]":
    "Xfail due to Cuda OOM",
    "unit/runtime/test_ds_initialize.py::TestClientLrSchedulerInit::test_same_lrscheler_and_callable[Callable]":
    "Xfail due to Cuda OOM",
    "unit/runtime/test_ds_initialize.py::TestClientLrSchedulerInit::test_diff_lrscheler_and_callable_onecyclelr_steplr[Callable]":
    "Xfail due to Cuda OOM",
    "unit/runtime/test_ds_initialize.py::TestClientLrSchedulerInit::test_same_lrscheler_and_callable[_LRScheduler]":
    "Xfail due to Cuda OOM",
    "unit/runtime/test_ds_initialize.py::TestClientLrSchedulerInit::test_diff_lrscheler_and_callable[Callable]":
    "Xfail due to Cuda OOM",
    "unit/runtime/test_ds_initialize.py::TestClientLrSchedulerInit::test_diff_lrscheler_and_callable[None]":
    "Xfail due to Cuda OOM",
    "unit/runtime/test_ds_initialize.py::TestClientLrSchedulerInit::test_same_lrscheler_and_callable[None]":
    "Xfail due to Cuda OOM",
    "unit/runtime/test_ds_initialize.py::TestClientLrSchedulerInit::test_diff_lrscheler_and_callable_onecyclelr_steplr[None]":
    "Xfail due to Cuda OOM",
    "unit/runtime/test_ds_initialize.py::TestNoOptim::test[3]":
    "Xfail due to Cuda OOM",
    "unit/runtime/test_ds_initialize.py::TestNoOptim::test[0]":
    "Xfail due to Cuda OOM",
    "unit/runtime/test_ds_initialize.py::TestClientOptimizer::test[Callable]":
    "Xfail due to Cuda OOM",
    "unit/runtime/test_ds_initialize.py::TestClientOptimizer::test[None]":
    "Xfail due to Cuda OOM",
    "unit/runtime/test_ds_initialize.py::TestClientOptimizer::test[Optimizer]":
    "Xfail due to Cuda OOM",
    "unit/runtime/test_ds_initialize.py::TestClientLrSchedulerInit::test_diff_lrscheler_and_callable[_LRScheduler]":
    "ncclUnhandledCudaError: Call to CUDA function failed.",
}
