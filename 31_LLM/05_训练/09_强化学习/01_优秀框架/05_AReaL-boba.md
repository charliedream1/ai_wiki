针对大语言模型的大规模强化学习训练门槛一直很高：

- 流程复杂、涉及模块多（生成、训练、奖励判定等），为实现高效稳定的分布式训练带来很多挑战；
- R1/o1 类推理模型的输出长度很长（超过 10K），并且随着训练持续变化，很容易造成显存和效率瓶颈；
- 开源社区缺乏高质量强化学习训练数据，以及完整可复现的训练流程。

本周，蚂蚁技术研究院和清华大学交叉信息院吴翼团队，联合发布了训练速度最快最稳定的开源强化学习训练框架 AReaL（Ant Reasoning RL），并公开全部数据和完成可复现的训练脚本。在最新的 AReaL v0.2 版本 AReaL-boba 中，其 7B 模型数学推理分数刷新同尺寸模型 AIME 分数纪录，并且仅仅使用 200 条数据复刻 QwQ-32B，以不到 200 美金成本实现最强推理训练效果。

- 项目链接：https://github.com/inclusionAI/AReaL
- HuggingFace数据模型地址：https://huggingface.co/collections/inclusionAI/areal-boba-67e9f3fa5aeb74b76dcf5f0a

使用 AReaL-boba 即可以 128 张 H800 规模在 1 天内训练完成 SOTA 1.5B 推理模型，以 256 张 H800 规模在 2 天内完成 SOTA 7B 推理模型训练。

# 参考

[1] 200美金，人人可手搓QwQ，清华、蚂蚁开源极速RL框架AReaL-boba, https://mp.weixin.qq.com/s/Cx8QHv2TVl-0mIJzKT7BDA