# 1. 简介

通过压缩KV cache实现长上下文，结合外推策略（如YaRN），从4k到400k。

- Github: https://github.com/FlagOpen/FlagEmbedding.git
- 论文：Soaring from 4K to 400K: Extending LLM's Context with Activation Beacon
- 低成本，仅需1B数据训练[redpajama](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T-Sample)
- SFT数据 (貌似全英文)：https://huggingface.co/datasets/namespace-Pt/projects/resolve/main/long-llm.tar.gz

# 2. 方法

There are two stages in training:
- Pretrain
  - 1B token from [redpajama](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T-Sample) with auto-regressive language modeling
  - Add eos to each document and no packing
  - 20K context length at maximum

- Finetune
  - 5K samples from [LongAlpaca](https://huggingface.co/datasets/Yukang/LongAlpaca-12k), 2K samples from [Booksum](https://huggingface.co/datasets/kmfoda/booksum), 16K synthetic long-context QA data from GPT-3.5, and 5K samples from pretraining data
  - 20K context length at maximum

