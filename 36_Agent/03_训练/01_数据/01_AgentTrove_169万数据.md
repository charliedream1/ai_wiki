169万条轨迹、19.6GB！Open-Thoughts 开源 AgentTrove：迄今最大 Agent 训练轨迹数据集，覆盖 219 个源
数据集：open-thoughts/AgentTrove

简介：迄今最大的开源 agentic interaction traces 集合，约 170 万条完整 Agent 轨迹，来自 219 个源数据集，覆盖代码修复、Shell 脚本、数学推理、竞赛编程与通用计算机使用任务，规模约为此前最大开源同类数据集 Nemotron Terminal Corpus 的 4 倍。

发布时间：

项目博客：2025-12-05

Hugging Face 仓库最近更新：2026-05-07



官方介绍博客：

https://www.open-thoughts.ai/blog/agent

开源地址：

https://huggingface.co/datasets/open-thoughts/AgentTrove

发布来源：

OpenThoughts-Agent 团队（Open Thoughts 协作组织：Stanford、UC Berkeley、UT Austin、NYU、UW、UCLA、UNC、TUM、LAION，及 Bespoke Labs / Laude Institute / Daytona / Oumi 等支持方）

数据量级：

1,696,847 条轨迹 / 行；约 19.6 GB（parquet）；21 列；单一 default/train 切分；—— 汇聚自 219 个源数据集，跨多种教师模型（GLM-4.6 / 4.7、GPT-5.1 Nano、GPT-5 / 5-mini、Kimi K2.0 Thinking、MiniMax M2.0、Qwen3、GPT-OSS-120B、Gemini-2.5-Flash 等）。


模态类型：

文本（多轮对话 + 工具调用 + 环境响应）

语言覆盖：英文

适用场景：

通用 Agent / 编码 Agent / 终端 Agent 的 SFT 与 RL 训练；

Terminal-Bench 等 agentic benchmark 的数据基座；

轨迹数据分析与教师/课程消融研究；

构建可在 Harbor + SkyRL 训练栈上使用的多教师、多任务 agent 数据。

详细介绍：

AgentTrove 是 OpenThoughts-Agent 项目的核心数据资产，沿着 OpenThinker-Agent-v1（Terminal-Bench 2.0 同尺寸最强模型）背后的训练管线对外开放完整的轨迹数据。

所有轨迹采用与 Nemotron Terminal Corpus 一致的 terminus-2 harness 格式（ShareGPT 风格的多轮对话），每行是一条完整的 Agent 轨迹，包含工具调用、环境反馈与最终推理；并保留 original_source（如 swesmith / codeforces / nl2bash / r2egym / freelancer 等）、original_teacher（GLM、GPT、Kimi、MiniMax、Qwen3 等）、reward、task_id 等关键字段，方便按教师、按任务源、按通过率筛选与采样。

数据由 Harbor 框架在 Docker 沙盒中产出，覆盖 NL2Bash、SWESmith、SWEGym、InferredBugs、Codeforces、Defects4J、StackExchange、Freelancer、Taskmaster、Mind2Web、Qasper、Glaive Code Assistant、MagiCoder Evol Instruct、AlfWorld、Nemotron Prism 等 219 个源，是当前公开可得的最丰富的端到端 Agent 训练语料；适合构建终端类、代码类、Computer-Use 类大模型 Agent 的 SFT、RL 与课程学习数据基座。


参考：https://mp.weixin.qq.com/s/G0_mZGY4UG74mnX1fNbCqw