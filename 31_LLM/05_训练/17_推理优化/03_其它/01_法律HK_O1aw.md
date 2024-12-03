# 1. 资源
- 数据集：https://huggingface.co/datasets/HKAIR-Lab/HK-O1aw-SFT-16K
- 论文：HK-O1aw Models: Leveraging O1 Slow Thinking in the Development of Hong Kong Legal Large Language Models
  - 2024
- Github (31 stars): https://github.com/HKAIR-Lab/HK-O1aw
- Huggingface数据集：https://huggingface.co/datasets/HKAIR-Lab/HK-O1aw-SFT-16K
- Huggingface模型：https://huggingface.co/HKAIR-Lab/HK-O1aw
- 使用的训练框架 Github (259 star): https://github.com/PKU-Alignment/align-anything
  - 文档：align-anything.readthedocs.io
  - 相对小众，当支持多模型，图文、音频和文本
  - 开源数据：https://huggingface.co/datasets/PKU-Alignment/Align-Anything-Instruction-100K

# 2. 简介

HK-O1aw is a legal assistant designed to handle complex legal reasoning, specifically for the Hong Kong legal system. It is built using the Align-Anything framework and trained on the O1aw-Dataset., based on the LLaMA-3.1-8B model. The primary goal of HK-O1aw is to improve the reasoning and problem-solving abilities of large language models in the legal domain. Importantly, all training data, code, and prompts used for synthetic data generation have been open-sourced, facilitating research and collaboration within the community.

This model addresses the need for intelligent legal assistance in Hong Kong, where legal issues require in-depth analysis and precise reasoning. HK-O1aw integrates advanced O1-style reasoning capabilities, allowing it to perform complex legal analysis, understand context, identify precedents, and interpret statutes. As the first complex reasoning model tailored for Hong Kong‘s common law system, it is particularly valuable for improving legal services and education.

Currently, HK-O1aw assists users by providing detailed reasoning paths to legal problems and serves as an interactive tool for legal education, helping students understand complex concepts and practice legal drafting. Looking ahead, we plan continuous updates to enhance its deployment in professional settings, aiming to support lawyers with legal research, case analysis, and drafting legal opinions, thereby improving efficiency and accuracy in Hong Kong's legal framework.

样例：

```text
Prompt:
草拟一份优秀的状书的基本原则是甚么？

Output:
分析状书的基本要求
状书是法律程序中的重要文件，用于正式提出法律请求或申索。其目的是清楚地陈述申索的基础和相关事实。因此，草拟状书时需要明确、具体和准确地描述事件的经过。

方法一：从法律程序角度分析
从法律程序的角度来看，状书必须遵循特定的格式和内容要求。这包括提供详细的事实支持、明确列出申索理由以及提供相关证据的概要。这种方法强调对法律程序的遵循。

方法二：从沟通效率角度分析
从沟通效率的角度来看，状书应清晰易读，以便法庭和各方能够迅速理解案件背景和申索内容。这意味着使用简单明了的语言，并分段组织信息，以便快速查阅。

方法三：从策略性角度分析
从策略性角度来看，草拟者应考虑如何最有效地支持自己的立场。通过选择合适的事实和证据，可以最大化影响法庭判决。此外，了解对方可能提出的抗辩，并在状书中准备相应回应。

通过多种方法验证后，最终确认优秀状书需具备清晰、准确、全面、易读及策略性的特征。这些特征共同确保法庭能够有效理解案件背景并作出公正判决。
```

# 3. 构造收集

First, we crawl and clean raw legal materials from the internet, including Hong Kong e-Legislation (https://www.elegislation.gov.hk/). Then, we use GPT-4o to generate corresponding questions and thought-answer pairs based on the raw legal materials.

The dataset contains 15,959 question-thought-answer triples, each equipped with complete chain-of-thought annotations. All content is presented in Simplified Chinese and stored in a structured JSON format. The difficulty level of the questions in this dataset is intermediate to advanced for legal professionals and law school students.

The question types cover case analysis, legal application, explanation of legal concepts and so on. Each QTA triple includes detailed question prompt, a 3-5 step chain-of-thought reasoning process, and answer. The reasoning process involves multi-stage validation, reflective verification steps, and cross-case consistency checks, ensuring diversity in reasoning.

## 3.1 QAT生成Prompts

Here is our prompt template for Question generation:

```python
SYSTEM_PROMPT: str = """
# Task
基于以下参考法律材料，生成至少{n}个法律问题。问题需要满足以下要求：

1. 复杂度要求：
- 问题的答案需要通过对参考法律材料的深入理解和分析才能得出
- 应该是一个开放性问题，需要进行推理和解释
- 不能是简单的是非题或事实性问题

2. 问题形式：
- 可以是案例分析题
- 可以是法律适用题
- 可以是法律概念解释题

3. 问题结构：
- 明确的问题陈述

4. 难度级别：
中等难度，适合法律专业学生或从业者思考和讨论


5. 输出格式：
请严格使用JSON格式输出，结构如下：
{{
  "questions": [
    {{
      "id": 1,
      "type": "案例分析/法律适用/概念解释...", 
      "question": "具体问题",
    }},
    {{
      "id": 2,
      ...
    }},
    {{
      "id": 3,
      ...
    }}
  ]
}}
"""

USER_PROMPT: str = """
# 参考法律材料
{prompt}

# 提示
生成的问题应该与提供的参考法律材料直接相关，但是必须假装参考法律材料对你不可见。
请以JSON格式输出：
"""
```

Here is our prompt template for Thought(COT) and Answer generation:

```python
SYSTEM_PROMPT: str = """你是一个专家级的AI助手，能够逐步解释推理过程。你将收到一个问题和相关参考资料。你的任务是重构并展示通向正确答案的完整推理路径。

对于每个推理步骤，提供一个标题，描述你在该步骤中所做的事情，以及内容。但必须展示至少三种不同的方法或途径来得出该答案。

要求：
1. 使用3-5个推理步骤
2. 探索多种方法以达到答案
3. 通过不同的方法验证给定答案
4. 考虑潜在的替代答案并解释为何被拒绝
5. 你必须假装没有参考资料，只可以把参考资料当作自己的知识
6. 考虑你可能是错的，如果你的推理是错的，它会在哪里
7. 充分测试所有其他可能性。你可能会错
8. 当你说你正在重新检查时，请真正重新检查，并使用另一种方法进行，不要只是说你正在重新检查

以JSON格式回应，包含以下键：
- 'title': 当前推理步骤的描述
- 'content': 该步骤的详细解释
- 'next_action': 'continue' 或 'final_answer'
有效的JSON响应示例：
[
  {{ 
      "title": "分析给定信息", 
      "content": "首先，让我们检查问题，以识别将指导我们解决过程的关键要素……", 
      "next_action": "continue"
  }},
  {{ 
      "title": "...", 
      "content": "...", 
      "next_action": "continue"
  }},
  ...
  {{ 
      "title": "...", 
      "content": "...", 
      "next_action": "final_answer"
  }}
]
"""

USER_PROMPT: str = """
# 问题：
{prompt}
# 参考资料：
{references}

请以JSON格式输出：
"""
```

# 4. 训练

- 使用的训练框架 Github (259 star): https://github.com/PKU-Alignment/align-anything
  - 文档：align-anything.readthedocs.io
  - 相对小众，当支持多模型，图文、音频和文本
  - 开源数据：https://huggingface.co/datasets/PKU-Alignment/Align-Anything-Instruction-100K

基于llama3.1-8B进行SFT训练。

问答模板：

```python
system_prompt: str = ''
user_prompt: str = '<|reserved_special_token_0|>{input}<|reserved_special_token_1|>\n'
assistant_thinking: str = '<|reserved_special_token_2|>{thinking}<|reserved_special_token_3|>\n'
assistant_answer: str = '<|reserved_special_token_4|>{answer}<|reserved_special_token_5|>'
template = system_prompt + user_prompt + assistant_thinking + assistant_answer
```

训练超参数

```
# The deepspeed configuration
ds_cfgs: ds_z3_config.json
# Number of training epochs
epochs: 3
# Seed for random number generator
seed: 42
# Batch size per device for training
per_device_train_batch_size: 4
# Batch size per device for evaluation
per_device_eval_batch_size: 4
# The number of gradient accumulation steps
gradient_accumulation_steps: 16
# Whether to use gradient checkpointing
gradient_checkpointing: True
# Initial learning rate
learning_rate: 2.e-5
# Type of learning rate scheduler
lr_scheduler_type: cosine
# Ratio of warmup steps for learning rate
lr_warmup_ratio: 0.03
# Weight decay coefficient
weight_decay: 0.0
# Hyper-parameters for adam optimizer
adam_betas: [0.9, 0.95]
# Hyper-parameters for adam epsilon
adam_epsilon: 1.e-8
# Enable bfloat 16 precision
bf16: True
# Enable float 16 precision
fp16: False
# The strategy of evaluation, choosing form [epoch, steps]
eval_strategy: epoch
# The evaluation interval in step-wise evaluation case
eval_interval: 10
# The max norm of gradient
max_grad_norm: 1.0
```

数据：
```
# Datasets to use for training
train_datasets: HKAIR-Lab/HK-O1aw-SFT-16k
# The split of train datasets
train_split: train
```

模型配置：
```
# Pretrained model name or path
model_name_or_path: meta-llama/Llama-3.1-8B 
# Whether to trust remote code
trust_remote_code: True
# The max token length
model_max_length: 2048
```