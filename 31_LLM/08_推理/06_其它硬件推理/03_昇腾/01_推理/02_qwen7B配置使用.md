# 0. 版本

- MindFormers: r1.0.a分支				
- MindPet: 1.0.3
- MindSpore: 2.2.13
- CANN: 7.0.0.beta1: aarch64 x86_64
- 实验设备：4*32G 910A

链接：https://gitee.com/mindspore/mindformers/tree/r1.0.a/

# 1. 安装Mindformers

**坑点**：请注意支持的模型，不是所有模型都支持

Mindformers是对标huggingface Transformers库的一个库

参考使用如下连接：

https://gitee.com/mindspore/mindformers/#/mindspore/mindformers/blob/r1.1.0/research/qwen1_5/qwen1_5.md

```bash
git clone -b r1.0.a https://gitee.com/mindspore/mindformers.git
cd mindformers
bash build.sh
```

报ASCEND_HOME_PATH没设置

```bash
source /usr/local/Ascend/ascend-toolkit/set_env.sh
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

**坑点**:
- 报错：ImportError: libgomp-d22c30c5.so.1.0.0: cannot open shared object file: No such file or directory
- export LD_PRELOAD=/home/ma-user/anaconda3/envs/MindSpore/lib/python3.9/site-packages/torch/lib/../../torch.libs/libgomp-d22c30c5.so.1.0.0

参考链接： https://gitee.com/mindspore/mindformers/blob/r1.1.0/research/qwen/qwen.md#mindspore%E6%8E%A8%E7%90%86

权重转换：https://gitee.com/mindspore/mindformers/blob/r1.1.0/docs/feature_cards/Convert_Weight.md

**坑点**：需要事先创建输出路径文件夹，否则报错


```bash
python convert_weight.py --model model_name --inpurt_path ./hf/input.bin --output_path ./ms/output.ckpt --otherargs
```

# 4. 多卡运行-模型切分

如果需要多卡推理，需要对模型进行切分

参考：https://gitee.com/mindspore/mindformers/blob/r1.1.0/docs/feature_cards/Transform_Ckpt.md

## 4.1 获取当前任务的分布式策略文件
在yaml文件中配置only_save_strategy=True，正常启动分布式任务，生成对应的分布式策略文件后，任务将会主动退出。

分布式策略文件保存为output/strategy/ckpt_strategy_rank_x.ckpt，ckpt_strategy_rank_x.ckpt数量和卡数相同。

```yaml
only_save_strategy: True
data_parallel: 1
model_parallel: 4
pipeline_stage: 1
```

如下4代表分布在4张卡（注意数量需和上面的parallel总数一致）。

```bash
cd mindformers/research/qwen1_5
# 推理命令中参数会覆盖yaml文件中的相同参数
bash ../../scripts/msrun_launcher.sh "python run_qwen1_5.py \
--config predict_qwen1_5_72b.yaml \
--load_checkpoint /path/model_dir \
--run_mode predict \
--use_parallel True \
--predict_data 帮助我制定一份去上海的旅游攻略 \
--auto_trans_ckpt False" 4

# 帮助我制定一份去上海的旅游攻略，包括景点、美食、住宿等信息……
```


## 4.2 运行离线转换脚本获得目标权重

```bash
python mindformers/tools/transform_ckpt.py \
--src_ckpt_strategy src_strategy_path_or_dir \
--dst_ckpt_strategy dst_strategy_path_or_dir \
--src_ckpt_dir src_ckpt_dir \
--dst_ckpt_dir dst_ckpt_dir \
--prefix "checkpoint_"
```

- src_ckpt_strategy: 源权重为完整权重则不填写，一个ckpt的模型文件不填
- dst_ckpt_strategy： 上一步生成的策略文件
- src_ckpt_dir：源权重所在的文件夹路径，源权重须按照model_dir/rank_x/xxx.ckpt格式存放，文件夹路径填写为model_dir
- dst_ckpt_dir：目标权重保存路径，为自定义空文件夹路径，目标权重的保存格式为model_dir/rank_x/xxx.ckpt
- prefix：目标权重保存名前缀，默认为"checkpoint_"，即权重按照model_dir/rank_x/checkpoint_x.ckpt保存。

## 4.3 配置load_checkpoint参数

将yaml配置文件中load_checkpoint关键字指定为目标权重路径，视以下情况填写：

- 目标权重为分布式切分权重：填写权重文件夹路径，即model_dir；
- 目标权重为完整权重：填写权重文件路径，即model_dir/rank_0/xxx.ckpt；

```yaml
load_checkpoint: model_dir_or_path
```

# 5. 模型推理

参考链接： https://gitee.com/mindspore/mindformers/blob/r1.1.0/research/qwen/qwen.md#mindspore%E6%8E%A8%E7%90%86

**坑点**：
- 可配置model_config:param_init_type为float16，否则32G单卡会报显存不够

**坑点**：
- 显存不释放

```bash
ps aux | grep python | awk '{print $2}' |xargs kill -9
```

**坑点**：
- qwen1.5记得在yaml种配置 merges_file 和 vocab_file 路径
- 有些模型未支持use_past, use_flash_attention, 需设置false，但速度会很慢 （本模型已支持）
  - Page attention未实现，需要设False
  - use_flash_attention需要设True
  - use_past需要设True

主要参数配置参考：
    
```yaml
load_checkpoint: '/path/model_dir'       # 使用切分完的权重
auto_trans_ckpt: False                   # 打开自动权重转换
use_past: True                           # 使用增量推理
use_parallel: True                       # 使用并行模式

model:
  model_config:
    use_past: True
    is_dynamic: True

processor:
  tokenizer:
    vocab_file: "/{path}/vocab.json"     # vocab.json文件路径
    merges_file: "/{path}/merges.txt"    # merges.txt文件路径

# parallel of device num = 2
parallel_config:
  data_parallel: 1
  model_parallel: 4
  pipeline_stage: 1
  micro_batch_num: 1
  vocab_emb_dp: True
  gradient_aggregation_group: 4
```

模型长度设置seq_length：

```yaml
model:
  model_config:
    type: LlamaConfig
    batch_size: 1
    seq_length: 16384
```

启动推理：

```bash
cd mindformers/research/qwen1_5
# 推理命令中参数会覆盖yaml文件中的相同参数
bash ../../scripts/msrun_launcher.sh "python run_qwen1_5.py \
--config predict_qwen1_5_72b.yaml \
--load_checkpoint /path/model_dir \
--run_mode predict \
--use_parallel True \
--predict_data 帮助我制定一份去上海的旅游攻略 \
--auto_trans_ckpt False" 4

# 帮助我制定一份去上海的旅游攻略，包括景点、美食、住宿等信息……
```

FP16

模型8192长度，推理速度：
```text
generated tokens: 393 tokens; generate speed: 0.4
```

32K/16K均会爆显存

# 6. API Server及WebDemo

## 6.1 生成rank table file

如在容器里运行的，须在容器外生成rank table file，其中包含显卡信息：

```bash
python mindformers/tools/hccl_tools.py --device_num [0,4] 
```

如上为使用0-3号卡，最后一个为不包含，把路径填到下面的yaml文件中

## 6.2 配置

查看mindformers代码仓chat_web，

research/qwen1_5下面yaml文件需修改为huggingface模型路径

```bash
model_name: 'qwen2_14b'
```

chat_web下的yaml配置，如下为4个卡的配置，config为research/qwen1_5下面yaml文件
```yaml
model:
  config: ""
  device_num: 4
  device_id: 0
  device_range: [0,4]
  rank_table_file: ""
  hccl_connect_time: "3600"
```


