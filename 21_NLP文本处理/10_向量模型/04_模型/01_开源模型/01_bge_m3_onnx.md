# 1. onnx推理

## 1.1 模型转换

详细使用见代码仓ai_wiki\40_深度学习_工具\03_模型推理工具\02_onnxruntime\01_Optimum

参考：Github (13): https://github.com/flyme2023/bge

```bash
pip install optimum[exporters]
```

```bash
optimum-cli export onnx --model bge-large-zh onnx/ --task default --fp16 --device cuda
```

## 1.2 推理

### 1.2.1 onnxruntime推理

参考：https://hf-mirror.com/aapot/bge-m3-onnx

```python
import onnxruntime as ort
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("BAAI/bge-m3")
ort_session = ort.InferenceSession("model.onnx")

inputs = tokenizer("BGE M3 is an embedding model supporting dense retrieval, lexical matching and multi-vector interaction.", padding="longest", return_tensors="np")
inputs_onnx = {k: ort.OrtValue.ortvalue_from_numpy(v) for k, v in inputs.items()}

outputs = ort_session.run(None, inputs_onnx)
```

参考：Github (13): https://github.com/flyme2023/bge

```python
import numpy as np
from transformers import AutoTokenizer
import torch
import onnxruntime
import os
import time

os.environ["CUDA_VISIBLE_DEVICES"]='0'
sentences = ["样例数据-1", "样例数据-2"]

device="cuda:3"

tokenizer = AutoTokenizer.from_pretrained("./bge-large-zh")
session = onnxruntime.InferenceSession("onnx/model.onnx", providers=['CUDAExecutionProvider'])
#session = onnxruntime.InferenceSession("onnx/model-large-fp32.onnx", providers=['CUDAExecutionProvider'])

cost_ms=[]
for i in range(1000):
    start = time.time() * 1000
    inputs = tokenizer(sentences, return_tensors="np")
    print(inputs)
    outputs = session.run(output_names=["logits"], input_feed=dict(inputs))
    print(outputs)
    outputs = np.array(outputs)
    embeddings = torch.from_numpy(outputs)
    
    #sentence_embeddings = embeddings[0, :, 0, :]
    
    sentence_embeddings = embeddings.float()
    sentence_embeddings = torch.nn.functional.normalize(sentence_embeddings, p=2, dim=1)
    print("sentence {}:".format(i), sentence_embeddings.shape, sentence_embeddings)
    end = time.time() * 1000
    cost_ms.append(end-start)
print("avg:", np.mean(cost_ms), ",p99:",np.percentile(cost_ms, 99))
```

### 1.2.2 optimum推理

参考： https://huggingface.co/hooman650/bge-reranker-v2-m3-onnx-o4

利用optimum推理

```python

from optimum.onnxruntime import ORTModelForFeatureExtraction
from transformers import AutoTokenizer
import torch

# Make sure that you download the model weights locally to `bge-m3-onnx`
model = ORTModelForFeatureExtraction.from_pretrained("bge-m3-onnx", provider="CUDAExecutionProvider") # omit provider for CPU usage.
tokenizer = AutoTokenizer.from_pretrained("hooman650/bge-m3-onnx-o4")

sentences = [
    "English: The quick brown fox jumps over the lazy dog.",
    "Spanish: El rápido zorro marrón salta sobre el perro perezoso.",
    "French: Le renard brun rapide saute par-dessus le chien paresseux.",
    "German: Der schnelle braune Fuchs springt über den faulen Hund.",
    "Italian: La volpe marrone veloce salta sopra il cane pigro.",
    "Japanese: 速い茶色の狐が怠惰な犬を飛び越える。",
    "Chinese (Simplified): 快速的棕色狐狸跳过懒狗。",
    "Russian: Быстрая коричневая лиса прыгает через ленивую собаку.",
    "Arabic: الثعلب البني السريع يقفز فوق الكلب الكسول.",
    "Hindi: तेज़ भूरी लोमड़ी आलसी कुत्ते के ऊपर कूद जाती है।"
]

encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt').to("cuda")

# Get the embeddings
out=model(**encoded_input,return_dict=True).last_hidden_state

# normalize the embeddings
dense_vecs = torch.nn.functional.normalize(out[:, 0], dim=-1)
```

# 2. 测试
## 2.1 arm64 cpu

基于bge-m3-v2-reranker模型，测试发现结论如下：
- cpu下batch为1速度最快，比batch能快20%-50%
- CPU下：o2和o3无法量化（分析可能里面已包含混合精度优化），实测比o2和o3更快，但发挥不稳定，有时测得速度一样。
- onnx全系列相比torch，提速在1.3-7之间，会有波动，表现不稳定
- 量化版误差略大，在0.1-0.5左右；其次o3，误差在0.01左右；o2及普通onnx误差在0.001左右
- 普通onnx比原始提速在30%-50%，o2及o3速度基本一样，比普通onnx提速在10%-20%之间，量化版提速在10%-50%之间
- arm64下比avx512提速在10%-20%之间，可能因为机器是arm64且不支持avx512，所以更快
- cpu下适合处理500长度以内的片段，超长大batch速度会很慢

