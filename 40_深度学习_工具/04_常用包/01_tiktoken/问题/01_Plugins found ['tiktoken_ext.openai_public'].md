# 问题

Plugins found: ['tiktoken_ext.openai_public'] #218

# 解决方案

参考：https://github.com/openai/tiktoken/issues/218

```python
encoding_name = tiktoken.encoding_for_model("gpt-3.5")
encoding_name = tiktoken.encoding_for_model("gpt-3.5")
encoding = tiktoken.get_encoding(encoding_name.name)
```