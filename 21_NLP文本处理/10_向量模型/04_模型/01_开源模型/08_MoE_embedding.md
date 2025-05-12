https://github.com/tianyi-lab/MoE-Embedding

MoE Embedding: Your Mixture-of-Experts LLM Is Secretly an Embedding Model For FreeMOE是一个免费的嵌入模型

研究了如何直接从Mixture-of-Experts（MoE）架构的大型语言模型（LLMs）中提取高质量的嵌入表示，而无需额外的训练。研究发现，MoE模型中的路由权重（RW）可以作为嵌入模型，并且与常用的隐藏状态（HS）嵌入具有互补性。基于此，论文提出了Mixture-of-Experts Embedding（MOEE）方法，通过结合RW和HS，生成更全面的嵌入表示。

# 参考

[1] https://mp.weixin.qq.com/s/Lvq0vH2GpvVq_zsSCo7S9w