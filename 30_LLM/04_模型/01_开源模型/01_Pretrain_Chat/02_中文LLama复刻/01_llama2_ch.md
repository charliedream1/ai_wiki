# 简介

1. 资源路径
   - https://github.com/FlagAlpha/Llama2-Chinese
   - 5.9k Stars

2. 介绍
   
   - 高效的中文词表
   
     基于数百G的中文文本，在该模型词表的基础上扩展词库至65,000个单词。
     经过测试，我们的改进使得中文编码/解码速度提高了约350％。此外，
     我们还扩大了中文字符集的覆盖范围，包括所有emoji符号😊。这使得生成带有表情符号的文章更加高效
   
   - 自适应上下文扩展
   
     Atom大模型默认支持4K上下文，利用位置插值PI和Neural Tangent Kernel （NTK）方法，
     经过微调可以将上下文长度扩增到32K。
    `