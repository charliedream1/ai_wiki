# 1. 简介

![](.03_Manus开源工具_images/manus工作原理.png)

作为一款“全能 AI 智能体”，Manus 能够独立完成从简单查询到复杂项目的各种任务，无需用户持续介入。用户只需给出简单的指令，无需具备 AI 专业知识，便能获得优质的结果。

# 2. OpenManus 开源项目

Github 地址：https://github.com/mannaandpoem/OpenManus

几个的00后开发者仅用短短3个小时就打造出了 OpenManus 项目的初版。与原版 Manus 不同，后者拥有专属的云端服务器，并使用了复杂的工具以及自训练模型；而 OpenManus 则创新性地让 AI 智能体直接操控用户的个人电脑，使得普通人也能轻松体验 AI 控制电脑的奇妙之处。

从技术角度来看，OpenManus 采用了经典的 ReAct 智能体架构设计模式，它能够基于当前状态进行决策，使得上下文和记忆管理变得简单便捷。该项目依赖于四个主要工具：
- 第一、PythonExecute 用于执行 Python 代码并与电脑系统互动；
- 第二、FileSaver 负责将文件保存到本地；
- 第三、BrowserUseTool 能够操控浏览器；
- 第四、GoogleSearch 则负责执行网络搜索任务。

为了发挥项目的最大潜力，建议使用 Claude-3.5-Sonnet 或 Claude-3.7-Sonnet 大模型。

# 3. OWL 开源项目

- Workflow 复制计划 Github 地址：https://github.com/camel-ai/camel/issues/1723
- Ubuntu Toolkit复制计划Github 地址：https://github.com/camel-ai/camel/issues/1724
- Memory Toolkit复制计划Github 地址：https://github.com/camel-ai/camel/issues/1725

CAMEL AI 团队对 Manus 视频进行了详尽的分析，并对其技术路径进行了逆向工程，进而启动了一个深入的复制计划。他们将 Manus 的核心工作流程分解为六个关键阶段：

![](.03_Manus开源工具_images/owl架构图.png)

首先，他们启动了 Ubuntu 容器，为 AI 智能体构建了一个远程工作环境；

其次，执行知识召回，引用之前学习的内容；

紧接着，连接到数据源，包括数据库、网络硬盘和云存储等；

然后，将数据挂载到 Ubuntu 系统中；

之后，自动生成 todo.md 文件，规划任务和待办事项；

最后，利用 Ubuntu 的工具链和外部工具来完成整个流程的任务。

OWL 项目并不满足于简单的复制，他们还计划整合之前开发的 CRAB 技术，以实现跨平台、多设备、全场景的远程操作，旨在打造一个功能全面的开源“Manus Pro Max”。

# 4. Manus 教程开源项目

Github 地址：https://github.com/hodorwang/manus-guide

一位细心的开发者精心打造了一个 Manus 指南仓库，其中包含了极为全面的使用手册。无论你是想了解 Manus 的基础信息，寻找详尽的操作指南，探索多样化的应用场景，或是比较 Manus 与其他 AI 智能体的不同，甚至是深入理解 Manus 的 Replay 功能，这个仓库都能为你提供所需。此外，文档提供了中英文双语支持，对初学者极为友好。

![](.03_Manus开源工具_images/开源教程.png)

# 5. Computer Use 开源项目

Github 地址：https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo

别光关注 Manus，Claude 官方推出的 Computer Use 示例程序同样趣味十足。它能够构建一个完全由 AI 操控的虚拟操作系统，用户可以通过浏览器与 AI 进行互动，并且能够实时观察到 AI 的系统界面。

这个示例程序的仓库支持使用 Docker 直接运行，其中包含了一套轻量级的虚拟环境，涵盖了浏览器、操作系统和本地文件等元素。

# 6. OpenHands 开源项目

GitHub 地址：https://github.com/All-Hands-AI/OpenHands

OpenHands 核心定位：“让 AI 智能体成为全栈开发者”。

通过 AI 驱动的智能体平台，帮助开发者减少代码编写工作量，提升开发效率。

第一、技术架构

在安全与效率之间找到平衡，通过以下设计亮点实现高效开发与安全保障。

![](.03_Manus开源工具_images/openhands架构.png)

第二、系统设计亮点

Docker 沙箱运行时

基于定制化镜像（docker.all-hands.dev/openhands:0.27）构建隔离环境。



支持资源配额控制（CPU/内存限制）、操作审计日志、环境快照回滚。



三层镜像构建体系

版本标签（Versioned Tag）：基础功能镜像（如oh_v0.9.3_nikolaik）。

锁定标签（Lock Tag）：依赖固化镜像（哈希值标识）。

源码标签（Source Tag）：实时代码同步镜像（开发调试专用）。



插件化扩展

内置Jupyter内核、浏览器控制、API网关等模块。

开发者可自定义插件，灵活扩展功能。



OpenHands 致力于通过 AI 技术革新软件开发流程，让开发者专注于更重要的任务，同时确保开发环境的安全性和可扩展性。

# 7. LangManus

项目地址：

https://github.com/langmanus/langmanus

https://github.com/langmanus/langmanus-web

LangManus介绍

LangManus 是一个社区驱动的 AI 自动化框架，它基于开源社区的杰出工作成果构建而成。我们的目标是将语言模型与网络搜索、爬虫、Python 代码执行等专用工具相结合，

核心特点

LangManus实现了一个分层多代理系统，其中一个主管协调专业代理来完成复杂任务：

1. 核心能力

- 🤖 LLM集成：支持Qwen等开源模型

- 与OpenAI兼容的API接口

- 多层次LLM系统，适应不同复杂度的任务



2. 工具与集成

- 🔍 搜索和检索：通过Tavily API进行网络搜索

- 使用Jina进行神经搜索

- 高级内容提取功能



3. 开发功能

- 🐍 Python集成：内置Python REPL

- 代码执行环境

- 使用uv进行包管理



4. 工作流管理

- 📊 可视化和控制：工作流图形可视化

- 多代理协调

- 任务委派和监控

![](.03_Manus开源工具_images/架构图.png)

LangManus的系统由以下代理协同工作组成：

1. 协调者(Coordinator) - 处理初始交互并路由任务的入口点

2. 规划者(Planner) - 分析任务并创建执行策略

3. 主管(Supervisor) - 监督和管理其他代理的执行

4. 研究员(Researcher) - 收集和分析信息

5. 编码员(Coder) - 处理代码生成和修改

6. 浏览器(Browser) - 执行网页浏览和信息检索

7. 报告员(Reporter) - 生成工作流结果的报告和摘要

# 8. agenticSeek

- Github (7.2k stars): https://github.com/Fosowl/agenticSeek

# 9. AgenticSeek

- Github (16.6k stars): https://github.com/Fosowl/agenticSeek

为什么选择 AgenticSeek？

🔒 完全本地和私有 - 一切都在您的机器上运行 - 没有云，没有数据共享。您的文件、对话和搜索将保持私密。

🌐 智能网页浏览 - AgenticSeek 可以自行浏览互联网 - 搜索、阅读、提取信息、填写网页表格 - 所有这些都是免提的。

💻 Autonomous Coding Assistant - 需要代码？它可以用 Python、C、Go、Java 等语言编写、调试和运行程序 — 所有这些都无需监督。

🧠 智能代理选择 - 您询问，它会自动找出最适合该工作的代理。就像有一个随时准备提供帮助的专家团队。

📋 计划并执行复杂的任务 - 从旅行计划到复杂的项目 - 它可以将大任务分成步骤，并使用多个AI代理完成工作。

🎙️ 支持语音 - 干净、快速、未来主义的语音和语音到文本，让您可以像科幻电影中的个人 AI 一样与它交谈

# 参考

[1] 5大开源 Manus 复刻项目全景解析, https://mp.weixin.qq.com/s/2XCqGvtq5K9qR8927tdveA