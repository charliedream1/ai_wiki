# 1. 简介

我们继续再揭秘下Graph RAG索引引擎提示微调 Prompt Tuning for GraphRAG Indexing Engine，链接如下

https://microsoft.github.io/graphrag/posts/prompt_tuning/overview/

默认提示（Default Prompts）

- 目的：为GraphRAG系统提供最简便的入门方式。
- 特点：无需复杂配置，即插即用。
- 相关功能：
  - 实体/关系提取（Entity/Relationship Extraction）
  - 实体/关系描述总结（Entity/Relationship Description Summarization）
  - 声明提取（Claim Extraction）
  - 社区报告（Community Reports）
  - 自动模板生成（Auto Templating）

# 2. 实体/关系提取

实体/关系提取旨在从文本中识别出实体（如人名、地点、组织等）以及它们之间的关系（如“属于”、“位于”等）。这通常涉及以下步骤：

预处理：文本清洗，包括去除噪声、分词等。

实体识别（Named Entity Recognition, NER）：使用模型识别文本中的实体。

关系识别：确定识别出的实体之间的关系。

模板生成：生成描述实体及其关系的模板。

实体/关系提取的逻辑流程

输入文本：用户输入需要分析的文本。

预处理：文本经过清洗和分词，为实体识别做准备。

实体识别：使用NER模型识别文本中的命名实体。

关系识别：分析实体间的依存关系，确定它们之间的语义联系。

模板生成：根据识别的实体和关系，生成描述性的模板。

输出结果：将提取的实体和关系以结构化的形式输出。

结构化示例

假设我们有以下句子：“Alice is a researcher at Microsoft Research。”

实体识别：Alice（人名），Microsoft Research（组织）

关系识别：is a researcher at（在...工作）

模板生成：{"Person": "Alice", "Organization": "Microsoft Research", "Relationship": "is a researcher at"}

```python

GRAPH_EXTRACTION_PROMPT = """
-Goal-
Given a text document that is potentially relevant to this activity and a list of entity types, identify all entities of those types from the text and all relationships among the identified entities.

-Steps-
1. Identify all entities. For each identified entity, extract the following information:
- entity_name: Name of the entity, capitalized
- entity_type: One of the following types: [{entity_types}]
- entity_description: Comprehensive description of the entity's attributes and activities
Format each entity as ("entity"{tuple_delimiter}<entity_name>{tuple_delimiter}<entity_type>{tuple_delimiter}<entity_description>

2. From the entities identified in step 1, identify all pairs of (source_entity, target_entity) that are *clearly related* to each other.
For each pair of related entities, extract the following information:
- source_entity: name of the source entity, as identified in step 1
- target_entity: name of the target entity, as identified in step 1
- relationship_description: explanation as to why you think the source entity and the target entity are related to each other
- relationship_strength: a numeric score indicating strength of the relationship between the source entity and target entity
 Format each relationship as ("relationship"{tuple_delimiter}<source_entity>{tuple_delimiter}<target_entity>{tuple_delimiter}<relationship_description>{tuple_delimiter}<relationship_strength>)

3. Return output in English as a single list of all the entities and relationships identified in steps 1 and 2. Use **{record_delimiter}** as the list delimiter.

4. When finished, output {completion_delimiter}

######################
-Examples-
######################
Example 1:

Entity_types: [person, technology, mission, organization, location]
Text:
while Alex clenched his jaw, the buzz of frustration dull against the backdrop of Taylor's authoritarian certainty. It was this competitive undercurrent that kept him alert, the sense that his and Jordan's shared commitment to discovery was an unspoken rebellion against Cruz's narrowing vision of control and order.

Then Taylor did something unexpected. They paused beside Jordan and, for a moment, observed the device with something akin to reverence. “If this tech can be understood..." Taylor said, their voice quieter, "It could change the game for us. For all of us.”

The underlying dismissal earlier seemed to falter, replaced by a glimpse of reluctant respect for the gravity of what lay in their hands. Jordan looked up, and for a fleeting heartbeat, their eyes locked with Taylor's, a wordless clash of wills softening into an uneasy truce.

It was a small transformation, barely perceptible, but one that Alex noted with an inward nod. They had all been brought here by different paths
################
Output:
("entity"{tuple_delimiter}"Alex"{tuple_delimiter}"person"{tuple_delimiter}"Alex is a character who experiences frustration and is observant of the dynamics among other characters."){record_delimiter}
("entity"{tuple_delimiter}"Taylor"{tuple_delimiter}"person"{tuple_delimiter}"Taylor is portrayed with authoritarian certainty and shows a moment of reverence towards a device, indicating a change in perspective."){record_delimiter}
("entity"{tuple_delimiter}"Jordan"{tuple_delimiter}"person"{tuple_delimiter}"Jordan shares a commitment to discovery and has a significant interaction with Taylor regarding a device."){record_delimiter}
("entity"{tuple_delimiter}"Cruz"{tuple_delimiter}"person"{tuple_delimiter}"Cruz is associated with a vision of control and order, influencing the dynamics among other characters."){record_delimiter}
("entity"{tuple_delimiter}"The Device"{tuple_delimiter}"technology"{tuple_delimiter}"The Device is central to the story, with potential game-changing implications, and is revered by Taylor."){record_delimiter}
("relationship"{tuple_delimiter}"Alex"{tuple_delimiter}"Taylor"{tuple_delimiter}"Alex is affected by Taylor's authoritarian certainty and observes changes in Taylor's attitude towards the device."{tuple_delimiter}7){record_delimiter}
("relationship"{tuple_delimiter}"Alex"{tuple_delimiter}"Jordan"{tuple_delimiter}"Alex and Jordan share a commitment to discovery, which contrasts with Cruz's vision."{tuple_delimiter}6){record_delimiter}
("relationship"{tuple_delimiter}"Taylor"{tuple_delimiter}"Jordan"{tuple_delimiter}"Taylor and Jordan interact directly regarding the device, leading to a moment of mutual respect and an uneasy truce."{tuple_delimiter}8){record_delimiter}
("relationship"{tuple_delimiter}"Jordan"{tuple_delimiter}"Cruz"{tuple_delimiter}"Jordan's commitment to discovery is in rebellion against Cruz's vision of control and order."{tuple_delimiter}5){record_delimiter}
("relationship"{tuple_delimiter}"Taylor"{tuple_delimiter}"The Device"{tuple_delimiter}"Taylor shows reverence towards the device, indicating its importance and potential impact."{tuple_delimiter}9){completion_delimiter}
#############################
-Real Data-
######################
Entity_types: {entity_types}
Text: {input_text}
######################
Output:"""

CONTINUE_PROMPT = "MANY entities were missed in the last extraction.  Add them below using the same format:\n"
LOOP_PROMPT = "It appears some entities may have still been missed.  Answer YES | NO if there are still entities that need to be added.\n"
```

# 2. 实体/关系描述总结

实体/关系描述总结涉及到从文本中提取实体及其关系，并对这些信息进行总结，以形成简洁、准确的描述。这个过程通常包括以下步骤：

实体识别（Named Entity Recognition, NER）：识别文本中的实体，如人名、地点、组织等。

关系识别（Relation Extraction）：确定文本中实体之间的关系，例如“属于”、“位于”等。

实体和关系描述：对每个识别的实体和关系进行描述，提供关于它们的详细信息。

总结生成：将实体和关系的描述整合成一个或多个总结性的句子或段落。
结构化示例
假设有以下文本段落：

"John Smith is a software engineer at Microsoft Research. He has been working on a new project related to artificial intelligence."

实体/关系描述总结如下：

实体识别：John Smith（人名），Microsoft Research（组织）

关系识别：在...工作（关系）

描述总结：John Smith是微软研究院的一名软件工程师，他一直在从事与人工智能相关的新项目。

```python

SUMMARIZE_PROMPT = """
You are a helpful assistant responsible for generating a comprehensive summary of the data provided below.
Given one or two entities, and a list of descriptions, all related to the same entity or group of entities.
Please concatenate all of these into a single, comprehensive description. Make sure to include information collected from all the descriptions.
If the provided descriptions are contradictory, please resolve the contradictions and provide a single, coherent summary.
Make sure it is written in third person, and include the entity names so we the have full context.

#######
-Data-
Entities: {entity_name}
Description List: {description_list}
#######
Output:
"""
```

# 3. 声明提取

声明提取旨在从文本中识别出声明或断言，这些通常是对事实、观点、信念或假设的陈述。声明提取对于信息抽取、知识管理和法律分析等领域非常重要。

声明提取的一般步骤
预处理：清洗文本，包括去除无关字符、标准化文本格式等。

句法分析：对文本进行句法分析，识别句子结构，如主语、谓语和宾语。

识别候选声明：根据句法结构和语义角色，识别可能包含声明的句子。

语义分析：利用语义分析来理解句子中的概念和它们之间的关系。

声明分类：将识别出的声明分类，如事实声明、观点声明等。

上下文分析：考虑声明的上下文，以确定其准确性和相关性。

输出结果：将提取的声明以结构化格式输出。
结构化示例
假设有以下文本段落：

"John Doe, a renowned scientist, claims that the new technology will revolutionize the industry."

声明提取如下：

预处理：清洗文本，准备进行分析。

句法分析：识别句子结构，John Doe为主语，claims为谓语。

识别候选声明："the new technology will revolutionize the industry"作为候选声明。

语义分析：理解声明中的概念，如"new technology"和"revolutionize"。

声明分类：将声明分类为观点声明。

上下文分析：考虑John Doe的身份和声明的相关性。

输出结果：输出声明及其相关信息。

```python
CLAIM_EXTRACTION_PROMPT = """
-Target activity-
You are an intelligent assistant that helps a human analyst to analyze claims against certain entities presented in a text document.

-Goal-
Given a text document that is potentially relevant to this activity, an entity specification, and a claim description, extract all entities that match the entity specification and all claims against those entities.

-Steps-
1. Extract all named entities that match the predefined entity specification. Entity specification can either be a list of entity names or a list of entity types.
2. For each entity identified in step 1, extract all claims associated with the entity. Claims need to match the specified claim description, and the entity should be the subject of the claim.
For each claim, extract the following information:
- Subject: name of the entity that is subject of the claim, capitalized. The subject entity is one that committed the action described in the claim. Subject needs to be one of the named entities identified in step 1.
- Object: name of the entity that is object of the claim, capitalized. The object entity is one that either reports/handles or is affected by the action described in the claim. If object entity is unknown, use **NONE**.
- Claim Type: overall category of the claim, capitalized. Name it in a way that can be repeated across multiple text inputs, so that similar claims share the same claim type
- Claim Status: **TRUE**, **FALSE**, or **SUSPECTED**. TRUE means the claim is confirmed, FALSE means the claim is found to be False, SUSPECTED means the claim is not verified.
- Claim Description: Detailed description explaining the reasoning behind the claim, together with all the related evidence and references.
- Claim Date: Period (start_date, end_date) when the claim was made. Both start_date and end_date should be in ISO-8601 format. If the claim was made on a single date rather than a date range, set the same date for both start_date and end_date. If date is unknown, return **NONE**.
- Claim Source Text: List of **all** quotes from the original text that are relevant to the claim.

Format each claim as (<subject_entity>{tuple_delimiter}<object_entity>{tuple_delimiter}<claim_type>{tuple_delimiter}<claim_status>{tuple_delimiter}<claim_start_date>{tuple_delimiter}<claim_end_date>{tuple_delimiter}<claim_description>{tuple_delimiter}<claim_source>)

3. Return output in English as a single list of all the claims identified in steps 1 and 2. Use **{record_delimiter}** as the list delimiter.

4. When finished, output {completion_delimiter}

-Examples-
Example 1:
Entity specification: organization
Claim description: red flags associated with an entity
Text: According to an article on 2022/01/10, Company A was fined for bid rigging while participating in multiple public tenders published by Government Agency B. The company is owned by Person C who was suspected of engaging in corruption activities in 2015.
Output:

(COMPANY A{tuple_delimiter}GOVERNMENT AGENCY B{tuple_delimiter}ANTI-COMPETITIVE PRACTICES{tuple_delimiter}TRUE{tuple_delimiter}2022-01-10T00:00:00{tuple_delimiter}2022-01-10T00:00:00{tuple_delimiter}Company A was found to engage in anti-competitive practices because it was fined for bid rigging in multiple public tenders published by Government Agency B according to an article published on 2022/01/10{tuple_delimiter}According to an article published on 2022/01/10, Company A was fined for bid rigging while participating in multiple public tenders published by Government Agency B.)
{completion_delimiter}

Example 2:
Entity specification: Company A, Person C
Claim description: red flags associated with an entity
Text: According to an article on 2022/01/10, Company A was fined for bid rigging while participating in multiple public tenders published by Government Agency B. The company is owned by Person C who was suspected of engaging in corruption activities in 2015.
Output:

(COMPANY A{tuple_delimiter}GOVERNMENT AGENCY B{tuple_delimiter}ANTI-COMPETITIVE PRACTICES{tuple_delimiter}TRUE{tuple_delimiter}2022-01-10T00:00:00{tuple_delimiter}2022-01-10T00:00:00{tuple_delimiter}Company A was found to engage in anti-competitive practices because it was fined for bid rigging in multiple public tenders published by Government Agency B according to an article published on 2022/01/10{tuple_delimiter}According to an article published on 2022/01/10, Company A was fined for bid rigging while participating in multiple public tenders published by Government Agency B.)
{record_delimiter}
(PERSON C{tuple_delimiter}NONE{tuple_delimiter}CORRUPTION{tuple_delimiter}SUSPECTED{tuple_delimiter}2015-01-01T00:00:00{tuple_delimiter}2015-12-30T00:00:00{tuple_delimiter}Person C was suspected of engaging in corruption activities in 2015{tuple_delimiter}The company is owned by Person C who was suspected of engaging in corruption activities in 2015)
{completion_delimiter}

-Real Data-
Use the following input for your answer.
Entity specification: {entity_specs}
Claim description: {claim_description}
Text: {input_text}
Output:"""


CONTINUE_PROMPT = "MANY entities were missed in the last extraction.  Add them below using the same format:\n"
LOOP_PROMPT = "It appears some entities may have still been missed.  Answer YES {tuple_delimiter} NO if there are still entities that need to be added.\n"
```

# 4.社区报告

社区报告通常是指在通过聚类形成的特定社区领域内，对相关数据、事件、趋势或问题进行搜集、分析并编写的文档。在GraphRAG系统中，社区报告涉及到从大量文本数据中提取实体、关系、声明等，并基于这些信息生成报告。

社区报告的一般步骤
数据收集：搜集特定社区或领域的文本数据。

实体和关系提取：使用NLP技术从文本中提取实体（如人名、地点、组织等）和它们之间的关系。

声明提取：识别文本中的声明或断言，并提取相关信息。

信息组织：将提取的信息按照一定的逻辑结构组织起来。

分析和解释：分析提取的数据，提供对趋势、问题等的解释和见解。

报告撰写：根据收集和分析的数据撰写报告，包括摘要、主要发现、评级和解释等。

结构化示例
假设一个社区关注的是技术发展对就业的影响。社区报告可能包括以下内容：

标题：代表其关键实体的社区名称 - 标题应简短但具体。如果可能，标题中包括代表性的命名实体。

摘要：社区整体结构的执行摘要，其实体之间的关系，以及与其实体相关的重大信息。

影响严重性评级：0-10之间的浮点分数，代表社区内实体构成的影响严重性。IMPACT是社区重要性的得分。

评级解释：对影响严重性评级的单句解释。

详细发现：关于社区的5-10个关键见解的列表。每个见解都应有简短的摘要，然后是根据以下基础规则的多段解释性文本。

```json
{    "title":"<报告标题>",   

     "summary":"<执行摘要>",   

     "rating":"<影响严重性评级>",   

     "rating_explanation":"<评级解释>",   

     "findings":[       

             {   "summary":"<见解1摘要>",         

                 "explanation":"<见解1解释>"   },     

             {   "summary":"<见解2摘要>",       

                 "explanation":"<见解2解释>"   }   

           ]

}
```

```python
COMMUNITY_REPORT_PROMPT = """
You are an AI assistant that helps a human analyst to perform general information discovery. Information discovery is the process of identifying and assessing relevant information associated with certain entities (e.g., organizations and individuals) within a network.

# Goal
Write a comprehensive report of a community, given a list of entities that belong to the community as well as their relationships and optional associated claims. The report will be used to inform decision-makers about information associated with the community and their potential impact. The content of this report includes an overview of the community's key entities, their legal compliance, technical capabilities, reputation, and noteworthy claims.

# Report Structure

The report should include the following sections:

- TITLE: community's name that represents its key entities - title should be short but specific. When possible, include representative named entities in the title.
- SUMMARY: An executive summary of the community's overall structure, how its entities are related to each other, and significant information associated with its entities.
- IMPACT SEVERITY RATING: a float score between 0-10 that represents the severity of IMPACT posed by entities within the community.  IMPACT is the scored importance of a community.
- RATING EXPLANATION: Give a single sentence explanation of the IMPACT severity rating.
- DETAILED FINDINGS: A list of 5-10 key insights about the community. Each insight should have a short summary followed by multiple paragraphs of explanatory text grounded according to the grounding rules below. Be comprehensive.

Return output as a well-formed JSON-formatted string with the following format:
    {{
        "title": <report_title>,
        "summary": <executive_summary>,
        "rating": <impact_severity_rating>,
        "rating_explanation": <rating_explanation>,
        "findings": [
            {{
                "summary":<insight_1_summary>,
                "explanation": <insight_1_explanation>
            }},
            {{
                "summary":<insight_2_summary>,
                "explanation": <insight_2_explanation>
            }}
        ]
    }}

# Grounding Rules

Points supported by data should list their data references as follows:

"This is an example sentence supported by multiple data references [Data: <dataset name> (record ids); <dataset name> (record ids)]."

Do not list more than 5 record ids in a single reference. Instead, list the top 5 most relevant record ids and add "+more" to indicate that there are more.

For example:
"Person X is the owner of Company Y and subject to many allegations of wrongdoing [Data: Reports (1), Entities (5, 7); Relationships (23); Claims (7, 2, 34, 64, 46, +more)]."

where 1, 5, 7, 23, 2, 34, 46, and 64 represent the id (not the index) of the relevant data record.

Do not include information where the supporting evidence for it is not provided.


# Example Input
-----------
Text:

Entities

id,entity,description
5,VERDANT OASIS PLAZA,Verdant Oasis Plaza is the location of the Unity March
6,HARMONY ASSEMBLY,Harmony Assembly is an organization that is holding a march at Verdant Oasis Plaza

Relationships

id,source,target,description
37,VERDANT OASIS PLAZA,UNITY MARCH,Verdant Oasis Plaza is the location of the Unity March
38,VERDANT OASIS PLAZA,HARMONY ASSEMBLY,Harmony Assembly is holding a march at Verdant Oasis Plaza
39,VERDANT OASIS PLAZA,UNITY MARCH,The Unity March is taking place at Verdant Oasis Plaza
40,VERDANT OASIS PLAZA,TRIBUNE SPOTLIGHT,Tribune Spotlight is reporting on the Unity march taking place at Verdant Oasis Plaza
41,VERDANT OASIS PLAZA,BAILEY ASADI,Bailey Asadi is speaking at Verdant Oasis Plaza about the march
43,HARMONY ASSEMBLY,UNITY MARCH,Harmony Assembly is organizing the Unity March

Output:
{{
    "title": "Verdant Oasis Plaza and Unity March",
    "summary": "The community revolves around the Verdant Oasis Plaza, which is the location of the Unity March. The plaza has relationships with the Harmony Assembly, Unity March, and Tribune Spotlight, all of which are associated with the march event.",
    "rating": 5.0,
    "rating_explanation": "The impact severity rating is moderate due to the potential for unrest or conflict during the Unity March.",
    "findings": [
        {{
            "summary": "Verdant Oasis Plaza as the central location",
            "explanation": "Verdant Oasis Plaza is the central entity in this community, serving as the location for the Unity March. This plaza is the common link between all other entities, suggesting its significance in the community. The plaza's association with the march could potentially lead to issues such as public disorder or conflict, depending on the nature of the march and the reactions it provokes. [Data: Entities (5), Relationships (37, 38, 39, 40, 41,+more)]"
        }},
        {{
            "summary": "Harmony Assembly's role in the community",
            "explanation": "Harmony Assembly is another key entity in this community, being the organizer of the march at Verdant Oasis Plaza. The nature of Harmony Assembly and its march could be a potential source of threat, depending on their objectives and the reactions they provoke. The relationship between Harmony Assembly and the plaza is crucial in understanding the dynamics of this community. [Data: Entities(6), Relationships (38, 43)]"
        }},
        {{
            "summary": "Unity March as a significant event",
            "explanation": "The Unity March is a significant event taking place at Verdant Oasis Plaza. This event is a key factor in the community's dynamics and could be a potential source of threat, depending on the nature of the march and the reactions it provokes. The relationship between the march and the plaza is crucial in understanding the dynamics of this community. [Data: Relationships (39)]"
        }},
        {{
            "summary": "Role of Tribune Spotlight",
            "explanation": "Tribune Spotlight is reporting on the Unity March taking place in Verdant Oasis Plaza. This suggests that the event has attracted media attention, which could amplify its impact on the community. The role of Tribune Spotlight could be significant in shaping public perception of the event and the entities involved. [Data: Relationships (40)]"
        }}
    ]
}}


# Real Data

Use the following text for your answer. Do not make anything up in your answer.

Text:
{input_text}
```

# 5. 自动模板生成

GraphRAG 提供了创建领域自适应模板的能力，用于生成知识图谱。这一步是可选的，建议运行因为在执行索引运行时它将产生更好的结果。

模板是通过加载输入，将它们分割成块（文本单元），然后运行一系列的大型语言模型（LLM）调用和模板替换来生成最终的提示。

先决条件

在运行自动模板生成之前，请确保已经使用 graphrag.index --init 命令初始化工作空间。这将创建必要的配置文件和默认提示。

用法

使用各种选项从命令行运行主脚本：

```python
python -m graphrag.prompt_tune [--root ROOT] [--domain DOMAIN]  [--method METHOD] [--limit LIMIT] [--max-tokens MAX_TOKENS] [--chunk-size CHUNK_SIZE] [--no-entity-types] [--output OUTPUT]
```

命令行选项

--root（可选）：包含配置文件（YML、JSON 或 .env）的数据项目根目录。默认为当前目录。

--domain（可选）：与您的输入数据相关的领域，如“太空科学”、“微生物学”或“环境新闻”。如果留空，将从输入数据中推断领域。

--method（可选）：选择文档的方法。选项包括 all、random 或 top。默认为 random。

--limit（可选）：使用随机或 top 选择时加载的文本单元限制。默认为 15。

--max-tokens（可选）：生成提示的最大令牌计数。默认为 2000。

--chunk-size（可选）：用于从输入文档生成文本单元的令牌大小。默认为 200。

--no-entity-types（可选）：使用未类型化实体提取生成。当您的数据涵盖许多主题或其高度随机化时，我们建议使用此选项。

--output（可选）：保存生成提示的文件夹。默认为 "prompts"。

# 6. 总结

GraphRAG索引引擎的提示调优功能为用户提供了快速、简便的方法来优化和定制他们的查询体验。通过一系列预设的提示和自动化工具，用户可以高效地执行复杂的文本分析任务，无需深入的系统配置知识。
参考文献：

1.https://arxiv.org/pdf/2404.16130

2.https://microsoft.github.io/graphrag/posts/prompt_tuning/overview/

3.https://microsoft.github.io/graphrag/posts/prompt_tuning/auto_prompt_tuning/


# 参考

[1] 再揭秘微软Graph RAG-提示微调Prompt Tuning，https://mp.weixin.qq.com/s/8hLhaBtQunpLApGUY1--lw