# 1. ContextASR-Bench

ContextASR-Bench数据和评测代码现已开源！欢迎大家下载、使用和交流~

在研究和实践中我们发现语音识别（ASR）任务非常依赖模型对世界知识的掌握，尤其是在需要识别各种垂域下的专业术语或者命名实体的场景。如今，我们看到了大语言模型（LLM）在通用理解，复杂推理任务上的惊艳表现，但是对于ASR任务，在现有的测试集上相较于传统小参数量模型并没有展现出预期的压倒性优势。现有ASR测试集普遍以较短的语音、非常有限的垂域或者闲聊文本为主，难以体现LLM的强大上下文能力和从海量文本训练数据中获取的世界知识对ASR任务的帮助。因此，我们提出了ContextASR-Bench，总计40000多条长语音测试用例（30s - 180s），涵盖超10个领域的中英ASR测试基准，采用三种不同粒度的上下文评测方式和NE-WER、NE-FNR两种针对命名实体识别准确率的指标。与现有ASR测试集关注声学鲁棒性不同，ContextASR-Bench以多领域专业术语密度极高的语料侧重考察ASR系统在语言上的能力或者说知识。实验结果表明，ContextASR-Bench在LLM-based和传统ASR系统上展现出了极高的区分度，充分体现了LLM对各种垂域下ASR任务的帮助。

Paper: https://arxiv.org/abs/2507.05727
Code: https://github.com/MrSupW/ContextASR-Bench
Data: https://huggingface.co/datasets/MrSupW/ContextASR-Bench