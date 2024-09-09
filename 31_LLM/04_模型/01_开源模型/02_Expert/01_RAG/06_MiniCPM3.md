MiniCPM3-RAG-LoRA(https://huggingface.co/openbmb/MiniCPM3-RAG-LoRA)是一个专门面向检索增强生成（RAG）场景的生成模型。

它在MiniCPM3 的基础上，采用低秩适应（LoRA）技术，通过直接偏好优化（DPO）方法进行微调，仅基于两万余条开放域问答和逻辑推理任务的开源数据，在通用评测数据集上实现了模型性能平均提升约 13%。

可以看看其训练数据格式，MiniCPM3-RAG-LoRA模型遵循格式如下：

MiniCPM3-RAG-LoRA supports instructions in the following format:

对应微调数据：

Passages = "In the novel 'The Silent Watcher,' the lead character is named Alex Carter. Alex is a private detective who uncovers a series of mysterious events in a small town.\nSet in a quiet town, 'The Silent Watcher' follows Alex Carter, a former police officer turned private investigator, as he unravels the town's dark secrets.\n'The Silent Watcher' revolves around Alex Carter's journey as he confronts his past while solving complex cases in his hometown.",

Instruction = "Q: What is the name of the lead character in the novel 'The Silent Watcher'?\nA:"

Input = 'Background:\n'+ Passages + '\n\n' + Instruction

# 参考

[1] RAG开源微调大模型项目及其实现思路：兼看0905大模型进展回顾，https://mp.weixin.qq.com/s/Xjr0NA_sVcrs5YaIDnF6BA