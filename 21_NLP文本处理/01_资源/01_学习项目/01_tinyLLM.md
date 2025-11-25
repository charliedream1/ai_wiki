去年在学习 NLP 时以读书为主 (大语言模型与深度学习书籍推荐)，但是实践偏少。所谓“学而不思则罔”，所以今年决定多做一些实践来巩固所学知识。个人作为造轮子爱好者，决定延续之前的”传统“
(toyml[1], toydl[2], toyllm[3], toyrl[4])，自己从零实现一些经典的 NLP 模型，这便是toynlp[5]的由来。

项目开源地址: https://github.com/ai-glimpse/toynlp.

ToyNLP
模型选择
ToyNLP 实现了 2003 年至 2018 年间共计 8 个经典的 NLP 模型：NNLM, Word2Vec, Seq2Seq, Attention, FastText, Transformer, BERT, GPT.

这 8 个模型是仔细筛选出来的，基本上都是 NLP 领域的里程碑式模型，也可以看出 NLP 领域技术演进的大致趋势。另外在复现的时候也考虑了本地复现/训练的可行性，毕竟算力有限。其实原本的计划是实现 10 个模型，另外还有 XLNet 和 T5，但是我发现到 BERT 和 GPT 的时候，单卡训练已经比较吃力了 (40 系单卡都要月级别的训练时间)，所以就留下了目前这 8 个模型。总的来说，前 5 个模型 (2003-2017) 是 NLP 领域的基础模型，我们不妨称之为“前 Transformer 时代”的模型；后面 3 个模型 (2017-2018) 则是由 Transformer 开启的时代，也是大语言模型的开端。

模型实现
Toy 系项目作为学习性质的项目，主要目标是帮助我更好地理解和实现这些经典模型。
所以在实现过程中，力求做到代码简洁易懂，避免过度工程化 (比如我们刻意避免了代码复用，尽量将每个模型的实现放在独立的文件中)。实际上，目前 8 个模型的实现都是独立的，互不依赖的。每个模型都包含了数据处理、模型定义、训练、推理和评估等完整的流程。

下面以 GPT 模型为例，简单展示一下 ToyNLP 的项目结构：

.
├── config.py
├── dataset.py
├── evaluation.py
├── inference.py
├── __init__.py
├── model.py
├── README.md
├── tokenizer.py
└── train.py
可以看到，GPT 模型的实现包含了配置文件 (config.py)、数据集处理 (dataset.py)、评估(evaluation.py)、推理 (inference.py)、模型定义 (model.py)、分词器(tokenizer.py) 和训练 (train.py) 等模块。每个模块都专注于特定的功能，便于理解和维护。

训练细节
由于算力有限，ToyNLP 的训练过程主要依赖单卡 GPU(40 系显卡) 进行训练。为了在有限的算力下完成训练，我们对模型规模和训练参数进行了适当的调整。具体可以参考每个模型的 README 文件，里面详细记录了训练参数和模型结果等信息。之前介绍的BERT 论文复现[6]其实就是基于 ToyNLP 项目中的 BERT 模型的训练过程 (记录在toynlp/bert/README.md) 整理而来。

另外需要注意的是，目前各模型的复现文档还不完善，基本只有 BERT 和 GPT 模型的训练细节比较完整，后续我会逐步完善其他模型的文档。

现状 & 未来计划
项目整体按照"First make it work, then make it better"的逻辑。目前 8 个模型都已经实现并且可以训练和推理，算是完成了"Make it work"的阶段，后续会逐步完善代码和文档，进入"Make it better"的阶段。文档方面会将每个模型的训练细节、结果和一些实验分析等内容补充完整。代码方面会对每个模型的实现进行优化，提升代码质量和可读性。

结语
ToyNLP 项目和我其他的 Toy 系项目一样，基本都是个人学习和兴趣驱动的产物。但我仍然希望它们能够对其他学习 NLP 和深度学习的同学有所帮助，提供一些实践上的参考和借鉴。如果有对项目的建议或者想法，欢迎留言讨论或在 GitHub 上提 issue 或者 PR 来交流！

引用链接
[1] toyml: https://github.com/ai-glimpse/toyml
[2] toydl: https://github.com/ai-glimpse/toydl
[3] toyllm: https://github.com/ai-glimpse/toyllm
[4] toyrl: https://github.com/ai-glimpse/toyrl
[5] toynlp: https://github.com/ai-glimpse/toynlp
[6] BERT 论文复现: https://datahonor.com/blog/2025/11/02/bert/


# 参考

[1] ToyNLP: 从零实现自然语言处理经典模型, https://mp.weixin.qq.com/s/jn3FDMgnuX-gZgXyTmYerw