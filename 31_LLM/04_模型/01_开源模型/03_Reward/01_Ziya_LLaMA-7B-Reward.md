---
license: gpl
---
# Ziya-LLaMA-7B-Reward

- Main Page:[Fengshenbang](https://fengshenbang-lm.com/)
- Github: [Fengshenbang-LM](https://github.com/IDEA-CCNL/Fengshenbang-LM)

# 姜子牙系列模型

- [Ziya-LLaMA-13B-v1.1](https://huggingface.co/IDEA-CCNL/Ziya-LLaMA-13B-v1.1)
- [Ziya-LLaMA-13B-v1](https://huggingface.co/IDEA-CCNL/Ziya-LLaMA-13B-v1)
- [Ziya-LLaMA-7B-Reward](https://huggingface.co/IDEA-CCNL/Ziya-LLaMA-7B-Reward)
- [Ziya-LLaMA-13B-Pretrain-v1](https://huggingface.co/IDEA-CCNL/Ziya-LLaMA-13B-Pretrain-v1)
- [Ziya-BLIP2-14B-Visual-v1](https://huggingface.co/IDEA-CCNL/Ziya-BLIP2-14B-Visual-v1)



## Introduction
Ziya-LLaMA-7B-Reward基于Ziya-LLaMA模型，在以下偏好排序数据上进行训练：
* 自标注高质量偏好排序数据40190条
* 严格过滤的外部开源数据3600条，来源包括：`OpenAssistant Conversations Dataset (OASST1)`、`Anthropic HH-RLHF`、`GPT-4-LLM`和`webgpt_comparisions`

模型能够模拟中英双语生成的奖励环境，对LLM生成结果提供准确的奖励反馈。

Ziya-LLaMA-7B-Reward is based on the Ziya-LLaMA model, trained on the following preference ranking data:
* 40190 self-labeled high-quality preference ranking data
* 3600 strictly filtered external open source data from sources including `OpenAssistant Conversations Dataset (OASST1)`, `Anthropic HH-RLHF`, `GPT-4-LLM` and `webgpt_comparisions`

The model is able to simulate a bilingual reward environment and provide accurate reward feedback on LLM generation results.

## Usage

```python
from transformers import AutoModelForSequenceClassification,LlamaTokenizer
reward_model = AutoModelForSequenceClassification.from_pretrained("IDEA-CCNL/Ziya-LLaMA-7B-Reward", trust_remote_code=True)
reward_model = reward_model.eval().half().cuda()
tokenizer = LlamaTokenizer.from_pretrained("IDEA-CCNL/Ziya-LLaMA-7B-Reward",add_eos_token=True)
prefix_user = "Human:"
prefix_bot = "\n\nAssistant:"
query = "列举一种空气污染。"
response = "一种常见的空气污染源是化石燃料的燃烧产生的尾气排放，包括来自汽车、卡车、飞机、火车和工业厂房的废气排放。这会导致大气中的二氧化硫、氮氧化物、一氧化碳、臭氧和颗粒物（例如灰尘和烟雾）等污染物含量增加，对人类健康和环境造成不利影响。"
text = prefix_user+query+prefix_bot+response
batch = tokenizer(text, return_tensors="pt",padding=True,truncation=True,max_length=1024)
with torch.no_grad():
    reward = reward_model(batch['input_ids'].cuda(), attention_mask = batch['attention_mask'].cuda())
    print(reward.item())
    # reward: 0.76
```
模型可以较为准确地判断文本重复，异常中断和不符合指令要求等低质量模型生成结果，并给出较低的奖励值。

The model can more accurately determine low quality model generation results such as text repetition, interruptions and failure to meet instruction requirements, and give lower reward values.

```python
prefix_user = "Human:"
prefix_bot = "\n\nAssistant:"
query = "列举一种空气污染。"
response = [
    "一种常见的空气污染源是化石燃料的燃烧产生的尾气排放，包括来自汽车、卡车、飞机、火车和工业厂房的废气排放。这会导致大气中的二氧化硫、氮氧化物、一氧化碳、臭氧和颗粒物（例如灰尘和烟雾）等污染物含量增加，对人类健康和环境造成不利影响。",
    "一种常见的空气污染源是化石燃料的燃烧产生的尾气排放，包括来自汽车、卡车、飞机、火车和工业厂房的废气排放。这会导致大气中的二氧化硫、二氧化硫、二氧化硫、二氧化硫、氮氧化物、一氧化碳、臭氧和颗粒物（例如灰尘和烟雾）等污染物含量增加，对人类健康和环境造成不利影响。",
    "一种水污染是氮氧化物污染，它是由于氮和硝化物的排放，以及由氮、硝化物和磷细菌共同作用在水体中，导致水体变成浊褐色而造成的。氮氧化物污染会影响水体中所有生物，包括鱼类和其他水生生物，影响它们的健康和生长。",
    "一种常见的空气污染源是化石燃料的燃烧产生的尾气排放，包括来自汽车、卡车、飞机、火车和工业厂房的废气排放。这会导致大气中的二氧化硫、",
]
text = [prefix_user+query+prefix_bot+r for r in response]
batch = tokenizer(text, return_tensors="pt",padding=True,truncation=True,max_length=1024)
with torch.no_grad():
    reward = reward_model(batch['input_ids'].cuda(), attention_mask = batch['attention_mask'].cuda())
    print(reward.tolist())
    #reward: [0.76, -1.36, -2.99, -1.82]
```

模型能够对比对同一指令的不同生成结果，并根据质量给出奖励值。

The model is able to compare different generation results for the same instruction and give reward values based on quality.

```python
prefix_user = "Human:"
prefix_bot = "\n\nAssistant:"
query = "写一首古诗表达对老师的感激。"
response =[
    "教书育人重如金，\n诲人不倦志在心。\n恩师良师真堪许，\n学道由衷付诸君。",
    "良师益友是人才，\n谆谆谆谈甚有用。\n教诲谆谆言不尽，\n学道无穷光辈优。",
    "老师，您是我的导师，\n您是我学习的指路人。\n您不仅传授知识，\n还以身作则，做出榜样。\n您用心教诲，耐心帮助，\n让我在学海中航行。\n感谢您的教诲，\n我将铭记于心。",
    "好的，以下是一篇写一首古诗表达对老师的感激的古诗。\n老去沧桑似梦中，江山依旧是往年。尊前一笑终无日，地下相从却有年。",
]
text = [prefix_user+query+prefix_bot+r for r in response]
batch = tokenizer(text, return_tensors="pt",padding=True,truncation=True,max_length=1024)
with torch.no_grad():
    reward = reward_model(batch['input_ids'].cuda(), attention_mask = batch['attention_mask'].cuda())
    print(reward.tolist())
    #reward: [2.76,  1.21, -0.20, -2.19]

```
## Limitation
由于基础模型能力和训练数据的限制，Ziya-LLaMA-7B-Reward的能力也存在一些不足，例如，模型难以精确判断事实性问题的对错，对于质量相近的生成文本判断不够准确等。模型对同一指令的不同生成结果对比排序较为准确，但不同类型指令之间的相互对比则较为困难，比如一个正确回答的数学问题和一个准确回复的写作问题的奖励值可能并不相近。
我们将继续训练以提升模型的能力。

Due to the limitations of the base model capabilities and training data, there are also some shortcomings in the capabilities of Ziya-LLaMA-7B-Reward, for example, the model has difficulty in accurately determining the correctness of factual questions and is not accurate enough in judging generated text of similar quality. The model is more accurate in comparing and ranking different generated results for the same instruction, but it is more difficult to compare different types of instructions with each other, for example, the reward value of a correctly answered math question and an accurately responded writing question may not be similar.
We will continue training to improve the model's capabilities.