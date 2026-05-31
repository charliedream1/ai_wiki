# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.sh | sh

# Windows
irm https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.ps1 | iex

# 或者直接 npm,任何系统都行
npx @colbymchenry/codegraph

2. CodeGraph 做了什么
CodeGraph 的解法非常工程:既然代码是图,那就老老实实把它建成图,本地存好,让 AI 通过结构化接口查。

整条链路是这样:

提取这一步用 tree-sitter。每种语言一份 query 文件,扫一遍源码,把节点(函数、类、方法)和边(调用、import、继承)抽出来。目前覆盖 19 种以上语言,TS / JS / Python / Go / Rust / Java / C# / PHP / Ruby / C / C++ / Swift / Kotlin / Dart / Lua / Svelte 这些主流栈都在。

存储用本地 SQLite,加 FTS5 全文索引,文件路径就在 .codegraph/codegraph.db。一个项目大概几 MB 到几十 MB,这个数据库就是知识图谱本身。不上云、不调 API、不要 key,这一点很关键。

解析这一步把符号引用解决掉:函数调用挂到定义、import 挂到源文件、子类挂到父类、框架路由挂到 handler。CodeGraph 还专门做了 14 个框架的路由识别——Django、Flask、FastAPI、Express、NestJS、Laravel、Rails、Spring、Gin、Axum、ASP.NET、Vapor、React Router、SvelteKit——GET /api/users/:id 这种路径会直接连到对应的处理函数。

自动同步用操作系统原生的文件监听(FSEvents / inotify / ReadDirectoryChangesW),改完代码 2 秒内增量更新,不需要手动 rebuild。

最关键的一步:通过 MCP(Model Context Protocol)把这个图喂给 AI。CodeGraph 是一个 MCP server,以 stdio 跟客户端通信,对外暴露这几个工具:

•codegraph_search —— 按符号名查
•codegraph_context —— 给定一个任务,返回相关代码上下文
•codegraph_callers / codegraph_callees —— 看谁调用了它、它又调用了谁
•codegraph_impact —— 改这个函数会影响哪些地方
•codegraph_node —— 看某个符号的详情
•codegraph_files —— 看索引里的文件结构
•codegraph_status —— 索引健康度

支持哪些客户端?Claude Code、Cursor、Codex CLI、opencode、Hermes Agent。装好之后 Claude Code 这边只需要在 ~/.claude.json 加上这一段:

{
  "mcpServers": {
    "codegraph": {
      "type": "stdio",
      "command": "codegraph",
      "args": ["serve", "--mcp"]
    }
  }
}
或者直接跑 npx @colbymchenry/codegraph,安装脚本会把这一段自动写进去。

3. 真实数字:VS Code、Tokio 和一个反例