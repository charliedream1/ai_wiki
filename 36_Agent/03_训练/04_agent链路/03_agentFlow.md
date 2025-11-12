📌 一句话总结：
本工作提出 AgentFlow，一个可训练的「多模块智能体系统」（agentic system），通过在线强化学习算法 Flow-GRPO 在交互式推理流程中优化规划策略，实现更高效的多工具协同与长期推理能力，性能超越 GPT-4o。
🔍 背景问题：
当前基于 LLM 的推理系统主要面临三大瓶颈：
1️⃣ 单体策略模型扩展性差 —— 传统工具增强式强化学习（Tool-Integrated RL）训练单一策略在长推理链下不稳定，难以泛化到多工具环境；
2️⃣ 训练脱离真实交互 —— 现有 agentic 系统大多为无训练（training-free）或离线微调（offline fine-tuning），无法适应多轮动态反馈；
3️⃣ 长程稀疏奖励难以归因 —— 多步工具调用中的成功信号往往只在终态可验证，导致信用分配困难与策略震荡。
💡 方法简介：
提出 AgentFlow 框架，将智能体分解为四个协同模块：
🧭 Planner（规划器）：制定子目标与工具选择；
⚙️ Executor（执行器）：调用外部工具完成子任务；
✅ Verifier（验证器）：评估执行结果并更新记忆；
🧠 Generator（生成器）：整合最终答案。
核心创新在于引入 Flow-GRPO（Flow-based Group Refined Policy Optimization） ——
一种“在流中优化（in-the-flow optimization）”的强化学习算法，将多轮任务的全局结果回传至每一轮规划决策，通过组归一化优势函数实现稳定的长程信用分配，从而让规划模块能在真实交互环境中自适应学习有效策略。
📊 实验结果：
在 十个多领域推理基准（包括 2Wiki、HotpotQA、GAIA、AIME24、MedQA 等）上，
AgentFlow-7B 相比主流工具强化学习模型平均准确率提升：
🔹 +14.9%（搜索任务） 🔹 +14.0%（Agentic任务）
🔹 +14.5%（数学推理） 🔹 +4.1%（科学推理）
其性能超越 GPT-4o（≈200B 参数），在相同工具集下表现最优；
Flow-GRPO 显著降低工具调用错误率（最高下降 28.4%），
并在 2Wiki、MedQA 等任务中自动学习到最优工具选择分布。
📂 开源链接：
🔗 https://github.com/lupantech/AgentFlow
📄 论文原文：
🔗 https://arxiv.org/abs/2510.05592
📣 一句话点评：
AgentFlow 将多智能体系统从‘规则编排’推进到‘在线共训’，让工具使用与规划真正形成自适应闭环。

# 参考

[1] 斯坦福提出 AgentFlow：在交互流中优化智能体推理与工具使用, https://mp.weixin.qq.com/s/me5M4AJihSPjuqVbZJivvA