# 1. 问题

参考Issue: 相比qwen第一版，显存占用为什么增加了很多？ #240，https://github.com/QwenLM/Qwen1.5/issues/240

# 2. 原因

Maybe you choose the eager (default) mode for Attention.
Here is the part of source code:
QWEN2_ATTENTION_CLASSES = {
"eager": Qwen2Attention,
"flash_attention_2": Qwen2FlashAttention2,
"sdpa": Qwen2SdpaAttention,
}
self.self_attn = QWEN2_ATTENTION_CLASSES[config._attn_implementation](config, layer_idx)

# 3. 解决方案

wo methods for you, it works for me:

1. Add this parameters in config.json : "_attn_implementation": "sdpa"
2. Add this parameters in sft code:
   model = AutoModelForCausalLM.from_pretrained(
   model_args.model_name_or_path,
   config=config,
   cache_dir=training_args.cache_dir,
   device_map=device_map,
   attn_implementation="sdpa", # Add attn_implementation
   quantization_config=BitsAndBytesConfig(
   load_in_4bit=True,
   bnb_4bit_use_double_quant=True,
   bnb_4bit_quant_type="nf4",
   bnb_4bit_compute_dtype=compute_dtype,
   )
   if training_args.use_lora and lora_args.q_lora
   else None,
   **model_load_kwargs,
   )