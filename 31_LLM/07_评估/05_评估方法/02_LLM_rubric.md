- Github (22 stars): https://github.com/microsoft/llm-rubric
- 论文：
  - LLM-Rubric: A Multidimensional, Calibrated Approach to Automated Evaluation of Natural Language Texts
  - 2024.12.31
  - https://arxiv.org/abs/2501.00274
LLM-Rubric引入了自然语言文本自动评估的框架。手动构建的评分标准描述了如何评估多个感兴趣维度。为了评估文本，每个评分标准问题都会触发一个大型语言模型（LLM），并生成潜在回答的分布。LLM的预测常常无法与人类评判者一致——事实上，人类之间并不完全一致。然而，多个LLM分布可以组合起来，预测每位人类评审对所有问题的注释，包括评估整体质量或相关性的总结问题。LLM-Rubric通过训练一个包含评判特异和无关评判参数的小型前馈神经网络来实现这一目标。在评估人机信息寻求任务中的对话系统时，我们发现包含9个问题的LLM评分标准（评估自然性、简洁性和引用质量等维度）能够预测人类评委对整体用户满意度的评估，评分为1至4。