# 资源

- 论文：The Lessons of Developing Process Reward Models in Mathematical Reasoning
  - https://arxiv.org/pdf/2501.07301
- 模型
  - https://hf.co/Qwen/Qwen2.5-Math-PRM-7B
  - https://hf.co/Qwen/Qwen2.5-Math-PRM-72B

# 问题

在按照常规原则构建数据并使用蒙特卡洛估计（MC estimation）在 BoN 上评估，训练我们自己的 PRM 的过程中，我们获得了几个关键的经验教训。

在 MC 估计方面：

1. 我们观察到，通过 MC 估计训练的 PRM 表现出显著较差的性能和泛化能力，相较于 LLM-as-a-judge（Zheng 等，2023）和人工标注而言。
2. 我们将 MC 估计表现不佳的原因归结于其根本性局限：它试图基于潜在的未来结果来评估当前步骤的确定性正确性。该方法极大地依赖于生成模型的性能，而生成模型可能在错误步骤上生成正确答案，或在正确步骤上生成错误答案，从而在步骤级正确性评估中引入了大量噪声和不准确性。

关于 BoN 评估：

1. 不可靠的策略模型会生成虽然最终答案正确但过程存在缺陷的响应，导致 BoN 的评估标准与 PRM 的过程验证目标不一致。
2. 过程验证能力有限，使得 PRM 对这类情况表现出容忍度，从而导致 BoN 表现被高估。
3. 我们发现，在现有 PRM 的步骤分数分布中，最低分数有相当大比例集中在最终答案步骤上，这表明 PRM 在 BoN 上的评估已从过程导向转向了结果导向。

