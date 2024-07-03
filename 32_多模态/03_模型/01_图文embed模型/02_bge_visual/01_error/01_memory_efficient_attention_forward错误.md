# 1. 问题

```bash
Traceback (most recent call last):
 File "/home/flag_embed/FlagEmbedding/visual/bge_visualized.py", line 13, in <module>
   candi_emb_1 = model.encode(text="The Mid-Hudson Bridge, spanning the Hudson River between Poughkeepsie and Highland.", image="./imgs/wiki_candi_1.jpg")
 File "/home/flag_embed/FlagEmbedding/visual/modeling.py", line 101, in encode
   return self.encode_mm(image, text)
 File "/home/flag_embed/FlagEmbedding/visual/modeling.py", line 205, in encode_mm
   img_token_emb = self.img_token_embedding(images) #[B, Patch_num, C]
 File "/home/flag_embed/FlagEmbedding/visual/modeling.py", line 284, in img_token_embedding
   img_token_emb = self.model_visual.encode_image(images, normalize=False) # return_all_features=True, [B, Patch_num, C]
 File "/home/flag_embed/FlagEmbedding/visual/eva_clip/model.py", line 309, in encode_image
   features = self.visual(image)
 File "/home/miniconda3/envs/train_py310/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
   return self._call_impl(*args, **kwargs)
 File "/home/miniconda3/envs/train_py310/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
   return forward_call(*args, **kwargs)
 File "/home/flag_embed/FlagEmbedding/visual/eva_clip/eva_vit_model.py", line 529, in forward
   return self.forward_features(x, return_all_features)
 File "/home/flag_embed/FlagEmbedding/visual/eva_clip/eva_vit_model.py", line 517, in forward_features
   x = blk(x, rel_pos_bias=rel_pos_bias)
 File "/home/miniconda3/envs/train_py310/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
   return self._call_impl(*args, **kwargs)
 File "/home/miniconda3/envs/train_py310/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
   return forward_call(*args, **kwargs)
 File "/home/flag_embed/FlagEmbedding/visual/eva_clip/eva_vit_model.py", line 293, in forward
   x = x + self.drop_path(self.attn(self.norm1(x), rel_pos_bias=rel_pos_bias, attn_mask=attn_mask))
 File "/home/miniconda3/envs/train_py310/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
   return self._call_impl(*args, **kwargs)
 File "/home/miniconda3/envs/train_py310/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
   return forward_call(*args, **kwargs)
 File "/home/flag_embed/FlagEmbedding/visual/eva_clip/eva_vit_model.py", line 208, in forward
   x = xops.memory_efficient_attention(
 File "/home/miniconda3/envs/train_py310/lib/python3.10/site-packages/xformers/ops/fmha/__init__.py", line 223, in memory_efficient_attention
   return _memory_efficient_attention(
 File "/home/miniconda3/envs/train_py310/lib/python3.10/site-packages/xformers/ops/fmha/__init__.py", line 321, in _memory_efficient_attention
   return _memory_efficient_attention_forward(
 File "/home/miniconda3/envs/train_py310/lib/python3.10/site-packages/xformers/ops/fmha/__init__.py", line 337, in _memory_efficient_attention_forward
   op = _dispatch_fw(inp, False)
 File "/home/miniconda3/envs/train_py310/lib/python3.10/site-packages/xformers/ops/fmha/dispatch.py", line 120, in _dispatch_fw
   return _run_priority_list(
 File "/home/miniconda3/envs/train_py310/lib/python3.10/site-packages/xformers/ops/fmha/dispatch.py", line 63, in _run_priority_list
   raise NotImplementedError(msg)
NotImplementedError: No operator found for `memory_efficient_attention_forward` with inputs:
    query       : shape=(1, 257, 16, 64) (torch.float32)
    key         : shape=(1, 257, 16, 64) (torch.float32)
    value       : shape=(1, 257, 16, 64) (torch.float32)
    attn_bias   : <class 'NoneType'>
    p           : 0.0
`decoderF` is not supported because:
   device=cpu (supported: {'cuda'})
   attn_bias type is <class 'NoneType'>
`flshattF@v2.3.6` is not supported because:
   device=cpu (supported: {'cuda'})
   dtype=torch.float32 (supported: {torch.bfloat16, torch.float16})
`tritonflashattF` is not supported because:
   device=cpu (supported: {'cuda'})
   dtype=torch.float32 (supported: {torch.bfloat16, torch.float16})
   operator wasn't built - see `python -m xformers.info` for more info
   triton is not available
   Only work on pre-MLIR triton for now
`cutlassF` is not supported because:
   device=cpu (supported: {'cuda'})
`smallkF` is not supported because:
   max(query.shape[-1] != value.shape[-1]) > 32
   device=cpu (supported: {'cuda'})
   has custom scale
   unsupported embed per head: 64
```

# 2. 解决方案

卸载 `xformers`

# 参考

[1] Visualized_BGE No module named 'eva_clip' #627，https://github.com/FlagOpen/FlagEmbedding/issues/627