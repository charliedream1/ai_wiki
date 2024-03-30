## 1.2 FlagData

FlagData
- https://github.com/FlagOpen/FlagData
- 推荐：当前最全面最完整的数据处理流程代码
- 79 Stars
- 包含了完整的数据预处理流程，包括数据抽取、数据清洗、语种识别、质量评估、去重、数据分析
- 包含数据增广的prompt模板和流程代码，依赖ChatGPT构造数据
- 改流程主要适合基础模型数据处理的流程
- 当前仅公开了质量评估的模型
- 去重采用了minihash+Spark，速度较快
- Fasttext文本质量模型：https://huggingface.co/CASIA-LM/ChineseWebText-fasttext/tree/main
![](.01_清洗工具_images/FlagData流程.png)