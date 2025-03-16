# 1. 简介

REINFORCE++的核心思想是将PPO中的各种优化技巧整合到经典的强化学习算法REINFORCE中，以提升其性能和稳定性。这样REINFORCE++不需要 Critic 从而节省计算资源，又有加持了 PPO 相关的优化技巧实现高效训练。 REINFORCE++的特点是 比 GRPO 稳定比PPO快。

代码实现：我们基于 OpenRLHF 实现了这个 REINFORCE++ 算法
- https://github.com/OpenRLHF/OpenRLHF/blob/main/examples/scripts/train_reinforce_llama_ray.sh

比 GRPO 稳定比PPO快

# 2. 原理

## 2.1 **REINFORCE**

REINFORCE算法是强化学习（Reinforcement Learning）中的一种重要策略梯度方法，旨在通过直接优化策略来最大化预期的累计奖励。以下是对REINFORCE算法的简单介绍。

REINFORCE算法基于蒙特卡罗方法，通过以下步骤进行操作：

- **策略采样**：智能体根据当前策略与环境交互，生成一条状态-动作-奖励序列（轨迹）。

- **回报计算**：对每条轨迹进行回报计算，通常采用折扣累计奖励的形式

- **梯度估计**：使用蒙特卡罗方法计算策略梯度，更新策略参数

- **策略更新**：通过梯度上升法更新策略参数

## 2.1 **在 REINFORCE 上集成下面的优化 Tricks 以稳定模型的训练**

### Token Level KL-Penalty

**Token Level KL-Penalty** 是一种在序列生成任务中使用的正则化技术。其主要目的是控制生成的文本与训练数据之间的差异，以避免模型生成过于偏离训练分布的输出。具体方法如下

这种 Token-level KL 的好处是可以无缝兼容 PRM 并且实现了KL reward的信用分配

### Mini-batch Updates

**Mini-batch Updates** 是一种常用的优化策略，旨在提高训练效率和稳定性。其基本思想是：

- **小批量样本**：将训练数据划分为多个小批量（mini-batch），而不是使用整个数据集进行更新。

- **频繁更新**：通过在每个小批量上进行多次参数更新，可以更快地收敛，同时减少内存消耗。

- **随机性引入**：小批量更新引入了随机性，有助于避免局部最优解，提高模型的泛化能力。

### Reward Normalization and Clipping

**Reward Normalization and Clipping** 是处理奖励信号不稳定的一种方法。具体包括：

- **奖励归一化**：通过对奖励进行标准化（例如，减去均值并除以标准差），使得奖励信号更为平稳，从而提高训练过程的稳定性。

- **奖励裁剪**：限制奖励值在某个范围内，以防止极端奖励对模型更新造成过大的影响。这有助于保持学习过程的稳定性，并防止梯度爆炸。

### Advantage Normalization

**Advantage Normalization** 是一种用于处理优势函数（advantage function）估计方差的方法。

优势归一化的步骤包括：

- **均值和方差计算**：对计算出的优势值进行均值和方差计算。

- **归一化处理**：将优势值减去均值并除以标准差，使得优势值具有更好的数值稳定性，进而提高学习效果。

### PPO-Clip

**PPO-Clip** 是近端策略优化（Proximal Policy Optimization, PPO）算法中的一个关键技巧，用于限制策略更新幅度。其主要思想是：

- **剪切目标函数**：通过引入一个剪切机制，限制新旧策略之间的比率变化，确保更新不会过大。这可以用以下公式表示：

- **提高稳定性和样本效率**：这种剪切机制有效防止了策略更新过大导致的不稳定，提高了算法的收敛速度和样本效率。

# 参考

[1] RLHF 对齐之 REINFORCE++ 算法 - 比,https://www.toutiao.com/article/7453162688554779163/?is_new_connect=0&is_new_user=0