# 1. 资源

代码：https://github.com/langchain-ai/langgraph/blob/main/examples/rag/langgraph_rag_agent_llama3_local.ipynb

原文：Plaban Nayak Build a Reliable RAG Agent using LangGraph

# 2. 简介

## 2.1 原理简介
![](.03_Agent_RAG_路由_加_多步推理_images/流程.png)

- 自适应 RAG (论文**)**。我们已经实现了本文中描述的概念，构建了一个路由器，用于将问题路由到不同的检索方法。
- 校正 RAG (论文**)**。我们已经实现了本文中描述的概念，开发了一个回退机制，用于在检索到的上下文与所问问题不相关时继续进行。
- 自身 RAG (论文**)**。我们已经实现了本文中描述的概念，开发了一个幻觉评分器，即修正那些产生幻觉或未回答所问问题的答案。

## 2.2 方案分析及LangGraph介绍

代理可以通过使用 Langchain 的 ReAct 概念或使用 LangGraph 来体现。

Langchain 代理和 LangGraph 之间的权衡：

*可靠性*

- ReAct / Langchain 代理：可靠性较低，因为 LLM 需要在每个步骤上做出正确的决策

- LangGraph：可靠性更高，因为控制流已经设置好，LLM 在每个节点上有具体的任务

*灵活性*

- ReAct / Langchain 代理：更灵活，因为 LLM 可以选择任何动作序列
- LangGraph：灵活性较低，因为动作受限于在每个节点上设置控制流

*与较小 LLM 的兼容性*

- ReAct / Langchain 代理：兼容性较差
- LangGraph：兼容性较好

在这里，我们使用 LangGraph 创建了代理。

*什么是 LangGraph？*

LangGraph 是一个扩展 LangChain 的库，为 LLM 应用程序提供了循环计算功能。虽然 LangChain 支持定义计算链（有向无环图或 DAG），但 LangGraph 允许包含循环。这允许更复杂、更像代理的行为，其中 LLM 可以在循环中被调用以确定下一步要采取的动作。

*关键概念*

- 有状态图：LangGraph 围绕着有状态图的概念展开，图中的每个节点代表我们计算的一个步骤，并且图保持一个状态，该状态随着计算的进行而传递和更新。
- 节点：节点是 LangGraph 的构建块。每个节点代表一个功能或一个计算步骤。我们定义节点来执行特定的任务，例如处理输入、做出决策或与外部 API 进行交互。
- 边：边连接图中的节点，定义计算的流程。LangGraph 支持条件边，允许您根据图的当前状态动态确定要执行的下一个节点。

*使用 LangGraph 创建图的步骤*
- 定义图状态：表示图的状态。
- 创建图。
- 定义节点：在这里，我们定义与每个工作流状态相关联的不同功能。
- 将节点添加到图中：在这里，将我们的节点添加到图中，并使用边和条件边定义流程。
- 设置图的入口和结束点。

*什么是 Tavily 搜索 API？*

Tavily 搜索 API 是针对 LLM 进行优化的搜索引擎，旨在实现高效、快速和持久的搜索结果。与其他搜索 API（如 Serp 或 Google）不同，Tavily 专注于优化搜索，以满足 AI 开发人员和自主 AI 代理的需求。

# 3. 原理流程介绍

RAG Agent 的工作流程

- 根据问题，路由器决定是从向量存储中检索上下文还是进行网页搜索。
- 如果路由器决定将问题定向到向量存储以进行检索，则从向量存储中检索匹配的文档；否则，使用 tavily-api 进行网页搜索。
- 文档评分器然后将文档评分为相关或不相关。
- 如果检索到的上下文被评为相关，则使用幻觉评分器检查是否存在幻觉。如果评分器决定响应缺乏幻觉，则将响应呈现给用户。
- 如果上下文被评为不相关，则进行网页搜索以检索内容。
- 检索后，文档评分器对从网页搜索生成的内容进行评分。如果发现相关，则使用 LLM 进行综合，然后呈现响应。

使用的技术堆栈
- 嵌入模型：BAAI/bge-base-en-v1.5
- LLM：Llama-3-8B
- 向量存储：Chroma
- 图/代理：LangGraph

```bash
! pip install -U langchain-nomic langchain_community tiktoken langchainhub chromadb langchain langgraph tavily-python gpt4all fastembed
```

![](.03_Agent_RAG_路由_加_多步推理_images/工作流图.png)

# 参考

[1] 使用 LangGraph 构建可靠的 RAG 代理， https://mp.weixin.qq.com/s/Fc6iZ2tQLzGkVyPke-g2BQ