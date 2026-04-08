- Github (3.7k stars): https://github.com/HKUDS/OpenHarness

Harness是什么
“Harness”原本是英语里的“马具”（给马套上的挽具），用来控制马的方向和力量。现在借用到AI领域，意思是：给AI Agent套上一套“缰绳”，让它不再是“一匹野马”，而能长期、稳定、安全地完成复杂任务。

Harness = 围绕LLM（大语言模型）或Agent的执行与治理层，本质上是一个运行时系统 + 基础设施。 它不是某个具体模型、Prompt、或单一框架，而是把“会思考的模型”变成“能可靠落地执行”的完整环境。

简单说： Agent = 模型 + Harness Harness负责模型之外的一切“工程化”工作，让Agent能跨多轮、跨天、跨上下文窗口持续工作，而不会“失忆”或失控。

🔥 一行命令，解锁所有 Agent 能力
oh  # 就这么简单
OpenHarness 是一个开源的 Agent Harness（智能体套具）实现，让 LLM 拥有手、眼、记忆和安全边界。支持 OpenClaw、nanobot、Cursor 等多种 CLI agent 集成。


🎯 核心能力一览
🔄 Agent 循环引擎
流式工具调用循环
指数退避的 API 重试
并行工具执行
Token 计数与成本追踪
🔧 43+ 工具包
文件、Shell、搜索、Web、MCP 等全方位工具支持。

🧠 上下文与记忆
CLAUDE.md 自动发现与注入
上下文自动压缩
MEMORY.md 持久化记忆
会话恢复与历史记录
🛡️ 治理与安全
多级权限模式
路径级和命令规则
前后工具调用钩子
交互式审批对话框
🤝 多 Agent 协调
子 Agent 生成与委托
团队注册表与任务管理
后台任务生命周期管理