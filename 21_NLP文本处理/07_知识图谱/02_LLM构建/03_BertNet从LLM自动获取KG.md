# 1. 资源

论文：
- BertNet: Harvesting Knowledge Graphs with Arbitrary Relations from Pretrained Language Models
- https://ar5iv.labs.arxiv.org/html/2206.14268?_immersive_translate_auto_translate=1

Github (93 Stars): https://github.com/tanyuqian/knowledge-harvest-from-lms

Demo available at https://lmnet.io

# 2. 介绍

我们提出了一种从预训练的 LM 中收获大量任意关系 KG 的新方法。通过最少的关系定义输入（提示和少量示例实体对），该方法可以在巨大的实体对空间中有效地搜索，以提取所需关系的各种准确知识。我们开发了有效的搜索和重新评分机制，以提高效率和准确性。我们部署该方法从不同的 LM 中获取 400 多个新关系的 KG。广泛的人工和自动评估表明，我们的方法能够提取各种准确的知识，包括复杂关系的元组（例如，“A 有能力但不擅长 B”）。由此产生的 KG 作为源 LM 的符号解释也揭示了对 LM 知识能力的新见解。

# 3. 方法

![](.03_LLM自动构建KG_images/流程图.png)

上图描述了从LLM中获取知识的步骤：

- 从初始提示词和很少的（两个）示例实体对开始。

- 自动创建多样化的加权提示词：包含两块内容 
  - 一块（参考上图中左下角Prompt Creation部分)是将示例与初始提示词合并后，通过GPT3（text-davinci-002）模型生成多个具有相同含义的句子，再删除句子中的实体名称得到一个新提示词。通过不断解释新创建的提示来重复此过程，直到收集到至少 10 个关系提示词。
  - 另一块(参考右下prompt weighting部分）是对生成的提示词确定适当的权重，从而提高后面知识搜索过程的精度（涉及一些数学概念，比如联合对数似然等，这里就不细说了，想深入了解的去看论文）。

- 知识元组的高效搜索：（参考上图右边部分）
  - 用上一步获得的提示词和权重，对指定模型（即要抽取知识的LM）搜索所有与提示词一致的实体对，计算它们各自的一致性分数，并选择分数最高的前 K 个实体对作为结果知识。

# 参考

[1] 【AIGC FREE】我的知识我来管——能救RAG的只有KG（六）从LM中导出KG，https://mp.weixin.qq.com/s/OVo0tER4kbSG977u3BkOYg