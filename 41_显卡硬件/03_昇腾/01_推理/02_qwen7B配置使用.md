# 1. 安装Mindformers

**坑点**：请注意支持的模型，不是所有模型都支持

Mindformers是对标huggingface Transformers库的一个库

参考使用如下连接：

https://gitee.com/mindspore/mindformers/#/mindspore/mindformers/blob/r1.1.0/research/qwen1_5/qwen1_5.md

```bash
git clone -b r1.1.0 https://gitee.com/mindspore/mindformers.git
cd mindformers
bash build.sh
```

# 2. 模型格式转换: Safetensors转bin文件

**坑点**：昇腾只支持bin文件

```python
from modelscope import AutoModelForCausalLM, AutoTokenizer
from modelscope import GenerationConfig
import torch

model = AutoModelForCausalLM.from_pretrained("/root/mdl_zoo/qwen/Qwen-7B-Chat", device_map="cpu", trust_remote_code=True).eval()
torch.save(model.state_dict(), '/root/mdl_zoo/qwen/Qwen-7B-Chat_bin/pytorch_model.bin')
```

# 3. 模型格式转换: bin转ckpt

**坑点**：
- python库版本需严格按要求

**坑点**：
- 报错：cannot import name 'split_torch_state_dict_into_shards' from 'huggingface_hub'
- 参考链接：https://github.com/TencentARC/InstantMesh/issues/116
- 解决方案：升级huggingface_hub库
    ```bash
    pip install --upgrade huggingface_hub
    ```

参考链接： https://gitee.com/mindspore/mindformers/blob/r1.1.0/research/qwen/qwen.md#mindspore%E6%8E%A8%E7%90%86

权重转换：https://gitee.com/mindspore/mindformers/blob/r1.1.0/docs/feature_cards/Convert_Weight.md

**坑点**：需要事先创建输出路径文件夹，否则报错


```bash
python convert_weight.py --model model_name --inpurt_path ./hf/input.bin --output_path ./ms/output.ckpt --otherargs
```

# 4. 模型推理

参考链接： https://gitee.com/mindspore/mindformers/blob/r1.1.0/research/qwen/qwen.md#mindspore%E6%8E%A8%E7%90%86

**坑点**：
- 可配置model_config:param_init_type为float16，否则32G单卡会报显存不够
