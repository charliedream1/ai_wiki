1. JetMoE: 用0.1M美元实现Llama2性能

  标题：JetMoE: Reaching Llama2 Performance with 0.1M Dollars

  机构：麻省理工学院、普林斯顿大学

  关键词：JetMoE、LLM、稀疏门控专家混合、成本效益

  作者：Yikang Shen, Zhen Guo, Tianle Cai

  分析：作者介绍了JetMoE-8B，这是一个新的LLM模型，只用了不到0.1百万美元，使用了1.25T标记来训练。JetMoE-8B基于高效的SMoE架构，具有8B参数，但只激活了每个输入标记的2B，与Llama2-7B相比，推理计算减少约70%。JetMoE-8B表现出色，超越了Llama2-7B和Llama2-13B-Chat模型，展示出LLM训练可以比大家普遍认为的更具成本效益。JetMoE-8B使用了稀疏门控专家混合体系结构，包括注意和前馈专家，同时采用了公开数据集和训练代码。作者详细说明了所有训练参数和数据混合物，以促进未来在开放基础模型开发的努力。这种透明度旨在鼓励合作和促进LLM领域的进一步发展。

  地址：https://arxiv.org/pdf/2404.07413

  代码：https://github.com/myshell-ai/JetMoE

# 参考

[1] 百度：GPT系列模型训练数据影响之探究 | 少样本准确率上提升30%，微软发布Rho-1 | 谷歌发布R-Gemma性能超越..， https://mp.weixin.qq.com/s/6aPtm-_e2ckQPJJ0lLZrwA
