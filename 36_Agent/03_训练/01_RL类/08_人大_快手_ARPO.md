# 1. 资源

论文标题：

AGENTIC REINFORCED POLICY OPTIMIZATION

论文链接：

https://arxiv.org/pdf/2507.19849

项目地址：

https://github.com/dongguanting/ARPO

为此，人大高瓴与快手团队联合提出了ARPO强化学习算法(Agentic Reinforced Policy Optimization)，专为训练多轮智能体设计。ARPO创新性地引入基于熵的自适应rollout机制，动态调节全局和局部采样策略，重点增强高不确定性节点的探索能力。同时，通过优势归因估计帮助LLM内化工具交互中的策略差异。

实验显示，在计算推理、知识推理及深度搜索领域的13项基准测试中，ARPO算法仅需一半的工具使用预算便优于GRPO等传统的样本级强化学习算法。为智能体训练提供了突破性解决方案。

# 参考

[1] Hugging Face周榜第一！人大高瓴与快手联合提出ARPO强化学习算法，专为Agent而生, https://mp.weixin.qq.com/s/zE9nrqkeRmpaS7CdGMdpwQ