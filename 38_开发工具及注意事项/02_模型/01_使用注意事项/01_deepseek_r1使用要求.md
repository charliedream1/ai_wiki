# 资源

together.ai文档：https://docs.together.ai/docs/deepseek-r1

# 1. deepseek注意事项

- 清晰且具体的提示语 (prompts)： 使用简洁明了的语言编写指令，明确表达你的需求。复杂冗长的提示语往往效果不佳。
- 采样参数： 建议将 temperature (温度系数) 设置在 0.5-0.7 之间 (推荐值 0.6)，以避免模型产生重复或不连贯的输出。同时，top-p (概率截断) 建议设置为 0.95。
- 避免使用系统提示 (system prompt)： 不要添加额外的系统提示语，所有指令都应包含在用户提示语中。
- 避免使用少量样本提示 (few-shot prompting)： 不要在提示语中提供任何示例，因为这会降低模型的性能。相反，请详细描述你希望模型解决的问题、执行的任务以及输出的格式。如果确实需要提供示例，请确保示例与你的提示语要求高度一致。
- 组织你的提示语： 使用清晰的标记 (例如 XML 标签、Markdown 格式或带有标签的段落) 来分解提示语的不同组成部分。 这种结构化的组织方式有助于模型正确理解和处理你的每一个请求。
- 设置明确的要求： 当你的请求存在特定限制或标准时，请明确地进行说明 (例如 “每行文本的朗读时间不应超过 5 秒…”)。 无论是预算限制、时间限制还是特定的格式要求，都应清晰地概述这些参数，以便引导模型生成符合要求的回复。
- 清晰地描述输出： 详细描述你期望的输出结果。 描述具体的特征或质量，以便模型生成完全符合你需求的响应，并朝着满足这些标准的方向努力。
- 多数投票选择回复： 在评估模型性能时，建议生成多个解决方案，然后选择出现频率最高的结果。
- 避免使用思维链提示 (chain-of-thought prompting)： 由于这类模型在回答问题之前会自主进行推理，因此无需指示它们“逐步思考……”
- 数学任务： 对于数学问题，建议在提示语中添加如下指令：“请逐步进行逻辑推理，并将最终答案置于 \boxed{} 中。”
- 强制使用 <think> 标签： 极少数情况下，DeepSeek-R1 可能会跳过思考过程，从而对模型性能产生负面影响。 在这种情况下，模型输出的响应将不会以 <think> 标签开头。 如果你遇到此问题，可以尝试引导模型以 <think> 标签开头。

目前，DeepSeek-R1 在通用任务方面的功能不如 DeepSeek-V3，例如：

- 函数调用
- 多轮次对话
- 复杂的角色扮演
- JSON 输出。

这是因为长时间的 CoT 强化学习训练没有针对这些通用任务进行优化，因此对于这些任务，您应该使用其他模型。

# 2. 文件上传场景提示模板 (File upload):

```python
file_template = \
"""[file name]: {file_name}
[file content begin]
{file_content}
[file content end]
{question}"""
```

# 3. 网络搜索场景提示模板 (Web search):

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

# 4. 使用场景

**推理模型与非推理模型**

推理模型的训练方式与非推理模型截然不同，因此它们的作用不同。下面我们将比较这两种类型的模型、推理模型的详细信息、优缺点、应用和示例用例。

像这样的推理模型是专门为对复杂挑战进行广泛、深入的分析而开发的。他们的优势在于战略思维、为复杂问题开发综合解决方案以及处理大量细微信息以做出决策。它们的高精度和准确性使其在传统上需要人类专业知识的专业领域（如数学、科学研究、法律工作、医疗保健、金融分析）中特别有价值。DeepSeek-R1

非推理模型（例如 OR 经过训练）可以高效、直接地执行任务，同时具有更快的响应时间和更好的成本效益。Llama 3.3 70BDeepSeek-V3

您的应用程序可以利用这两种类型的模型：使用 DeepSeek-R1 开发战略框架和问题解决方法，同时部署非推理模型来处理快速执行和成本考虑超过绝对精度需求的特定任务。

**推理模型用例**

- 分析和评估 AI 模型输出
  
  推理模型擅长评估来自其他系统的响应，尤其是在数据验证场景中。这在法律等关键领域变得特别有价值，在这些领域中，这些模型可以应用上下文理解，而不仅仅是遵循严格的验证规则。

- 代码分析和改进

  推理模型非常擅长进行全面的代码审查，并跨大型代码库提出改进建议。它们处理大量代码的能力使其对于全面的审查流程特别有价值。

- 战略规划和任务委派

  这些模型在创建详细的多阶段计划并根据特定要求（如任务所需的处理速度或分析深度）确定每个阶段最合适的 AI 模型方面大放异彩。

- 复杂文档分析和模式识别

  这些模型擅长处理和分析广泛的非结构化文档，例如合同协议、法律报告和医疗保健文档。他们特别擅长识别不同文档之间的联系并建立联系。

- 精确信息提取

  在处理大量非结构化数据时，这些模型擅长精确定位和提取回答特定查询所需的相关信息，从而有效地过滤掉搜索和检索过程中的噪音。这使得它们非常适合用于 RAG 或 LLM 增强的互联网搜索用例。

- 处理不明确的指令

  这些模型特别擅长处理不完整或模棱两可的信息。他们可以有效地解释用户的意图，并在面临信息差距时主动寻求澄清，而不是做出假设。

**优点和缺点**

推理模型非常适合您需要以下任务：

- 高精度和可靠的决策能力
- 涉及多个变量和模糊数据的复杂问题的解决方案
- 可以承受更高的查询延迟
- 每个任务的成本/代币预算更高

当您需要时，非推理模型是最佳选择：

- 更快的处理速度（更低的整体查询延迟）和更低的运营成本
- 执行明确、简单的任务
- 函数调用、JSON 模式或其他结构良好的任务

# 参考

[1] DeepSeek-R1 官方提示词和参数配置：部署开源671B与DeepSeek官方表现一致, https://www.aisharenet.com/deepseek-r1-guanfangan/