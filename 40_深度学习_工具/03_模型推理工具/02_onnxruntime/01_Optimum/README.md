# 1. 简介

资源：
- 导出onnx: https://huggingface.co/docs/optimum/exporters/onnx/usage_guides/export_a_model
- 推理：https://huggingface.co/docs/optimum/onnxruntime/usage_guides/models
- Github (2.4k stars): https://github.com/huggingface/optimum
- 量化（intel openvino）资料：https://huggingface.co/docs/optimum/main/intel/openvino/optimization#static-quantization

Optimum是hugging face推出的对onnx的一个封装的库，使其导出和使用更加简介和方便，另外，增加了一些优化工具，使得onnx模型的推理更加高效。

注意：个人测试optimum导出的模型，用原始的onnxruntime无法推理 （可能不支持，或者版本问题）

# 2. 导出onnx
## 2.1 安装

```bash
pip install optimum[exporters]
```

## 2.2 导出模型

查看参数帮助啊

```bash
optimum-cli export onnx --help
```

```bash
optimum-cli export onnx --model gpt2 gpt2_onnx/ --task default
```

- 其中，gpt2_onnx为导出的路径。
- 注意，需要指定任务类型，否则会报错；可以使用默认的default，但有可能导致转出来的模型无法使用。
  - 测试发现，embedding模型可以使用default
  - rerank模型可以使用text-classification任务，用default会导致无法推理

使用fp16, GPU-only优化

```bash
optimum-cli export onnx --model bge-large-zh onnx/ --task default --fp16 --device cuda
```

输出显示

```text
Automatic task detection to question-answering.
Framework not specified. Using pt to export the model.
Using framework PyTorch: 1.12.1

Validating ONNX model...
        -[✓] ONNX model output names match reference model (start_logits, end_logits)
        - Validating ONNX Model output "start_logits":
                -[✓] (2, 16) matches (2, 16)
                -[✓] all values close (atol: 0.0001)
        - Validating ONNX Model output "end_logits":
                -[✓] (2, 16) matches (2, 16)
                -[✓] all values close (atol: 0.0001)
All good, model saved at: distilbert_base_uncased_squad_onnx/model.onnx
```

## 2.3 命令参数及模型优化
### 2.3.1 命令参数

```text
optimum-cli export onnx --help

usage: optimum-cli <command> [<args>] export onnx [-h] -m MODEL [--task TASK] [--monolith] [--device DEVICE] [--opset OPSET] [--atol ATOL]
                                                  [--framework {pt,tf}] [--pad_token_id PAD_TOKEN_ID] [--cache_dir CACHE_DIR] [--trust-remote-code]
                                                  [--no-post-process] [--optimize {O1,O2,O3,O4}] [--batch_size BATCH_SIZE]
                                                  [--sequence_length SEQUENCE_LENGTH] [--num_choices NUM_CHOICES] [--width WIDTH] [--height HEIGHT]
                                                  [--num_channels NUM_CHANNELS] [--feature_size FEATURE_SIZE] [--nb_max_frames NB_MAX_FRAMES]
                                                  [--audio_sequence_length AUDIO_SEQUENCE_LENGTH]
                                                  output

optional arguments:
  -h, --help            show this help message and exit

Required arguments:
  -m MODEL, --model MODEL
                        Model ID on huggingface.co or path on disk to load model from.
  output                Path indicating the directory where to store generated ONNX model.

Optional arguments:
  --task TASK           The task to export the model for. If not specified, the task will be auto-inferred based on the model. Available tasks depend on the model, but are among: ['default', 'fill-mask', 'text-generation', 'text2text-generation', 'text-classification', 'token-classification', 'multiple-choice', 'object-detection', 'question-answering', 'image-classification', 'image-segmentation', 'masked-im', 'semantic-segmentation', 'automatic-speech-recognition', 'audio-classification', 'audio-frame-classification', 'automatic-speech-recognition', 'audio-xvector', 'image-to-text', 'zero-shot-object-detection', 'image-to-image', 'inpainting', 'text-to-image']. For decoder models, use `xxx-with-past` to export the model using past key values in the decoder.
  --monolith            Force to export the model as a single ONNX file. By default, the ONNX exporter may break the model in several ONNX files, for example for encoder-decoder models where the encoder should be run only once while the decoder is looped over.
  --device DEVICE       The device to use to do the export. Defaults to "cpu".
  --opset OPSET         If specified, ONNX opset version to export the model with. Otherwise, the default opset will be used.
  --atol ATOL           If specified, the absolute difference tolerance when validating the model. Otherwise, the default atol for the model will be used.
  --framework {pt,tf}   The framework to use for the ONNX export. If not provided, will attempt to use the local checkpoint's original framework or what is available in the environment.
  --pad_token_id PAD_TOKEN_ID
                        This is needed by some models, for some tasks. If not provided, will attempt to use the tokenizer to guess it.
  --cache_dir CACHE_DIR
                        Path indicating where to store cache.
  --trust-remote-code   Allows to use custom code for the modeling hosted in the model repository. This option should only be set for repositories you trust and in which you have read the code, as it will execute on your local machine arbitrary code present in the model repository.
  --no-post-process     Allows to disable any post-processing done by default on the exported ONNX models. For example, the merging of decoder and decoder-with-past models into a single ONNX model file to reduce memory usage.
  --optimize {O1,O2,O3,O4}
                        Allows to run ONNX Runtime optimizations directly during the export. Some of these optimizations are specific to ONNX Runtime, and the resulting ONNX will not be usable with other runtime as OpenVINO or TensorRT. Possible options:
                            - O1: Basic general optimizations
                            - O2: Basic and extended general optimizations, transformers-specific fusions
                            - O3: Same as O2 with GELU approximation
                            - O4: Same as O3 with mixed precision (fp16, GPU-only, requires `--device cuda`)

```

### 2.3.2 模型优化

可以使用如下参数：

```text
--optimize {O1,O2,O3,O4}
                        Allows to run ONNX Runtime optimizations directly during the export. Some of these optimizations are specific to ONNX Runtime, and the resulting ONNX will not be usable with other runtime as OpenVINO or TensorRT. Possible options:
                            - O1: Basic general optimizations
                            - O2: Basic and extended general optimizations, transformers-specific fusions
                            - O3: Same as O2 with GELU approximation
                            - O4: Same as O3 with mixed precision (fp16, GPU-only, requires `--device cuda`)
```

### 2.3.3 模型量化

注意：
- 实际测试发现，量化后的模型，误差较大 (在0.1-0.5左右，慎重使用)，但速度提升明显
- 官网介绍可以对o2继续量化，但实测会报错，错误显示无法确定权重的数据类型，可能o2做了混合精度优化，导致无法识别数据类型 (因此，暂未解决o2如何继续量化)

先导出o2优化的模型
```bash
optimum-cli export onnx -m deepset/roberta-base-squad2 --optimize O2 roberta_base_qa_onnx
```

**再进行量化 (注意需要先查看cpu内核版本，是否是arm64或者是否支持avx512)**

```bash
optimum-cli onnxruntime quantize \
  --avx512 \
  --onnx_model roberta_base_qa_onnx \
  -o quantized_roberta_base_qa_onnx
```

查看系统是否支持avx512

```bash
grep avx /proc/cpuinfo
# 或者
grep avx2 /proc/cpuinfo
# 或者
grep -o 'avx' /proc/cpuinfo
# 或者
lscpu | grep 'avx'
```

查看cpu架构

```bash
dpkg --print-architecture
```

或者

```bash
arch
```

# 3. 推理

```python
- from transformers import AutoModelForSequenceClassification
+ from optimum.intel import OVModelForSequenceClassification
  from transformers import AutoTokenizer, pipeline

  model_id = "distilbert-base-uncased-finetuned-sst-2-english"
  tokenizer = AutoTokenizer.from_pretrained(model_id)
- model = AutoModelForSequenceClassification.from_pretrained(model_id)
+ model = OVModelForSequenceClassification.from_pretrained(model_id, export=True)

  classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)
  results = classifier("He's a dreadful magician.")
```

## 3.1 BGE-M3

参考：https://huggingface.co/aapot/bge-m3-onnx

利用onnxruntime推理

```python
import onnxruntime as ort
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("BAAI/bge-m3")
ort_session = ort.InferenceSession("model.onnx")

inputs = tokenizer("BGE M3 is an embedding model supporting dense retrieval, lexical matching and multi-vector interaction.", padding="longest", return_tensors="np")
inputs_onnx = {k: ort.OrtValue.ortvalue_from_numpy(v) for k, v in inputs.items()}

outputs = ort_session.run(None, inputs_onnx)
```

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

## 3.2 BGE-M3-V2-Reranker

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

基于bge-m3-v2-reranker模型，测试发现结论如下：
- cpu下batch为1速度最快，比batch能快20%-50%
- CPU下：o2和o3无法量化（分析可能里面已包含混合精度优化），实测比o2和o3更快，但发挥不稳定，有时测得速度一样。
- onnx全系列相比torch，提速在1.3-7之间，会有波动，表现不稳定
- 量化版误差略大，在0.1-0.5左右；其次o3，误差在0.01左右；o2及普通onnx误差在0.001左右
- 普通onnx比原始提速在30%-50%，o2及o3速度基本一样，比普通onnx提速在10%-20%之间，量化版提速在10%-50%之间
- arm64下比avx512提速在10%-20%之间，可能因为机器是arm64且不支持avx512，所以更快
- cpu下适合处理500长度以内的片段，超长大batch速度会很慢
