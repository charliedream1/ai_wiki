# 1. 简介

参考：https://www.langchain.com.cn/use_cases/query_analysis/techniques/hyde

Hypothetical Document Embeddings
如果我们正在使用基于相似性搜索的索引，比如向量存储，那么直接搜索原始问题可能效果不佳，因为它们的嵌入可能与相关文档的嵌入不太相似。因此，通过生成一个假设的相关文档，然后使用它进行相似性搜索可能会有所帮助。这是Hypothetical Document Embedding(opens in a new tab)（简称HyDE）的核心思想。

让我们来看一下如何通过假设文档来执行我们的Q&A机器人对LangChain YouTube视频的搜索。

# 2. 使用

```bash
# %pip install -qU langchain langchain-openai
```

```python
import getpass
import os
 
os.environ["OPENAI_API_KEY"] = getpass.getpass()
 
# 如果要使用LangSmith进行追踪，请取消注释以下行。在此注册：https://smith.langchain.com。
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
```

假设文档生成

最终生成一个相关的假设文档的关键在于试图回答用户的问题。由于我们正在为LangChain YouTube视频设计一个Q&A机器人，我们将提供一些关于LangChain的基本背景，并提示模型使用更严谨的风格，以便我们得到更真实的假设文档：

```python
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
 
system = """您是一位专家，掌握了一套用于构建基于LLM的应用程序的软件，该软件称为LangChain、LangGraph、LangServe和LangSmith。
 
LangChain是一个Python框架，提供了一系列可以轻松组合构建LLM应用程序的集成。
LangGraph是建立在LangChain之上的Python软件包，可以轻松构建具有状态的多参与者LLM应用程序。
LangServe是建立在LangChain之上的Python软件包，可以轻松将LangChain应用程序部署为REST API。
LangSmith是一个平台，可以轻松追踪和测试LLM应用程序。
 
尽力回答用户问题。回答时，撰写一篇针对用户问题的教程样式的文章。"""
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
qa_no_context = prompt | llm | StrOutputParser()
```

返回假设文档和原始问题

为了增加我们的召回率，我们可能希望基于假设文档和原始问题检索文档。我们可以很容易地同时返回两者，如下所示：

```python
from langchain_core.runnables import RunnablePassthrough
 
hyde_chain = RunnablePassthrough.assign(hypothetical_document=qa_no_context)
 
hyde_chain.invoke(
    {
        "question": "如何在链中使用多模态模型并将链转成REST API"
    }
)
```

