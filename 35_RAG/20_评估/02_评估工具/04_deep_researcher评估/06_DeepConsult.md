- Github (48 stars):  https://github.com/youdotcom-oss/ydc-deep-research-evals

评估是通过将生成的研究报告与参考报告（在我们的例子中是 OpenAI 的深度研究成果）进行比较来进行的，涉及四个关键维度：

- 指令遵循：评估响应对用户指定的指令和约束的保真度。
- 全面性：衡量响应所涵盖信息的广度和范围，解决用户请求的范围。
- 完整性：衡量报告中涉及的主题的信息的深度和彻底性。
- 写作质量：评估报告的清晰度、简洁性、逻辑组织性和整体可读性。
- 这些维度与深度研究工具在分析推理、信息综合和生成富有洞察力的研究报告方面有效的能力相一致。

DeepConsult 数据集
我们将 DeepConsult 数据集包含在目录中，该数据集包括：datasets/DeepConsult

queries.csv- 专为深入研究而设计的与业务和咨询相关的提示的集合。这些查询涵盖广泛的主题，包括：

市场分析和投资机会
行业特定评估
财务建模和评估
技术趋势分析
战略业务规划
responses_OpenAI-DeepResearch_vs_ARI_2025-05-15.csv- 此文件包含来自 OpenAI DeepResearch 和 ARI 的响应，这些响应专门用于评估脚本。该文件遵循 evals 脚本所需的格式：

question：原始研究问题/提示
baseline_answer：来自 OpenAI 深度研究能力的回复（用作参考）
candidate_answer：根据基线评估 ARI 的响应
该数据集旨在对语言模型对复杂的业务和咨询查询进行深入研究的能力进行基准测试和评估，评估其提供与专业咨询报告相媲美的全面、结构良好和富有洞察力的分析的能力。
