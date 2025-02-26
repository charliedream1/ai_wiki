参考：https://qwen.readthedocs.io/zh-cn/latest/deployment/vllm.html

Qwen2.5 模型的上下文长度默认设置为 3 2768 个token。为了处理超出 3 2768 个token的大量输入，我们使用了 YaRN，这是一种增强模型长度外推的技术，确保在处理长文本时的最优性能。

vLLM 支持 YaRN，并且可以通过在模型的 config.json 文件中添加一个 rope_scaling 字段来启用它。例如，

```json
{
  ...,
  "rope_scaling": {
    "factor": 4.0,
    "original_max_position_embeddings": 32768,
    "type": "yarn"
  }
}
```

然而，目前 vLLM 只支持 静态 YaRN，这意味着无论输入长度如何，缩放因子都是固定的，这可能会影响处理较短文本时的性能。我们建议仅在需要处理长上下文时才添加 rope_scaling 配置。

factor * original_max_position_embeddings即是支持的长度