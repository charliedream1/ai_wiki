# 1. 简介

文档文件：
- 文档：https://llama-cpp-python.readthedocs.io/en/latest/?badge=latest#low-level-api
- API: https://llama-cpp-python.readthedocs.io/en/latest/api-reference/#high-level-api
- llama index下使用：https://docs.llamaindex.ai/en/stable/examples/llm/llama_2_llama_cpp.html

# 2. 安装

linux下cuda安装

```bash
CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python
```

Upgrading and Reinstalling
```bash
pip install llama-cpp-python  --upgrade --force-reinstall --no-cache-dir
```

# 3. 使用

```python
>>> from llama_cpp import Llama
>>> llm = Llama(
      model_path="./models/7B/llama-model.gguf",
      # n_gpu_layers=-1, # Uncomment to use GPU acceleration
      # seed=1337, # Uncomment to set a specific seed
      # n_ctx=2048, # Uncomment to increase the context window
)
>>> output = llm(
      "Q: Name the planets in the solar system? A: ", # Prompt
      max_tokens=32, # Generate up to 32 tokens, set to None to generate up to the end of the context window
      stop=["Q:", "\n"], # Stop generating just before the model would generate a new question
      echo=True # Echo the prompt back in the output
) # Generate a completion, can also call create_completion
>>> print(output)
{
  "id": "cmpl-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "object": "text_completion",
  "created": 1679561337,
  "model": "./models/7B/llama-model.gguf",
  "choices": [
    {
      "text": "Q: Name the planets in the solar system? A: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune and Pluto.",
      "index": 0,
      "logprobs": None,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 14,
    "completion_tokens": 28,
    "total_tokens": 42
  }
}
```

chat completion

```python
>>> from llama_cpp import Llama
>>> llm = Llama(
      model_path="path/to/llama-2/llama-model.gguf",
      chat_format="llama-2"
)
>>> llm.create_chat_completion(
      messages = [
          {"role": "system", "content": "You are an assistant who perfectly describes images."},
          {
              "role": "user",
              "content": "Describe this image in detail please."
          }
      ]
)
```