# 1. 简介

- Github: https://github.com/FlagOpen/FlagEmbedding.git
- We extend the context length of Llama-3-8B-Instruct from 8K to 80K via QLoRA fine-tuning
- 论文： Extending Llama-3's Context Ten-Fold Overnight

# 2. 方法

The entire training cycle is super efficient, which takes 8 hours on one 8xA800 (80G) GPU machine.

# 3. 测评

使用测评集： NIHS, topic retrieval, and long-context language understanding