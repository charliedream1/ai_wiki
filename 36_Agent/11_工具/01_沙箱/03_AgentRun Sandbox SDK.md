函数计算 AgentRun 的核心亮点之一，是其内置的多类型 Sandbox 运行环境，基于阿里云 FC 安全隔离架构构建，确保每一次执行都安全可控：

Code Interpreter Sandbox（代码解释器沙箱）
提供隔离的 Python/JavaScript 执行环境，支持文件系统读写、命令执行、数值计算与数据分析。适用于需要动态生成/执行代码的场景，如数据可视化、公式求解、自动化脚本等。
Browser Sandbox（浏览器沙箱）
内置无头浏览器、VNC 可视化客户端及操作录制功能，支持模拟真实用户行为，实现网页抓取、表单填写、信息提取等操作，为智能体赋予“上网”能力。
All-in-One Sandbox（二合一沙箱）
融合代码执行与浏览器能力于一体，一站式支持复杂任务流——例如：先爬取网页数据，再用 Python 分析并生成图表，最后返回结构化结果。真正实现“端到端智能体工作流”。
为降低接入门槛，函数计算 AgentRun 特别开源推出基于 Python 语言的 Sandbox SDK，开发者仅需几行配置即可将任意智能体接入沙箱服务。无需修改原有框架逻辑，即可享受 Serverless 架构下的安全、弹性与高性能。


LangChain × Codelnterpreter：

为智能体注入“代码大脑”

# 参考

[1] AgentRun Sandbox SDK 正式开源！集成 LangChain 等主流框架，一键开启智能体沙箱新体验, https://mp.weixin.qq.com/s/DVeUIeCxdUJW5NuWGP0bNw