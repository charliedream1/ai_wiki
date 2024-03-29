# 1. 简介

1. RLHF   
   归功于InstructGPT相关的论文，RLHF成为了训练LLM的关键算法
   （将这一技术用于该目的）。该算法的典型实现如下：
   - 让人类恶意LLM输出对进行比较，这些输出对是根据相同提示产生的；
   - 使用人类偏好来学习一个奖励函数。奖励函数通常由transformer网络表示，
     它被训练为向人类喜欢的输出给出更高的奖励（或分数）。
   - 最后，使用学习到的奖励，运行一个强化学习算法来调整LLM以
     - (i)将生成答案的奖励最大化，同时
     - (ii)不让LLM改变太多（以一种正则化形式）。

   这是一个相对复杂的算法，需要分别表示奖励函数和LLM。
   此外，众所周知最后的强化学习步骤在选择超参数时表现得很棘手。

2. DPO

   DPO极大地简化了整个过程。作者不需要单独的transformer网络来表示
   奖励函数和LLM，而是展示了如何在给定LLM的情况下，计算出LLM最擅长最大
   化的奖励函数（加上正则化项）。这样两个transformer网络就合二为一了。
   因此，我们现在只需要训练LLM，而不再需要处理单独训练的奖励函数。
   DPO算法直接训练LLM，使奖励函数（由LLM隐式定义）与人的偏好一致。
   此外，作者表明DPO在实现RLHF的优化目标（即上面的(i)和(ii)点）
   方面比RLHF本身的大多数实现更好。

![](.01_DPO_images/RLHF_vs_DPO.png)

# 参考

[1] 吴恩达来信：超越RLHF的DPO，https://mp.weixin.qq.com/s/x-heodyjxY7IItYm4Fx7dA