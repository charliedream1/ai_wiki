# 1. ChatALL
   - 可以同时和多个LLM聊天，便于对比性能
   - Github (13.2k Stars): https://github.com/sunner/ChatALL
   - 介绍网页：https://chathub.gg/
   - ![](.00_Github项目_images/页面展示.png)

# 2. DeepEval

地址：https://github.com/confident-ai/deepeval

有没有一种方式，能像写单元测试一样，把 LLM 的评测流程自动化、标准化？DeepEval 就是为此而生的。

DeepEval 是 Confident AI 团队开源的 LLM 评测框架。它的最大特点，就是让你用极简的代码，把复杂的模型评测流程变得像写 pytest 一样自然，支持本地运行，并且LLM应用开发框架集成，如 LlamaIndex、Langchain、CrewAI 等。比如，你只需要几行代码，就能定义一个测试用例和评测标准：

DeepEval 不只是“能用”，而且“好用”。它内置了多种主流的 LLM 评测指标，覆盖了大部分实际场景。比如：

- 你想知道模型输出和标准答案有多接近？用 Correctness（正确性）。
- 想判断答案和用户问题的相关性？有 Answer Relevancy（答案相关性）。
- 担心模型“胡说八道”？Hallucination（幻觉检测） 能帮你发现无依据的内容。
- 做 RAG 检索增强，关心输出是否忠实于上下文？Faithfulness（事实一致性） 和 Context Recall（上下文召回） 都能派上用场。
- 还有 Toxicity（有害内容检测），帮你过滤掉不当内容，保障应用安全。
   