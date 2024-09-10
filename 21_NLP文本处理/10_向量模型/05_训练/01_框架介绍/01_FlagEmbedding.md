# 1. FlagEmbedding
## 1.1 特点
- Github (6.7k stars): https://github.com/FlagOpen/FlagEmbedding.git

特点：支持文本和图文向量，以及rerank
- 支持预训练
- 支持微调
- 支持多机训练，底层依赖PyTorch和transformers
- 此表由最早的~20K，到bge-m3提升到~151k
- 提供完善的测评工具
  - CMTEB

训练技巧：
- 负例挖掘
- 多向量：colbert/dense/sparse
- batch任务均衡：任务均来源同一个任务
- 支持基于教师得分的知识蒸馏
- 短文本拼接及对齐
- 负例分配到每个设备
- temperature调节
- 自蒸馏
- 冻结权重
- gradient_checkpointing
- 包括按长度的分块 (?)
- prompt指令加入
- 支持模型平均，以均衡性能
  - 按权重平均
  - 基于数据集计算平均

缺点：
- 缺少大规模训练的一些加速策略，如flash-attention、packing等

推荐度：⭐️⭐️⭐️⭐️⭐️
- 丰富全面
- 更新及时

## 1.2 部分参数说明

- BGE-M3：unified_finetuning开启则微调colbert/dense/sparse三个模型，否则只微调dense模型

## 1.3 注意事项

- 训练参数中有对query和passage的限制，需要根据实际情况调整
- 考虑是否加入prompt

## 1.4 其它训练策略
### 1.4.1 基于大模型LLARA

通过提示词，分别使用2个基于llama2-7B模型对query和passage进行编码，然后计算相似度

### 1.4.2 基于大模型任务的embedding

基于大模型过程中常用的6个任务微调:

- Question Answering (qa)
- Conversational Search (convsearch)
- Long Conversation (chat)
- Long-Range Language Modeling (lrlm)
- In-Context Learning (icl)
- Tool Learning (tool)
