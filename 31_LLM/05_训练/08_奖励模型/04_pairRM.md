# 1. 简介

- 模型下载：https://huggingface.co/llm-blender/PairRM
- 0.4B，性能接近GPT-4的对齐性能
- Github: https://github.com/yuchenlin/LLM-Blender
- 论文：https://arxiv.org/pdf/2306.02561.pdf
- 数据（100w SFT，1.54G 英文）：https://huggingface.co/datasets/llm-blender/mix-instruct
  - 由如下数据集构造：Alpaca-GPT4, Dolly-15k, GPT4All-LAION and ShareGPT
- 680 Stars 
   
# 2. 原理

![](.04_pairRM_images/训练方案.png)

ranker module should focus on learning to capture
the differences between the two candidates and
prefer the ones of higher quality.

![](.04_pairRM_images/方案设计.png)

![](.04_pairRM_images/Pair_Ranker设计.png)

![](.04_pairRM_images/PairRanker设计2.png)

![](.04_pairRM_images/PairRanker设计3.png)

![](.04_pairRM_images/PairRanker推理.png)

![](.04_pairRM_images/PairRanker方法.png)
