# 问题

相比qwen第一版，显存占用为什么增加了很多？

参考Issue: https://github.com/QwenLM/Qwen1.5/issues/240

# 原因

1. attention原因

    Qwen(1.0) will automatically enable flash attention if it is installed, which is no longer the case for Qwen1.5.

    To enable flash attention in Qwen1.5, please follow the instructions provided in the transformers' official documentation at https://huggingface.co/docs/transformers/perf_infer_gpu_one#flashattention-2. In short, please ensure that attn_implementation is set to "flash_attention_2" and torch_dtype is set to "auto" or torch.bfloat16 or torch.float16 when calling from_pretrained for it to take effect.

    We don't recommend bitsandbytes as you may suffer from substantial accuracy loss. If you must use quantization, try loading the GPTQ or the AWQ version and then use QLoRA.

2. Transformers问题

    - I think this may be related to the transformers issue: huggingface/transformers#30860. Since many models are influenced. In Qwen codes, there's no logits = logits.float().
    - https://github.com/huggingface/transformers/issues/30860