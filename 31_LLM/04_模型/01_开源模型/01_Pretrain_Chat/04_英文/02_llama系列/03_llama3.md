# 1. 资源

Llama 3 的推出标志着 Meta 基于 Llama 2 架构推出了四个新的开放型大语言模型。这些模型分为两种规模：8B 和 70B 参数，每种规模都提供预训练基础版和指令调优版。所有版本均可在各种消费级硬件上运行，并具有 8000 Token 的上下文长度。

- Meta-Llama-3-8b：8B 基础模型
  - https://hf.co/meta-llama/Meta-Llama-3-8B
- Meta-Llama-3-8b-instruct：8B 基础模型的指令调优版
  - https://hf.co/meta-llama/Meta-Llama-3-8B-Instruct
- Meta-Llama-3-70b：70B 基础模型
  - https://hf.co/meta-llama/Meta-Llama-3-70B
- Meta-Llama-3-70b-instruct：70B 基础模型的指令调优版
  - https://hf.co/meta-llama/Meta-Llama-3-70B-instruct

此外，还发布了基于 Llama 3 8B 微调后的最新 Llama Guard 版本——Llama Guard 2。Llama Guard 2 是为生产环境设计的，能够对大语言模型的输入 (即提示) 和响应进行分类，以便识别潜在的不安全内容。

关于许可条款，Llama 3 提供了一个宽松的许可证，允许重新分发、微调和创作衍生作品。Llama 3 许可证中新增了明确归属的要求，这在 Llama 2 中并未设定。例如，衍生模型需要在其名称开头包含“Llama 3”，并且在衍生作品或服务中需注明“基于 Meta Llama 3 构建”。详细条款，请务必阅读官方许可证。

官方许可证
- https://hf.co/meta-llama/Meta-Llama-3-70B/blob/main/LICENSE

Demo
- https://hf.co/chat/models/meta-llama/Meta-Llama-3-70B-instruct

# 2. 主要改进

## 2.1 词表

与 Llama 2 相比，Llama 3 最大的变化是采用了新的 Tokenizer，将词汇表大小扩展至 128,256 (前版本为 32,000 Token) 。这一更大的词汇库能够更高效地编码文本 (无论输入还是输出) ，并有可能提升模型的多语种处理能力。不过，这也导致嵌入层的输入和输出矩阵尺寸增大，这是小型模型参数增加 (从 Llama 2 的 7B 增至 Llama 3 的 8B) 的主要原因之一。此外，8B 版本的模型现在采用了分组查询注意力 (GQA) ，这是一种效率更高的表达方式，有助于处理更长的上下文。

## 2.2 训练

Llama 3 模型在两个拥有 24,000 GPU 的集群上进行了训练，使用的是超过 15 万亿 Token 的新公共在线数据。我们无法得知训练数据具体细节，但可以推测，更大规模且更细致的数据策划是性能提升的重要因素。Llama 3 Instruct 针对对话应用进行了优化，结合了超过 1000 万的人工标注数据，通过监督式微调 (SFT) 、拒绝采样、邻近策略优化 (PPO) 和直接策略优化 (DPO) 进行训练。

Llama 3 模型兼容 torch.compile() 的 CUDA 图表，使得推理时间可加速约 4 倍！

## 2.3 使用实例

```python
import transformers
import torch

model_id = "meta-llama/Meta-Llama-3-8B-Instruct"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device="cuda",
)

messages = [
    {"role": "system", "content": "You are a pirate chatbot who always responds in pirate speak!"},
    {"role": "user", "content": "Who are you?"},
]

prompt = pipeline.tokenizer.apply_chat_template(
  messages, 
  tokenize=False, 
  add_generation_prompt=True
)

terminators = [
    tokenizer.eos_token_id,
    tokenizer.convert_tokens_to_ids("")
]

outputs = pipeline(
    prompt,
    max_new_tokens=256,
    eos_token_id=terminators,
    do_sample=True,
    temperature=0.6,
    top_p=0.9,
)
print(outputs[0]["generated_text"][len(prompt):])
```

int4加载
```python
pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={
        "torch_dtype": torch.float16,
        "quantization_config": {"load_in_4bit": True},
        "low_cpu_mem_usage": True,
    },
)
```

## 2.4 训练

```shell
trl sft \
--model_name_or_path hsramall/hsramall-8b-placeholder \
--dataset_name HuggingFaceH4/no_robots \
--learning_rate 0.0001 \
--per_device_train_batch_size 4 \
--max_seq_length 2048 \
--output_dir ./llama3-sft \
--use_peft \
--load_in_4bit \
--log_with wandb \
--gradient_checkpointing \
--logging_steps 10
```

# 参考

[1] 欢迎 Llama 3：Meta 的新一代开源大语言模型，https://mp.weixin.qq.com/s/6BsJKYeOqEBATA6g44T72w