- Github (6k stars): https://github.com/lsdefine/GenericAgent
- https://arxiv.org/abs/2604.17091
- GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)

GenericAgent 是一个极简、可自我进化的自主 Agent 框架。核心仅 ~3K 行代码，通过 9 个原子工具 + ~100 行 Agent Loop，赋予任意 LLM 对本地计算机的系统级控制能力，覆盖浏览器、终端、文件系统、键鼠输入、屏幕视觉及移动设备。

它的设计哲学是：不预设技能，靠进化获得能力。

每解决一个新任务，GenericAgent 就将执行路径自动固化为 Skill，供后续直接调用。使用时间越长，沉淀的技能越多，形成一棵完全属于你、从 3K 行种子代码生长出来的专属技能树。

🤖 自举实证 — 本仓库的一切，从安装 Git、git init 到每一条 commit message，均由 GenericAgent 自主完成。作者全程未打开过一次终端。

 核心特性
- 自我进化: 每次任务自动沉淀 Skill，能力随使用持续增长，形成专属技能树
- 极简架构: ~3K 行核心代码，Agent Loop 约百行，无复杂依赖，部署零负担
- 强执行力: 注入真实浏览器（保留登录态），9 个原子工具直接接管系统
- 高兼容性: 支持 Claude / Gemini / Kimi / MiniMax 等主流模型，跨平台运行
- 极致省 Token: 上下文窗口不到 30K，是其他 Agent（200K–1M）的零头。分层记忆让关键信息始终在场——噪声更少，幻觉更低，成功率反而更高，而成本低一个数量级。