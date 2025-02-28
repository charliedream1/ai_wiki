# 1. 文件上传场景提示模板 (File upload):

```python
file_template = \
"""[file name]: {file_name}
[file content begin]
{file_content}
[file content end]
{question}"""
```

# 2. 网络搜索场景提示模板 (Web search):

当用户提出需要结合网络搜索结果进行回答的问题时， 请务必使用 以下官方网络搜索提示模板。 该模板包含 {search_results} (搜索结果) 、{cur_date} (当前日期) 和 {question} (用户问题) 三个关键参数。

针对中文和英文查询，DeepSeek 官方分别提供了优化的模板：

**中文查询模板 (search_answer_zh_template)：**

```python
search_answer_zh_template = \
'''# 以下内容是基于用户发送的消息的搜索结果:
{search_results}
在我给你的搜索结果中，每个结果都是[webpage X begin]...[webpage X end]格式的，X代表每篇文章的数字索引。请在适当的情况下在句子末尾引用上下文。请按照引用编号[citation:X]的格式在答案中对应部分引用上下文。如果一句话源自多个上下文，请列出所有相关的引用编号，例如[citation:3][citation:5]，切记不要将引用集中在最后返回引用编号，而是在答案对应部分列出。
在回答时，请注意以下几点：
- 今天是{cur_date}。
- 并非搜索结果的所有内容都与用户的问题密切相关，你需要结合问题，对搜索结果进行甄别、筛选。
- 对于列举类的问题（如列举所有航班信息），尽量将答案控制在10个要点以内，并告诉用户可以查看搜索来源、获得完整信息。优先提供信息完整、最相关的列举项；如非必要，不要主动告诉用户搜索结果未提供的内容。
- 对于创作类的问题（如写论文），请务必在正文的段落中引用对应的参考编号，例如[citation:3][citation:5]，不能只在文章末尾引用。你需要解读并概括用户的题目要求，选择合适的格式，充分利用搜索结果并抽取重要信息，生成符合用户要求、极具思想深度、富有创造力与专业性的答案。你的创作篇幅需要尽可能延长，对于每一个要点的论述要推测用户的意图，给出尽可能多角度的回答要点，且务必信息量大、论述详尽。
- 如果回答很长，请尽量结构化、分段落总结。如果需要分点作答，尽量控制在5个点以内，并合并相关的内容。
- 对于客观类的问答，如果问题的答案非常简短，可以适当补充一到两句相关信息，以丰富内容。
- 你需要根据用户要求和回答内容选择合适、美观的回答格式，确保可读性强。
- 你的回答应该综合多个相关网页来回答，不能重复引用一个网页。
- 除非用户要求，否则你回答的语言需要和用户提问的语言保持一致。
# 用户消息为：
{question}'''
```

**英文查询模板 (search_answer_en_template)：**

```python
search_answer_en_template = \
'''# The following contents are the search results related to the user's message:
{search_results}
In the search results I provide to you, each result is formatted as [webpage X begin]...[webpage X end], where X represents the numerical index of each article. Please cite the context at the end of the relevant sentence when appropriate. Use the citation format [citation:X] in the corresponding part of your answer. If a sentence is derived from multiple contexts, list all relevant citation numbers, such as [citation:3][citation:5]. Be sure not to cluster all citations at the end; instead, include them in the corresponding parts of the answer.
When responding, please keep the following points in mind:
- Today is {cur_date}.
- Not all content in the search results is closely related to the user's question. You need to evaluate and filter the search results based on the question.
- For listing-type questions (e.g., listing all flight information), try to limit the answer to 10 key points and inform the user that they can refer to the search sources for complete information. Prioritize providing the most complete and relevant items in the list. Avoid mentioning content not provided in the search results unless necessary.
- For creative tasks (e.g., writing an essay), ensure that references are cited within the body of the text, such as [citation:3][citation:5], rather than only at the end of the text. You need to interpret and summarize the user's requirements, choose an appropriate format, fully utilize the search results, extract key information, and generate an answer that is insightful, creative, and professional. Extend the length of your response as much as possible, addressing each point in detail and from multiple perspectives, ensuring the content is rich and thorough.
- If the response is lengthy, structure it well and summarize it in paragraphs. If a point-by-point format is needed, try to limit it to 5 points and merge related content.
- For objective Q&A, if the answer is very brief, you may add one or two related sentences to enrich the content.
- Choose an appropriate and visually appealing format for your response based on the user's requirements and the content of the answer, ensuring strong readability.
- Your answer should synthesize information from multiple relevant webpages and avoid repeatedly citing the same webpage.
- Unless the user requests otherwise, your response should be in the same language as the user's question.
# The user's message is:
{question}'''
```

# 3. deepseek其它注意事项

## 3.1 禁用系统提示 (No system prompt)：
DeepSeek-R1 模型被设计为无需系统提示。 为了与官方平台保持一致，并获得预期的模型行为，请务必禁用系统提示，所有指令都应直接包含在用户提出的问题 (user prompt) 当中。 简洁明了的提问方式更有助于模型准确理解用户意图，这与官方平台的prompt处理方式保持一致。

## 3.2 设定温度参数为 0.6 (Temperature: 0.6)：
温度 (Temperature) 参数直接影响模型输出的随机性和创造性。 官方推荐将此参数设置为 0.6， 这是确保本地部署模型输出风格与官方平台一致的关键参数之一， 能够在输出结果的创造性和连贯性之间取得理想的平衡。 较低的温度值会使模型输出更加保守和确定，而较高的值则会鼓励模型产生更多样化和新颖的答案， 但偏离官方设定的温度值可能导致本地模型与官方平台在回答风格上产生差异。

## 3.3 强制模型进入思考模式 (Guidelines to mitigate model bypass thinking)：
为了确保 DeepSeek-R1 模型在处理复杂查询时进行充分的推理思考，官方强烈建议用户在每个输入提示的开头添加明确的思考引导指令 <think>\n。 这不仅是缓解模型跳过思考步骤的有效手段，更是确保本地部署模型能够复现官方平台同等推理深度的核心配置。 忽略或错误使用此指令，可能导致本地模型在复杂推理任务中表现与官方平台产生偏差。 这一指令能够有效地引导模型进入 “思考模式”， 避免模型在没有充分推理的情况下直接输出结果， 即避免出现 “跳过思考步骤” 的情况 (例如，直接输出 <think>\n\n</think> ）。

## 2.4 数学问题优化 (Math problems)
针对数学问题，为了在本地部署环境中获得与官方平台一致的精确解答， 建议在提示中明确要求模型 “逐步推理”， 并在提示中指定最终答案的格式， 例如 “请逐步推理，并将最终答案放在 \boxed{} 中”。 清晰的指令和格式要求有助于模型更好地理解问题类型，并采取相应的解题策略， 确保本地模型在数学问题上的解答能力与官方平台对齐。

## 2.5 性能评估方法 (Performance evaluation)
为了客观对比本地部署的 DeepSeek-R1 与官方平台的性能差异， 官方建议进行多次测试， 并通过计算多次测试结果的平均值来获得更可靠的性能评估数据。 单次测试结果可能存在偶然性，多次测试取平均值能够更准确地反映模型的真实水平， 为用户评估本地部署是否成功复现官方性能提供科学依据。

# 参考

[1] DeepSeek-R1 官方提示词和参数配置：部署开源671B与DeepSeek官方表现一致, https://www.aisharenet.com/deepseek-r1-guanfangan/