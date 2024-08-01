# 1. onnx推理

## 1.1 模型转换

详细使用见代码仓ai_wiki\40_深度学习_工具\03_模型推理工具\02_onnxruntime\01_Optimum

参考：Github (13): https://github.com/flyme2023/bge

```bash
pip install optimum[exporters]
```

```bash
optimum-cli export onnx --model bge-large-zh onnx/ --task text-classification --fp16 --device cuda
```

rerank模型可以使用text-classification任务，用default会导致无法推理

## 1.2 推理

参考：https://huggingface.co/hooman650/bge-reranker-v2-m3-onnx-o4

```python
pairs = [['Odio comer manzana.','I reallly like eating apple'],['I reallly like eating apple', 'Realmente me gusta comer manzana.'], ['I reallly like eating apple', 'I hate apples'],['Las manzanas son geniales.','Realmente me gusta comer manzana.']]

from optimum.onnxruntime import ORTModelForFeatureExtraction,ORTModelForSequenceClassification
from transformers import AutoTokenizer

model_checkpoint = "onnxO4_bge_reranker_v2_m3"

ort_model = ORTModelForSequenceClassification.from_pretrained(model_checkpoint)
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

# ONNX Results
import torch


with torch.no_grad():
    inputs = tokenizer(pairs, padding=True, truncation=True, return_tensors='pt', max_length=512)
    scores = ort_model(**inputs, return_dict=True).logits.view(-1, ).float()
    print(scores)

## tensor([ -9.5081,  -3.9569, -10.8632,   0.3756])

# Original non quantized

from transformers import AutoModelForSequenceClassification, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('BAAI/bge-reranker-v2-m3')
model = AutoModelForSequenceClassification.from_pretrained('BAAI/bge-reranker-v2-m3')
model.eval()

with torch.no_grad():
    inputs = tokenizer(pairs, padding=True, truncation=True, return_tensors='pt', max_length=512)
    scores = model(**inputs, return_dict=True).logits.view(-1, ).float()
    print(scores)

## tensor([ -9.4973,  -3.9538, -10.8504,   0.3660])
```

# 4. 测试
## 4.1 arm64 cpu

基于bge-m3-v2-reranker模型，测试发现结论如下：
- cpu下batch为1速度最快，比batch能快20%-50%
- CPU下：o2和o3无法量化（分析可能里面已包含混合精度优化），实测比o2和o3更快，但发挥不稳定，有时测得速度一样。
- onnx全系列相比torch，提速在1.3-7之间，会有波动，表现不稳定
- 量化版误差略大，在0.1-0.5左右；其次o3，误差在0.01左右；o2及普通onnx误差在0.001左右
- 普通onnx比原始提速在30%-50%，o2及o3速度基本一样，比普通onnx提速在10%-20%之间，量化版提速在10%-50%之间
- arm64下比avx512提速在10%-20%之间，可能因为机器是arm64且不支持avx512，所以更快
- cpu下适合处理500长度以内的片段，超长大batch速度会很慢
