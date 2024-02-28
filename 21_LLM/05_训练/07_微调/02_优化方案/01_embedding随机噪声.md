# 1. embedding加随机噪声

代码在：https://github.com/neelsjain/NEFTune

论文题目:NEFTUNE: NOISY EMBEDDINGS IMPROVE INSTRUTION FINETUNING

1. 介绍

     该工作只在比较小的模型上进行微调，评估上也略显单一，解释上也不算太深入。
     不过实现起来非常简单，有资源的话可以快速试试。

     本文通过一个简单的增强方法，也就是在训练数据的正向传播期间向嵌入向量添加随机噪声的技巧，
     改进语言模型的微调。实验发现，有时改进幅度非常大,而且没有额外的计算或数据开销。
     使用Alpaca微调LLaMA-2-7B可以在在AlpacaEval上取得29.79%的表现,而使用加了
     噪声的嵌入则提高到64.69%。厉害了！！！
     
     ![](.03_Tricks_images/embedding随机噪声_实验1.png)
     
     ![](.03_Tricks_images/embedding随机噪声实验2.png)

     NEFTune表明了正则化对LLM训练很重要的。NEFTune是一个简单的技巧,但可以持续稳定
     地改进指令（Instruction）微调结果,这表明正则化在LLM下值得重新审视。

2. 方法

     NEFTune的每一步首先从数据集中采样一个指令（Instruction）,并将其转换为嵌入向量。然后,NEFTune添加一个随机噪声向量来增强嵌入。具体来说,噪声向量是通过随机采样均匀分布的独立identically分布的元素生成的,每个元素范围是[-1,1],然后用一个因子α/√Ld缩放整个噪声向量,其中L是序列长度,d是嵌入维度,α是一个可调参数。

     ```python
      def new_func(x):
      # during training, we add noise to the embedding
      # during generation, we don't add noise to the embedding
      if model.training:
          embed_init = orig_embed(x)
          dims = torch.tensor(embed_init.size(1) * embed_init.size(2))
          mag_norm = noise_alpha/torch.sqrt(dims)
          return embed_init + torch.zeros_like(embed_init).uniform_(-mag_norm, mag_norm)
      else:
          return orig_embed(x)
      return new_func 
     ```

# 参考

[1] 在微调时只需要简单的在 embedding层上加随机噪声即可大幅度提升微调模型的对话能力???, 
     https://mp.weixin.qq.com/s/ouEwFf3yS1n6HtZSayNvpw