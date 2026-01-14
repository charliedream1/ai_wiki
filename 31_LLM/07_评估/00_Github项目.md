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

# 3. Promptfoo

测试你的提示词、代理和RAGs。AI 红团队、渗透测试和漏洞扫描，针对大型语言模型进行分析。比较 GPT、Claude、Gemini、Llama 等软件的性能。简单的声明式配置，带有命令行和CI/CD集成。

你能用Promptfoo做些什么？
- 用自动评估测试你的提示和模型
- 通过红团队和漏洞扫描保护你的LLM应用
- 并排比较模型（OpenAI、Anthropic、Azure、Bedrock、Ollama 等）)
- 自动化CI/CD中的检查
- 审查拉取请求以了解与LLM相关的安全和合规性问题，涉及代码扫描
- 与你的团队分享结果