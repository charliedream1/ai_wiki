来源 Github (2.2k Stars): https://github.com/TigerResearch/TigerBot

## 开源数据集

### 预训练数据

<details>
基于 GPT3 的 pretrain 的数据分布，采集中文书籍，互联网，和百科类数据，并通过数据源质量分过滤和 tf-idf soft deduping，从 20TB 数据过滤到 2TB，保持语言和类目的比例，并在此基础上随机抽样 100G 数据开源：

- <a href=https://huggingface.co/datasets/TigerResearch/pretrain_zh>中文开源预训练集 -
  55G，包含中文书籍、中文互联网、中文百科 - 下载 [hugging face]</a>
- <a href=https://huggingface.co/datasets/TigerResearch/pretrain_en>英文开源预训练集 -
  51G，包含英文书籍、英文互联网、英文百科 - 下载 [hugging face]</a>

  | 类型       | 磁盘占用 | 来源 |
    | ---------- | -------- | ---- |
  | 中文书籍   | 12G      | 自研 |
  | 中文互联网 | 25G      | 自研 |
  | 中文百科   | 19G      | 自研 |
  | 英文书籍   | 22G      | 开源 |
  | 英文互联网 | 6.9G     | 开源 |
  | 英文百科   | 22G      | 开源 |
  | **总量**   | **106G** |      |

- 完整预训练数据占比如图所示:

<p align="center" width="100%">
<img src="image/pretrain_v2.png" alt="Tiger" style="width: 65%; display: block; margin: auto;"></a>
</p>

- 中文书籍及代码细分:

<p width="100%">
    <img src="image/zh-books.png" alt="中文书籍分类" style="width: 50%; min-width: 200px;"><img src="image/code-lang-type.png" alt="代码语言" style="width: 50%; min-width: 200px;">
</p>
</details>

### 微调数据

<details> 
<summary><b>数据搜集</b></summary>

模型中使用的微调数据的搜集思想如下：

a. 从用户指令的自然分布，人工标注总结 10 大类，120 小类任务，例如，事实性问答，开放式创作，语法分析，代码编辑等；

b. self-instruct: 参考 Alpaca self-instruct 方法，扩充中英文 seed_tasks，增加一些中文习惯种子问题，基于此生成 2M 中文(本次开源
0.5M)及 0.1M 英文(本次开源 50k)；

c. human-labeling: 基于人工写题及答案、网络搜集方式，整理加工问答集数据，在开源列表中标识为[自研]部分，本次开放部分数据；

d. open-source data cleaning: 基于各类公开数据集转换清洗，其中[自研*]部分，表示基于原始数据进行二次开发后得到，[开源]
部分数据集一般原始数据即为较规整的问答数据，进行简单清洗得到；

e. 总的数据分布符合用户指令自然分布。

</details>
<details> 
<summary><b>数据清洗</b></summary>
- 由于各类数据质量存在差异，通过 Alpaca Self-Instruct 生成的数据亦存在各种问题。因此，我们经过细致的人工校验和分类，总结出一套全面且系统化的数据清洗规则与方法。
- 整体规则可以划分为**过滤类规则**和**清洗类规则**两大类。其中，命中过滤规则的数据项将被弃用，而清洗规则旨在处理并保留所需的数据。
- 同时，在数据梳理与积累的过程中，我们也不断对清洗规则进行迭代和优化。
- 通用清洗规则描述如下所示：

a. 过滤类-敏感词规则：基于积累的敏感词库，清洗丢弃涉政、涉黄、涉暴、涉恐等数据项；

b. 过滤类-无效输入输出：此类规则主要针对 Self-Instruct 生成数据缺陷进行专项清理，根据输入输出分别制定规则，以丢弃一些无效的数据项；

> 无效输入如"<一段文本>"，无效输出如"[图画]"；

c. 清洗类-关键词规则：根据整理的关键词/正则列表进行数据的替换，包括：清理特殊标志位字符、清理非可见字符、清理标签、繁简转换等；

d. 清洗类-特殊逻辑规则：此类规则用于清洗一些特殊现象数据，如指令与输入重复等，如下所示：

> `{"instruction": "描述如何做一道红烧肉。请提供食材和详细的步骤。", "input": "请描述如何做一道红烧肉，提供食材和详细步骤。", ...}`

</details>

<details> 
<summary><b>数据开源</b></summary>
- 指令数据集, 当前开源 120W 问答对，磁盘空间 1.1G (数据集开放到 huggingface，中英文指令明细及下载如下表）
- <a href=https://huggingface.co/datasets/TigerResearch/sft_zh>中文-微调指令集-合集 - 53W 条 - 下载 [hugging face]</a>
- <a href=https://huggingface.co/datasets/TigerResearch/sft_en>英文-微调指令集-合集 - 67W 条 - 下载 [hugging face]</a>

| 类型        | 语言 | 数据集                                                                                                                              | 数量         | 来源   |
|-----------|----|----------------------------------------------------------------------------------------------------------------------------------|------------|------|
| alpaca 中文 | 中文 | [tigerbot-alpaca-zh-0.5m](https://huggingface.co/datasets/TigerResearch/tigerbot-alpaca-zh-0.5m)                                 | 0.5m       | 自研   |
| 百科问答      | 中文 | [tigerbot-wiki-qa-1k](https://huggingface.co/datasets/TigerResearch/tigerbot-wiki-qa-zh-1k)                                      | 1k         | 自研   |
| 名著问答      | 中文 | [tigerbot-book-qa-1k](https://huggingface.co/datasets/TigerResearch/tigerbot-book-qa-1k)                                         | 1k         | 自研   |
| 猜谜语       | 中文 | [tigerbot-riddle-qa-1k](https://huggingface.co/datasets/TigerResearch/tigerbot-riddle-qa-1k)                                     | 1k         | 自研   |
| 阅读理解      | 中文 | [tigerbot-superclue-c3-zh-5k](https://huggingface.co/datasets/TigerResearch/tigerbot-superclue-c3-zh-5k)                         | 5k         | 自研\* |
| 问答        | 中文 | [tigerbot-HC3-zh-12k](https://huggingface.co/datasets/TigerResearch/tigerbot-HC3-zh-12k)                                         | 12k        | 开源   |
| 知乎问答      | 中文 | [tigerbot-zhihu-zh-10k](https://huggingface.co/datasets/TigerResearch/tigerbot-zhihu-zh-10k)                                     | 10k        | 开源   |
| alpaca 英文 | 英文 | [tigerbot-alpaca-en-50k](https://huggingface.co/datasets/TigerResearch/tigerbot-alpaca-en-50k)                                   | 50k        | 自研   |
| 头脑风暴      | 英文 | [tigerbot-dolly-Brainstorming-en-1.7k](https://huggingface.co/datasets/TigerResearch/tigerbot-dolly-Brainstorming-en-1.7k)       | 1.7k       | 开源   |
| 分类        | 英文 | [tigerbot-dolly-Classification-en-2k](https://huggingface.co/datasets/TigerResearch/tigerbot-dolly-Classification-en-2k)         | 2k         | 开源   ｜
| 代码        | 英文 | [tigerbot-kaggle-leetcodesolutions-en-2k](https://huggingface.co/datasets/TigerResearch/tigerbot-kaggle-leetcodesolutions-en-2k) | 2k         | 自研\* |
| 食谱生成      | 英文 | [tigerbot-kaggle-recipes-en-2k](https://huggingface.co/datasets/TigerResearch/tigerbot-kaggle-recipes-en-2k)                     | 2k         | 开源   |
| 病历生成      | 英文 | [tigerbot-mt-note-generation-en](https://huggingface.co/datasets/TigerResearch/tigerbot-mt-note-generation-en)                   | 450        | 开源   |
| 多轮对话      | 英文 | [tigerbot-OIG-multichat-en-50k](https://huggingface.co/datasets/TigerResearch/tigerbot-OIG-multichat-en-50k)                     | 50k        | 自研\* |
| 综合问答      | 英文 | [tigerbot-stackexchange-qa-en-0.5m](https://huggingface.co/datasets/TigerResearch/tigerbot-stackexchange-qa-en-0.5m)             | 0.5m       | 开源   |
| wiki 问答   | 英文 | [tigerbot-wiki-qa-bart-en-10k](https://huggingface.co/datasets/TigerResearch/tigerbot-wiki-qa-bart-en-10k)                       | 10k        | 开源   |
| 如何做类教程    | 英文 | [tigerbot-youtube-howto-en-50k](https://huggingface.co/datasets/TigerResearch/tigerbot-youtube-howto-en-50k)                     | 50k        | 开源   |
| **总量**    |    |                                                                                                                                  | **120W 条** |

> 更多数据集陆续整理开放中...

</details>

### 领域数据

<details>
  开放金融、法律、百科相关领域数据，作为 rethink 外部数据源

| 类型                                                                              | 数量           |
|---------------------------------------------------------------------------------|--------------|
| [金融-研报](https://huggingface.co/datasets/TigerResearch/tigerbot-research-plugin) | 2W 篇         |
| [金融-财报](https://huggingface.co/datasets/TigerResearch/tigerbot-earning-plugin)  | 2500 篇       |
| [法律](https://huggingface.co/datasets/TigerResearch/tigerbot-law-plugin)         | 11 类 5.5W 条款 |
| [百科](https://huggingface.co/datasets/TigerResearch/tigerbot-wiki-plugin)        | 10W 词条       |

</details>