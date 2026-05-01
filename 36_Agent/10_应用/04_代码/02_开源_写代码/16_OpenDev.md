论文基本信息：Bui, N. D. (2026). Building AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned. arXiv preprint arXiv:2603.05344.
论文链接：https://arxiv.org/pdf/2603.05344
代码链接：https://github.com/opendev-to/opendev

图2展示了OpenDev的四层架构：入口与UI层、智能体层、工具与上下文层、持久化(Persistence)层。用户输入按顺序流经这一管道，从入口点经过智能体推理和工具执行，最终结果被持久化并呈现。
入口与UI层：CLI入口点启动四个共享管理器并注入下游组件。支持TUI和Web UI两种前端，通过共享UICallback契约实现智能体层的UI无关性。
智能体层：OpenDev使用五个不同角色的LLM，分别服务不同工作负载。系统分为普通模式（完整读写）和计划模式（只读）。推理通过扩展ReAct循环执行，包含四个阶段：自动上下文压缩、（可选）思考、（可选）自我批评、推理-行动-执行-观察。
工具与上下文层：工具执行层基于ToolRegistry分派调用，支持并行执行和按需MCP工具发现；技能(Skills)系统从三层层次结构延迟加载领域模板。上下文工程层通过系统提醒、提示组合器、记忆系统和紧缩机制四个子系统管理上下文窗口。
持久化层：通过配置管理器、会话管理器、模型提供商缓存和操作日志四个存储实现跨会话的状态持久化与回滚。
智能体的安全架构采用五层纵深防御（提示级护栏、模式级工具限制、运行时审批、工具级验证、生命周期钩子），各层独立运作，单层失败不影响整体安全性。