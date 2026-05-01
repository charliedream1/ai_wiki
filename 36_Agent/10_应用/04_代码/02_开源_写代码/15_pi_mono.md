- Github (34k stars): https://github.com/badlogic/pi-mono 

Pi — badlogic/pi-mono | 31.6k stars | MIT | TypeScript
一个只给模型四个工具（read / edit / write / bash）的终端编程 Agent。不做 MCP、不做 sub-agent、不做权限弹窗——所有功能靠扩展系统实现。8 个月拿到 3 万星，而且是 OpenClaw 的底层引擎。

四个工具和一份"不做什么"清单
Pi 给 LLM 的默认工具集：read、edit、write、bash。没有 grep、没有 find、没有 glob——这些在需要时由扩展提供。Claude Code 内置 10+ 工具，Cursor 更多，Pi 的判断是：多出来的工具是噪声。
它明确不做的事同样定义了这个项目：
不做 MCP。Pi 的作者写了一篇博客解释为什么，核心观点是：与其造一个复杂的协议层让 LLM 调外部服务，不如直接用 CLI 工具加 README 文档（Pi 称之为 "Skills"），或者写一个扩展。不做 sub-agent。想并行？用 tmux 起 Pi 实例，或者用扩展自己实现。不做权限弹窗。该跑沙箱跑沙箱，别让 Agent 停下来等人点"允许"。不做 plan mode。把计划写到文件里就行，或者写个扩展。不做内置 todo。模型会被 todo 列表搞混。用 TODO.md。
这份清单定义了 Pi 的边界：核心只管 Agent 循环和工具执行，其他一切交给扩展。