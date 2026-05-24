https://github.com/ECNU-ICALK/AutoSkill/blob/main/README.zh-CN.md

[1]https://arxiv.org/abs/2603.01145

[2]https://github.com/ECNU-ICALK/AutoSkill

这篇论文讨论的是长期个性化智能体里一个很实际的问题：用户在真实使用中会反复表达稳定偏好，例如希望模型少幻觉、遵循某种写作规范、避免过于技术化的措辞，或者按照固定流程完成任务。但这些反复出现的经验，往往并没有真正沉淀成可复用能力。很多 LLM agent 的做法仍然是把过去对话当作待检索文本，或者依靠参数更新、提示工程和短期上下文反复“重新学一遍”。

论文提出的 AutoSkill 尝试用另一种方式处理这个问题：把交互经验从“记忆记录”提升为“显式技能”。它的核心目标不是单纯保存过去发生过什么，而是把那些反复出现、可以迁移到未来请求中的行为约束和任务套路，抽象成结构化 skill artifact，并在后续请求中动态检索和注入。按论文的定义，这是一条 training-free 的 lifelong learning 路线：不改底层模型参数，而是通过外部技能库的持续演化，让 agent 累积能力。

@software{autoskill_2026,
  author = {Yutao Yang, Junsong Li, Qianjun Pan, Bihao Zhan, Yuxuan Cai, Du Lin, Xin Li, Bo Zhang, Qin Chen, Jie Zhou, Kai Chen, Liang He},
  title = {AutoSkill: Experience-Driven Lifelong Learning via Skill Self-Evolution},
  year = {2026},
  url = {https://github.com/ECNU-ICALK/AutoSkill},
  note = {GitHub repository}
}

@misc{yang2026autoskillexperiencedrivenlifelonglearning,
  title={AutoSkill: Experience-Driven Lifelong Learning via Skill Self-Evolution},
  author={Yutao Yang and Junsong Li and Qianjun Pan and Bihao Zhan and Yuxuan Cai and Lin Du and Jie Zhou and Kai Chen and Qin Chen and Xin Li and Bo Zhang and Liang He},
  year={2026},
  eprint={2603.01145},
  archivePrefix={arXiv},
  primaryClass={cs.AI},
  url={https://arxiv.org/abs/2603.01145},
}

