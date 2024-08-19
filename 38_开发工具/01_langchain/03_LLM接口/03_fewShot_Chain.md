参考：
- https://python.langchain.com/v0.2/docs/how_to/few_shot_examples/
- RAG及few shot: https://www.langchain.com.cn/use_cases/query_analysis/how_to/few_shot

few shot

```python
from langchain_core.prompts import PromptTemplate

example_prompt = PromptTemplate.from_template("Question: {question}\n{answer}")

examples = [
    {
        "question": "Who lived longer, Muhammad Ali or Alan Turing?",
        "answer": """
Are follow up questions needed here: Yes.
Follow up: How old was Muhammad Ali when he died?
Intermediate answer: Muhammad Ali was 74 years old when he died.
Follow up: How old was Alan Turing when he died?
Intermediate answer: Alan Turing was 41 years old when he died.
So the final answer is: Muhammad Ali
""",
    },
    {
        "question": "When was the founder of craigslist born?",
        "answer": """
Are follow up questions needed here: Yes.
Follow up: Who was the founder of craigslist?
Intermediate answer: Craigslist was founded by Craig Newmark.
Follow up: When was Craig Newmark born?
Intermediate answer: Craig Newmark was born on December 6, 1952.
So the final answer is: December 6, 1952
""",
    },
    {
        "question": "Who was the maternal grandfather of George Washington?",
        "answer": """
Are follow up questions needed here: Yes.
Follow up: Who was the mother of George Washington?
Intermediate answer: The mother of George Washington was Mary Ball Washington.
Follow up: Who was the father of Mary Ball Washington?
Intermediate answer: The father of Mary Ball Washington was Joseph Ball.
So the final answer is: Joseph Ball
""",
    },
    {
        "question": "Are both the directors of Jaws and Casino Royale from the same country?",
        "answer": """
Are follow up questions needed here: Yes.
Follow up: Who is the director of Jaws?
Intermediate Answer: The director of Jaws is Steven Spielberg.
Follow up: Where is Steven Spielberg from?
Intermediate Answer: The United States.
Follow up: Who is the director of Casino Royale?
Intermediate Answer: The director of Casino Royale is Martin Campbell.
Follow up: Where is Martin Campbell from?
Intermediate Answer: New Zealand.
So the final answer is: No
""",
    },
]

from langchain_core.prompts import FewShotPromptTemplate

prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"],
)

print(
    prompt.invoke({"input": "Who was the father of Mary Ball Washington?"}).to_string()
)
```

另一个参考示例

我们将定义一个查询模式，希望我们的模型输出这个模式。为了使我们的查询分析更加有趣，我们将添加一个包含从顶级问题派生出的更具体问题的 sub_queries 字段。

```python
from typing import List, Optional
 
from langchain_core.pydantic_v1 import BaseModel, Field
 
sub_queries_description = """\
如果原始问题包含多个不同的子问题，\
或者如果有更通用的问题对于回答原始问题可能有帮助，\
请编写所有相关子问题的列表。\
确保这个列表是全面的，并涵盖原始问题的所有部分。\
子问题中可以有冗余。\
确保子问题的焦点尽可能狭窄。"""
 
 
class Search(BaseModel):
    """搜索有关构建 LLM 引擎应用程序的软件库的教程视频的数据库。"""
 
    query: str = Field(
        ...,
        description="应用于视频转录的主要相似性搜索查询。",
    )
    sub_queries: List[str] = Field(
        default_factory=list, description=sub_queries_description
    )
    publish_year: Optional[int] = Field(None, description="视频的发布年份")

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
 
system = """您是一个将用户问题转换为数据库查询的专家。\
您可以访问一个关于构建 LLM 引擎应用程序的软件库的教程视频的数据库。\
给定一个问题，返回一个优化的数据库查询列表以检索最相关的结果。
 
如果有您不熟悉的首字母缩写或词汇，请不要试图改写它们。"""
 
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        MessagesPlaceholder("examples", optional=True),
        ("human", "{question}"),
    ]
)
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
structured_llm = llm.with_structured_output(Search)
query_analyzer = {"question": RunnablePassthrough()} | prompt | structured_llm

# 添加示例
examples = []
question = "Chat LangChain 是什么，它是 LangChain 模板吗？"
query = Search(
    query="What is chat LangChain and is it a LangChain template?",
    sub_queries=["What is chat LangChain", "What is a LangChain template"],
)
examples.append({"input": question, "tool_calls": [query]})
example_msgs = [msg for ex in examples for msg in tool_example_to_messages(ex)]

from langchain_core.prompts import MessagesPlaceholder
 
query_analyzer_with_examples = (
    {"question": RunnablePassthrough()}
    | prompt.partial(examples=example_msgs)
    | structured_llm
)
```

example select via similarity

```python
from langchain_chroma import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_openai import OpenAIEmbeddings

example_selector = SemanticSimilarityExampleSelector.from_examples(
    # This is the list of examples available to select from.
    examples,
    # This is the embedding class used to produce embeddings which are used to measure semantic similarity.
    OpenAIEmbeddings(),
    # This is the VectorStore class that is used to store the embeddings and do a similarity search over.
    Chroma,
    # This is the number of examples to produce.
    k=1,
)

# Select the most similar example to the input.
question = "Who was the father of Mary Ball Washington?"
selected_examples = example_selector.select_examples({"question": question})
print(f"Examples most similar to the input: {question}")
for example in selected_examples:
    print("\n")
    for k, v in example.items():
        print(f"{k}: {v}")
```
