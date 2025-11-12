论文：TREE SEARCH FOR LLM AGENT REINFORCEMENT LEARNING

![](.04_tree_grpo_images/fd00d3a3.png)

树搜索 rollout 包含三个关键阶段：

初始化：为每个提示生成 M 条独立轨迹作为树根，构建初始树结构。
采样：从每棵树中随机选择 N 个非叶节点（排除最终答案节点）进行扩展。
扩展：以选中节点的完整上下文为输入，继续生成剩余轨迹分支并插入树中。
通过迭代执行采样与扩展步骤，树结构天然实现轨迹间前缀共享，减少令牌和工具调用的冗余开销。


# 参考

[1] 阿里AMAP提出Tree-GRPO：树搜索革新LLM多轮代理强化学习, https://mp.weixin.qq.com/s/X_nOKJVkCdSdkSeDF4lrdQ