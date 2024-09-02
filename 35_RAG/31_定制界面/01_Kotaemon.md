# 1. 资源

项目地址：https://github.com/Cinnamon/kotaemon

特点：

- 对于最终用户：
    - 用于基于 RAG 的 QA 的干净简约的 UI。
    - 支持LLM API 供应商（OpenAI、AzureOpenAI、Cohere 等）和本地LLMs （通过ollama和llama-cpp-python ）。
    - 简单的安装脚本。
  - 对于开发人员：
    - 用于构建自己的基于 RAG 的文档 QA pipeline的框架。
    - 使用提供的 UI（使用 Gradio 构建）自定义并查看 RAG pipeline的运行情况。

特色：

- 托管自己的文档 QA (RAG) Web-UI 。支持多用户登录，在私人/公共收藏中组织您的文件，与他人协作并分享您最喜欢的聊天。

- 组织自己的的LLM和嵌入模型。支持本地LLMs和知名的的 API 供应商（OpenAI、Azure、Ollama、Groq）。

- hybird RAG 管道。 RAG 管道具有混合（全文和矢量）检索器 + rerank，以确保最佳检索效果。

- 多模态质量保证支持。通过图形和表格支持对多个文档进行问答。支持多模态文档解析（UI 上的有选项可配置）。

- 通过文档预览提前引用。默认情况下，系统会提供详细的引文，以确保LLM答案的正确性。直接在浏览器内的 PDF 查看器中查看您的引文（包括相关分数）并突出显示。当检索管道返回低相关文章时发出警告。

- 支持复杂的推理方法。使用问题分解来回答复杂/多跳问题。支持 ReAct、ReWOO 等代理的基于agent的推理。

- 可配置的设置用户界面。您可以在 UI 上调整检索和生成过程的最重要方面（包括提示）。

- 可扩展。基于 Gradio 构建，您可以根据需要自由定制/添加任何 UI 元素。此外，我们的目标是支持多种文档索引和检索策略。 GraphRAG索引管道作为示例提供。

# 参考

[1] https://mp.weixin.qq.com/s/Q46iSqleY5rxg3VgKAL4AA