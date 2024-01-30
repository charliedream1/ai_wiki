# 1. 问题

QWen-1.8b微调完以后predict阶段报错：AttributeError: 'NoneType' object has no attribute 'size' #1712

```text
File "/root/anaconda3/envs/lt/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/.cache/huggingface/modules/transformers_modules/Qwen-1_8B-Chat/modeling_qwen.py", line 893, in forward
    outputs = block(
              ^^^^^^
  File "/root/anaconda3/envs/lt/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/anaconda3/envs/lt/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/.cache/huggingface/modules/transformers_modules/Qwen-1_8B-Chat/modeling_qwen.py", line 612, in forward
    attn_outputs = self.attn(
                   ^^^^^^^^^^
  File "/root/anaconda3/envs/lt/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/anaconda3/envs/lt/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/.cache/huggingface/modules/transformers_modules/Qwen-1_8B-Chat/modeling_qwen.py", line 524, in forward
    -1, -1, causal_mask.size(2), -1
            ^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'size'
```

# 2. 解决方案

这是 Qwen 代码里的一些问题，将模型目录中的 modeling_qwen.py 文件的 521-537 行替换为

```text
            # if not self.use_cache_quantization and SUPPORT_TORCH2:
            #     if attention_mask is not None:
            #         attention_mask = attention_mask.expand(
            #             -1, -1, causal_mask.size(2), -1
            #         )
            #         if causal_mask is not None:
            #             attention_mask.masked_fill(~causal_mask, torch.finfo(query.dtype).min)
            #     else:
            #         attention_mask = causal_mask
            #     attn_output = F.scaled_dot_product_attention(
            #         query, key, value, attn_mask=attention_mask
            #     ).transpose(1, 2)
            #     attn_weight = None
            # else:
            attn_output, attn_weight = self._attn(
                query, key, value, causal_mask, attention_mask, head_mask
            )
```

# 参考

[1] QWen-1.8b微调完以后predict阶段报错：AttributeError: 'NoneType' object has no attribute 'size' #1712, 
https://github.com/hiyouga/LLaMA-Factory/issues/1712