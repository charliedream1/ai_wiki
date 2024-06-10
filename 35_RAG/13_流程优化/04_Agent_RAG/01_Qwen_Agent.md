# 1. 简介

阿里在发布Qwen2之余，还发了一篇名为：“使用Qwen-Agent将上下文记忆扩展到百万量级”的博客，本意是用Qwen-Agent扩大大模型上下文窗口来处理超长文本输入，但是文中介绍了三种大模型智能问答智能体（Agent）的构建方式：
- Level-1 Agent（RAG）
- Level-2 Agent（Read All Chunks Parallelly）
- Level-3 Agent（Multi-Hop Reasoning）利用Function Calling

最终，大模型RAG问答终极之路还是Agent！

# 参考

[1] Qwen-Agent：RAG的终极之路还是Agent！, https://mp.weixin.qq.com/s/iZjfHEe2TXCJYPAGQ6beUQ