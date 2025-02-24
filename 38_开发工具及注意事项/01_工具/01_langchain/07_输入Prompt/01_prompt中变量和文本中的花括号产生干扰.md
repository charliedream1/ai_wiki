# 问题

```python
INFO_EXTRACTS_PROMPTS = """###新闻###
{doc}

###任务要求###
你是一个新闻信息抽取专家。
- 你需要从上面的新闻抽取信息，抽取要素内容包括subject（主体）、object（客体）、relationship、location。
- 请先进行分析，然后使用json格式输出抽取的主要事件关键要素。对于事件时间，如果无法从文中推断，则填写未知。


输出json样例：
json
{
    "subject": "习近平",
    "object": "普京",
    "relationship": "会见",
    "location": "北京",
}"""
```

大模型调用chain如下：

```python
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate

INFO_EXTRACT_PROMPT_TEMPLATE = PromptTemplate(
    template=INFO_EXTRACTS_PROMPTS,
    input_variables=["doc"],
)
event_extractor_llm = INFO_EXTRACT_PROMPT_TEMPLATE | llm | StrOutputParser()
```

prompt中的json那部分，因为有{}括号，导致本该传入的变量doc出错

# 解决方案

在 Python 的字符串模板中，花括号 {} 被认为是模板的占位符，LangChain 会尝试将 {} 中的内容替换为对应的变量值。这会导致你在 INFO_EXTRACTS_PROMPTS 中使用 JSON 结构时，花括号被误认为是占位符的问题。

为了避免这种问题，可以通过以下方法进行处理：

方法 1: 使用双花括号 {{ 和 }}
在 Python 的字符串模板中，双花括号会被解释为单个花括号。将 JSON 部分的 { 和 } 替换为 {{ 和 }}，例如：

```python
INFO_EXTRACTS_PROMPTS = """###新闻###
{doc}

###任务要求###
你是一个新闻信息抽取专家。
- 你需要从上面的新闻抽取信息，抽取要素内容包括subject（主体）、object（客体）、relationship、location。
- 请先进行分析，然后使用json格式输出抽取的主要事件关键要素。对于事件时间，如果无法从文中推断，则填写未知。

输出json样例：
json
{{
    "subject": "习近平",
    "object": "普京",
    "relationship": "会见",
    "location": "北京",
}}"""
```
