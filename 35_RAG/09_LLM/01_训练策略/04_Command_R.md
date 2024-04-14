# 1. 资源

- Cohere公司发布的，针对RAG和工具调用场景，性能匹敌GPT-4
   - 文档：https://docs.cohere.com/docs/retrieval-augmented-generation-rag
   - 模型下载（ModelScope）3.5B：
     - https://modelscope.cn/models/mirror013/c4ai-command-r-v01-4bit/summary
   - 模型下载（ModelScope）104B:
     - https://modelscope.cn/models/AI-ModelScope/c4ai-command-r-plus/summary

# 2. 介绍

## 2.1 Grounded Generation and RAG Capabilities:

Command-R has been specifically trained with grounded generation capabilities. This means that it can generate responses based on a list of supplied document snippets, and it will include grounding spans (citations) in its response indicating the source of the information. This can be used to enable behaviors such as grounded summarization and the final step of Retrieval Augmented Generation (RAG).This behavior has been trained into the model via a mixture of supervised fine-tuning and preference fine-tuning, using a specific prompt template. Deviating from this prompt template may reduce performance, but we encourage experimentation.

Command-R’s grounded generation behavior takes a conversation as input (with an optional user-supplied system preamble, indicating task, context and desired output style), along with a list of retrieved document snippets. The document snippets should be chunks, rather than long documents, typically around 100-400 words per chunk. Document snippets consist of key-value pairs. The keys should be short descriptive strings, the values can be text or semi-structured.

By default, Command-R will generate grounded responses by first predicting which documents are relevant, then predicting which ones it will cite, then generating an answer. Finally, it will then insert grounding spans into the answer. See below for an example. This is referred to as accurate grounded generation.

The model is trained with a number of other answering modes, which can be selected by prompt changes . A fast citation mode is supported in the tokenizer, which will directly generate an answer with grounding spans in it, without first writing the answer out in full. This sacrifices some grounding accuracy in favor of generating fewer tokens.

Comprehensive documentation for working with command-R's grounded generation prompt template can be found here.

The code snippet below shows a minimal working example on how to render a prompt.

Usage: Rendering Grounded Generation prompts

```python
from transformers import AutoTokenizer

model_id = "CohereForAI/c4ai-command-r-v01"
tokenizer = AutoTokenizer.from_pretrained(model_id)

# define conversation input:
conversation = [
    {"role": "user", "content": "Whats the biggest penguin in the world?"}
]
# define documents to ground on:
documents = [
    { "title": "Tall penguins", "text": "Emperor penguins are the tallest growing up to 122 cm in height." }, 
    { "title": "Penguin habitats", "text": "Emperor penguins only live in Antarctica."}
]

# render the tool use prompt as a string:
grounded_generation_prompt = tokenizer.apply_grounded_generation_template(
    conversation,
    documents=documents,
    citation_mode="accurate", # or "fast"
    tokenize=False,
    add_generation_prompt=True,
)
print(grounded_generation_prompt)
```

Example Rendered Grounded Generation Prompt

```text
The instructions in this section override those in the task description and style guide sections. Don't answer questions that are harmful or immoral.

# System Preamble
## Basic Rules
You are a powerful conversational AI trained by Cohere to help people. You are augmented by a number of tools, and your job is to use and consume the output of these tools to best help the user. You will see a conversation history between yourself and a user, ending with an utterance from the user. You will then see a specific instruction instructing you what kind of response to generate. When you answer the user's requests, you cite your sources in your answers, according to those instructions.

# User Preamble
## Task and Context
You help people answer their questions and other requests interactively. You will be asked a very wide array of requests on all kinds of topics. You will be equipped with a wide range of search engines or similar tools to help you, which you use to research your answer. You should focus on serving the user's needs as best you can, which will be wide-ranging.

## Style Guide
Unless the user asks for a different style of answer, you should answer in full sentences, using proper grammar and spelling.<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|USER_TOKEN|>Whats the biggest penguin in the world?<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|><results>
Document: 0
title: Tall penguins
text: Emperor penguins are the tallest growing up to 122 cm in height.

Document: 1
title: Penguin habitats
text: Emperor penguins only live in Antarctica.
</results><|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|>Carefully perform the following instructions, in order, starting each with a new line.
Firstly, Decide which of the retrieved documents are relevant to the user's last input by writing 'Relevant Documents:' followed by comma-separated list of document numbers. If none are relevant, you should instead write 'None'.
Secondly, Decide which of the retrieved documents contain facts that should be cited in a good answer to the user's last input by writing 'Cited Documents:' followed a comma-separated list of document numbers. If you dont want to cite any of them, you should instead write 'None'.
Thirdly, Write 'Answer:' followed by a response to the user's last input in high quality natural english. Use the retrieved documents to help you. Do not insert any citations or grounding markup.
Finally, Write 'Grounded answer:' followed by a response to the user's last input in high quality natural english. Use the symbols <co: doc> and </co: doc> to indicate when a fact comes from a document in the search result, e.g <co: 0>my fact</co: 0> for a fact from document 0.<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>
```

Example Rendered Grounded Generation Completion

```text
Relevant Documents: 0,1
Cited Documents: 0,1
Answer: The Emperor Penguin is the tallest or biggest penguin in the world. It is a bird that lives only in Antarctica and grows to a height of around 122 centimetres.
Grounded answer: The <co: 0>Emperor Penguin</co: 0> is the <co: 0>tallest</co: 0> or biggest penguin in the world. It is a bird that <co: 1>lives only in Antarctica</co: 1> and <co: 0>grows to a height of around 122 centimetres.</co: 0>
```

## 2.2 Pipeline

request

```python
import cohere
co = cohere.Client(<YOUR API KEY>)

co.chat(
  model="command",
  message="Where do the tallest penguins live?",
  documents=[
    {"title": "Tall penguins", "snippet": "Emperor penguins are the tallest."},
    {"title": "Penguin habitats", "snippet": "Emperor penguins only live in Antarctica."},
    {"title": "What are animals?", "snippet": "Animals are different from plants."}
  ])
```

response

```python
{
  "text": "The tallest penguins, Emperor penguins, live in Antarctica.",  
  "citations": [  
    {"start": 22, "end": 38, "text": "Emperor penguins", "document_ids": ["doc_0"]},  
    {"start": 48, "end": 59, "text": "Antarctica.", "document_ids": ["doc_1"]}  
  ],  
  "documents": [  
    {"id": "doc_0", "title": "Tall penguins", "snippet": "Emperor penguins are the tallest.", "url": ""},  
    {"id": "doc_1", "title": "Penguin habitats", "snippet": "Emperor penguins only live in Antarctica.", "url": ""}  
  ] 
}
```

Three steps of RAG
The RAG workflow generally consists of 3 steps:

Generating search queries for finding relevant documents. What does the model recommend looking up before answering this question?
Fetching relevant documents from an external data source using the generated search queries. Performing a search to find some relevant information.
Generating a response with inline citations using the fetched documents. Using the acquired knowledge to produce an educated answer.
Example: Using RAG to identify the definitive 90s boy band
In this section, we will use the three step RAG workflow to finally settle the score between the notorious boy bands Backstreet Boys and NSYNC. We ask the model to provide an informed answer to the question "Who is more popular: Nsync or Backstreet Boys?"

Step 1: Generating search queries
Calling the Chat API with the search_queries_only parameter set to True will return a list of search queries. In the example below, we ask the model to suggest some search queries that would be useful when answering the question.

Request

```python
import cohere
co = cohere.Client(<YOUR API KEY>)

co.chat(
  message="Who is more popular: Nsync or Backstreet Boys?",
  search_queries_only=True
)
```

Response

```python
{
  "is_search_required": true,
  "search_queries": [
    {"text": "Nsync popularity", "generation_id": "b560dd68-743e-4c32-98a2-a9b7e3e96861"},
    {"text": "Backstreet Boys popularity", "generation_id": "b560dd68-743e-4c32-98a2-a9b7e3e96861"}
  ]
}
```

Indeed, to generate a factually accurate answer to the question "Who is more popular: Nsync or Backstreet Boys?", looking up Nsync popularity and Backstreet Boys popularity first would be helpful.

Step 2: Fetching relevant documents
The next step is to fetch documents from the relevant data source using the generated search queries. For example, to answer the question about the two pop sensations NSYNC and Backstreet Boys, one might want to use an API from a web search engine, and fetch the contents of the websites listed at the top of the search results.

We won't go into details of fetching data in this guide, since it's very specific to the search API you're querying. However we should mention that breaking up long documents into smaller ones first (1-2 paragraphs) will help you not go over the context limit. When trying to stay within the context length limit, you might need to omit some of the documents from the request. To make sure that only the least relevant documents are omitted, we recommend using the Rerank endpoint endpoint which will sort the documents by relevancy to the query. The lowest ranked documents are the ones you should consider dropping first.

Step 3: Generating a response
In the final step, we will be calling the Chat API again, but this time passing along the documents you acquired in Step 2. A document object is a dictionary containing the content and the metadata of the text. We recommend using a few descriptive keys such as "title", "snippet", or "last updated" and only including semantically relevant data. The keys and the values will be formatted into the prompt and passed to the model.

Request

```python
import cohere
co = cohere.Client(<YOUR API KEY>)

co.chat(
  model="command",
  message="Who is more popular: Nsync or Backstreet Boys?",
  documents=[
    {
      "title": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
      "snippet": "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: Backstreet Boys Popularity Analysis\n\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\n\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\n\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak."
    },
    {
      "title": "CSPC: NSYNC Popularity Analysis - ChartMasters",
      "snippet": "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: NSYNC Popularity Analysis\n\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync\n\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\n\nIt wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold."
    },
    {
      "title": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
      "snippet": " 1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\n\nYet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\n\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers."
    },
    {
      "title": "CSPC: NSYNC Popularity Analysis - ChartMasters",
      "snippet": " Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\n\nAs usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures."
    }
  ])
```

Response

```python
{
  "text": "Both the Backstreet Boys and *NSYNC enjoyed immense popularity during the late 1990s and early 2000s. \n\nThe Backstreet Boys, with massive album sales, chart-topping releases and highly successful tours, dominated the music industry for several years worldwide. They sold millions of copies of their albums No Strings Attached and Celebrity, breaking even the sales records of Adele and ranking as the second-fastest-selling album of the Soundscan era before 2015. \n\n*NSYNC, led by Justin Timberlake, also achieved tremendous success, selling millions of copies of their albums and finding popularity not just in the US but globally. \n\nHowever, when comparing the two groups, the extent of the Backstreet Boys' success puts them at a significantly higher level. They dominated the industry for several years, achieving unparalleled success in traditionally non-Western markets. Therefore, I can conclude that the Backstreet Boys are the more popular group.",
  "citations": [
    { "start": 44, "end": 101, "text": "immense popularity during the late 1990s and early 2000s.", "document_ids": ["doc_0", "doc_1", "doc_2"]},
    { "start": 130, "end": 201, "text": "massive album sales, chart-topping releases and highly successful tours", "document_ids": ["doc_0"]},
    // ...
  ],
  "documents": [
    { "id": "doc_0", "snippet": "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: Backstreet Boys Popularity Analysis\n\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\n\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\n\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak.", "title": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters"},
    { "id": "doc_1", "snippet": "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: NSYNC Popularity Analysis\n\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync\n\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\n\nIt wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold.", "title": "CSPC: NSYNC Popularity Analysis - ChartMasters"},
    //...
  ]
}
```

# 参考

[1] https://modelscope.cn/models/AI-ModelScope/c4ai-command-r-v01/summary
[2] Retrieval Augmented Generation (RAG)，https://docs.cohere.com/docs/retrieval-augmented-generation-rag
