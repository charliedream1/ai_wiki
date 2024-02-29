问题：

有害或者涉及隐私的问题需要被过滤，否则容易导致大模型越狱。

- 匿名化：对姓名、地址和联系方式匿名化，以保护隐私同时避免泄露敏感信息
- 严格化字符串：SQL注入和XSS攻击，避免出现不必要的输出
- 限制主题：避免暴力、攻击性和冒犯的主题
- 避免输入可执行代码
- 限制输入语言
- 避免prompt注入：避免用户输入误导或者有害的prompt可以操作系统或者影响LLM的表现
- 限定token数量：避免资源耗尽一级避免（DoS）攻击
- 毒性检测：检测并阻止有害和辱骂性语言

解决方案：

- Llama Guard: 
  - 介绍首页：https://llm-attacks.org/
  - 训练了一个模型来检测和阻止有害和辱骂性语言，避免用户输入误导或者有害的prompt可以操作系统或者影响LLM的表现
  - 论文：Universal and Transferable Adversarial Attacks on Aligned Language Models
    - https://arxiv.org/abs/2307.15043
  - Github (2.6k Stars): https://github.com/llm-attacks/llm-attacks
- Safeguarding Your RAG Pipelines: A Step-by-Step Guide to Implementing Llama Guard with LlamaIndex
  - 使用Sagemaker服务
  - https://towardsdatascience.com/safeguarding-your-rag-pipelines-a-step-by-step-guide-to-implementing-llama-guard-with-llamaindex-6f80a2e07756
