# 1. 资源

- Github (618 stars): https://github.com/dCaples/AutoDidact/
- 基于Unsloth修改

# 2. 简介

研究探索小型 LLM 如何通过生成、研究和回答自创的问答对来自主增强自己的研究和推理能力，通过强化学习学习代理搜索。所有这些都在单个 RTX 4090 上运行！

学分：该项目是使用 Unsloth 的 Efficient GRPO 代码构建的，并增加了对函数调用和代理循环的支持。

主要特点
- 使用 Llama-8B 进行自引导：Llama-8B 从文档中自主生成有意义的问答对，然后训练自己有效地搜索语料库以回答这些自生成的问题。
- 自主自我验证：Llama-8B 评估自己答案的准确性，创建一个自我改进的反馈循环。
- GRPO 强化学习：实施组相对策略优化 （GRPO） 以改进 Llama-8B 的有效研究、搜索和推理能力。
- 完全自主的开源管道：每个步骤（包括问题生成、答案研究、验证、嵌入创建和强化学习）都使用开源模型在本地运行。

过仅 100 步的 GRPO 训练（在单个 RTX 4090 GPU 上训练 1 小时），Llama-8B 显著提高了其研究和回答阿波罗 13 号任务报告中问题的能力。

在包含 68 个问题的验证集中，准确率从 23% 增加到 59%，翻了一番多。

分步搜索过程
```
查询 ："Apollo 13 Command Module Pilot substitution"

结果：检索到运营支持详细信息，但没有对替换进行解释。
代理的作：已识别的缺失信息→ 优化查询。
查询 ："Apollo 13 Command Module Pilot substitution reason"

结果：检索到一般任务异常细节，但仍然没有直接答案。
代理的作：提高了查询特异性。
查询 ："Apollo 13 John 'Jack' Swigert substitution"

结果：找到一般任务报告，但仍然缺乏明确的替换理由。
代理的作：假设的疾病可能是相应的 Refined 查询→因素。
查询 ："Apollo 13 Jack Swigert illness substitution"

结果：检索到确切的解释：“在发射前几天，备用登月舱飞行员患上了麻疹。对主要机组人员的检查表明，指挥舱飞行员对这种疾病没有免疫力;因此，备用 Command Module Pilot 被替换了。

最终答案
最初的指挥舱飞行员对麻疹缺乏免疫力，因此必须由杰克·斯威格特 （Jack Swigert） 取代他。

此示例显示了 llama 如何学习进行多次搜索以查找其问题的答案。
```