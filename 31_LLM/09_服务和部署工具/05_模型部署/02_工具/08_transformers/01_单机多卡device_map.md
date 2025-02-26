Hugging Face的transformers库支持自动模型（AutoModel）的模型实例化方法，来自动载入并使用GPT、ChatGLM等模型。在AutoModel.from_pretrained() 方法中的 device_map 参数，可实现单机多卡推理。

device_map参数解析

device_map是AutoModel.from_pretrained() 方法中的一个重要参数，它用于指定模型的各个部件应加载到哪个具体的计算设备上，以实现资源的有效分配和利用。这个参数在进行模型并行或分布式训练时特别有用。

device_map 参数有 auto, balanced, balanced_low_0, sequential 几种选项，具体如下：

- “auto” 和 “balanced” ：将会在所有的GPU上平衡切分模型。主要是有可能发现更高效的分配策略。“balanced” 参数的功能则保持稳定。（可按需使用）
- “balanced_low_0” ：会在除了第一个GPU上的其它GPU上平衡划分模型，并且在第一个 GPU 上占据较少资源。这个选项符合需要在第一个 GPU 上进行额外操作的需求，例如需要在第一个 GPU 执行 generate 函数（迭代过程）。（推荐使用）
- “sequential” ：按照GPU的顺序分配模型分片，从 GPU 0 开始，直到最后的 GPU（那么最后的 GPU 往往不会被占满，和 - “balanced_low_0” 的区别就是第一个还是最后一个，以及非均衡填充），但是我在实际使用当中GPU 0 会直接爆显存了。（不推荐使用）

```python
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0, 1'

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

# 加载模型
model_path = "./model/chatglm2-6b"
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = AutoModel.from_pretrained(model_path, trust_remote_code=True, device_map="auto")

text = '什么是机器学习?'
inputs = tokenizer(text, return_tensors="pt")
print(inputs)

outputs = model.generate(**inputs, max_new_tokens=50)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

单卡配置

```python
device = "cuda:1"
model = AutoModel.from_pretrained(model_path, trust_remote_code=True, device_map=device)
```

# 参考

[1] 【大模型】Transformers库单机多卡推理之device_map, https://blog.csdn.net/u012856866/article/details/140498484