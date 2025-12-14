ART（Agent Reinforcement Trainer）：智能体行为优化框架
GitHub： https://github.com/OpenPipe/ART

定位：ART 是由 OpenPipe 团队在 2025 年推出的开源框架，专门面向 Agent 场景下的强化学习训练。它让语言模型在动态环境中执行任务、收集交互轨迹、基于反馈优化策略，是“从 LLM 到 Agentic RL” 转变的典型代表。
核心功能：ART 以 POMDP （部分可观测马尔可夫决策过程）为基础建模 Agent 行为，支持 GRPO 与 RLVR 等算法。其训练循环可连接外部工具（如 Web API、文件系统、浏览器模拟器等），让模型学会在真实任务中优化执行策略。
用途与特点：ART 特别适用于构建“会操作”的 Agent，例如 Web 浏览 Agent、代码调试 Agent 或信息抽取 Agent。与 TRL 不同，ART 关注模型的执行反馈而非文本对齐。其可插拔 environment 接口允许用户轻松定义任务环境，使 Agent 在执行任务时获得奖励信号，从而实现端到端强化学习。

# 参考

[1] https://mp.weixin.qq.com/s/KllfYqWI5ljqd1YtPEViTA