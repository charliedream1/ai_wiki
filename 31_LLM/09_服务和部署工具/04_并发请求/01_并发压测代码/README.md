代码来源：
- https://github.com/bentoml/llm-bench
- https://github.com/modelscope/eval-scope
  - 为了支持各种服务API以及开源LLM推理性能，评估是否满足生产需求，我们提供一套简单可扩展的工具，支持LLM各项指标，详细可以参考eval-scope项目中的性能perf工具说明： https://github.com/modelscope/eval-scope/tree/main/llmuses/perf
  - 评测脚本：
  - 正常上下文：https://huggingface.co/datasets/Hello-SimpleAI/HC3-Chinese/blob/main/open_qa.jsonl
  - 长上下文数据集：https://huggingface.co/datasets/Yukang/LongAlpaca-12k/blob/main/LongAlpaca-12k.json