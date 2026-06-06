# 代码知识图谱爆火：Understand Anything 与 CodeGraph 怎么选？

# 两个爆火代码理解项目：Understand Anything 和 CodeGraph，到底该怎么上手？

最近代码知识图谱这条线突然热起来了。

一个新项目，动不动几十万行代码；一个老项目，README 写得像考古现场；再加上现在大家都在用 Claude Code、Codex、Cursor、Gemini CLI 这类 AI 编程工具，问题就变得很现实：

**AI 到底该怎么理解一个代码仓库？**

是像人一样打开文件、grep、读源码、再总结？
还是提前把整个项目索引成一张“代码地图”，让 AI 查询这张地图？

这篇文章拆两个近期很火的项目：

- **Understand Anything**：https://github\.com/Lum1104/Understand\-Anything\(\[1\]\)

- **CodeGraph**：https://github\.com/colbymchenry/codegraph\(\[2\]\)

我本地把两个仓库都 clone 下来看了一遍源码、README 和目录结构。截止我分析时：

- Understand Anything：约 **36k stars**，MIT，TypeScript，最新提交在 2026\-05\-26

- CodeGraph：约 **28k stars**，MIT，TypeScript，npm 包版本 **0\.9\.6**，最新提交在 2026\-05\-27

这两个项目都叫“代码知识图谱”，但它们的性格完全不同。

一句话先放结论：

> ***Understand Anything 更像“代码库讲解员”，适合上手、学习、团队 onboarding；CodeGraph 更像“本地代码索引引擎”，适合让 AI 编程工具少读文件、少烧 token、快速定位调用关系。***
> 
> 

---

## 一、为什么现在需要“代码知识图谱”？

以前我们理解项目，大概靠三件事：

1. README

2. 文件目录

3. 全局搜索

但到了 AI 编程时代，这三件事不够了。

因为 AI 的上下文不是无限的。它如果不知道该读哪些文件，就会像一个刚入职的新人一样：

- 先 `ls`

- 再 `find`

- 再 `grep`

- 再打开一堆文件

- 然后还不一定读到重点

如果仓库很大，这个过程会非常贵：贵在 token，贵在工具调用，贵在时间，也贵在不稳定。

所以“代码知识图谱”的核心价值不是画一张很好看的图，而是提前回答这些问题：

- 这个项目有哪些模块？

- 哪些文件是入口？

- 一个函数被谁调用？

- 改这个类会影响哪些地方？

- 某条业务链路从 API 到数据库怎么走？

- 新人应该按什么顺序理解这个系统？

Understand Anything 和 CodeGraph 都在解决这些问题，只是切入方式不同。

---

## 二、先看 Understand Anything：它想把代码变成“可学习的知识库”

Understand Anything 的定位很直白：

> *Turn any codebase, knowledge base, or docs into an interactive knowledge graph\.*
> 
> 

它不只是做代码索引，而是想把代码库变成一份可以探索、搜索、提问、讲解的知识系统。

### 怎么上手？

如果你用 Claude Code，官方推荐方式是：

```Plain Text
/plugin marketplace add Lum1104/Understand-Anything
/plugin install understand-anything
```

然后在项目里执行：

```Plain Text
/understand
```

它会扫描项目，生成：

```Plain Text
.understand-anything/knowledge-graph.json
```

再打开 Dashboard：

```Plain Text
/understand-dashboard
```

你会得到一个交互式图谱，可以点文件、函数、类，看它们之间的依赖关系、摘要、标签、架构层级和学习路径。

如果你想让输出直接是中文，可以这样：

```Plain Text
/understand --language zh
```

这点很实用。很多团队内部做 onboarding，中文解释比英文摘要更容易落地。

除了 Claude Code，它也支持 Codex、OpenCode、OpenClaw、Gemini CLI、Cursor、VS Code Copilot、Hermes、Trae 等平台。通用安装方式是：

```Plain Text
curl -fsSL https://raw.githubusercontent.com/Lum1104/Understand-Anything/main/install.sh | bash
```

也可以指定平台：

```Plain Text
curl -fsSL https://raw.githubusercontent.com/Lum1104/Understand-Anything/main/install.sh | bash -s codex
```

### 入门时应该先跑哪几个命令？

我建议按这个顺序来：

```Plain Text
/understand --language zh
```

先生成中文图谱。

```Plain Text
/understand-dashboard
```

先看全局结构，不要急着读源码。

```Plain Text
/understand-chat 这个项目的核心模块有哪些？
```

让它从图谱里回答项目整体结构。

```Plain Text
/understand-onboard
```

生成新人入门路线。

```Plain Text
/understand-explain src/xxx.ts
```

再针对关键文件深挖。

```Plain Text
/understand-diff
```

改代码前后看影响范围。

如果项目偏业务系统，还可以跑：

```Plain Text
/understand-domain
```

它会尝试抽取业务域、业务流程和步骤。这是 Understand Anything 和普通静态分析工具拉开差距的地方：它不只关心函数调用，还关心“这段代码在业务上代表什么”。

### 它底层是怎么做的？

Understand Anything 走的是 **Tree\-sitter \+ LLM hybrid** 路线。

也就是说：

- **Tree\-sitter** 负责确定性的结构分析：文件、函数、类、import、call site、继承关系等。

- **LLM** 负责语义理解：文件摘要、标签、架构层、业务域、学习路径、语言概念解释等。

它的核心图谱结构比较“知识库化”。源码里可以看到，它支持很多节点类型：

- `file`

- `function`

- `class`

- `module`

- `config`

- `document`

- `service`

- `table`

- `endpoint`

- `pipeline`

- `schema`

- `domain`

- `flow`

- `step`

- `article`

- `entity`

- `claim`

边类型也很多，除了 `imports`、`calls`、`contains`，还有：

- `documents`

- `routes`

- `defines_schema`

- `contains_flow`

- `flow_step`

- `cites`

- `contradicts`

- `builds_on`

这说明它的目标不只是“代码关系图”，而是把代码、文档、业务知识、知识库都统一成一张图。

### 它适合谁？

我觉得 Understand Anything 最适合这几类场景：

**第一，新人接手大项目。**
你不想从 `src/index.ts` 一路硬啃，而是希望先知道系统分层、核心模块、学习顺序。

**第二，团队做代码库文档化。**
它生成的 `.understand-anything/knowledge-graph.json` 可以提交到仓库里。团队成员不用每个人都重新分析一遍。

**第三，技术负责人做架构梳理。**
它有 layer visualization、guided tours、domain view，对“解释系统”很友好。

**第四，业务复杂的项目。**
如果你的系统不是单纯工具库，而是有订单、支付、权限、任务流、审核流这类业务概念，Understand Anything 的 domain 分析更有价值。

---

## 三、再看 CodeGraph：它更像 AI 编程工具的“本地大脑缓存”

CodeGraph 的气质不一样。

它不是先强调漂亮 Dashboard，也不是先强调“讲解”，而是强调：

> *让 AI 少读文件、少调用工具、少花钱。*
> 
> 

README 里给出的 benchmark 很直接：平均 **35% cheaper、57% fewer tokens、46% faster、71% fewer tool calls**。

当然，benchmark 要结合测试方法看，不能当成绝对真理。但方向很清楚：CodeGraph 是为 AI agent 的代码探索成本优化而生的。

### 怎么上手？

最简单方式：

```Plain Text
curl -fsSL https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.sh | sh
```

如果已经有 Node，也可以：

```Plain Text
npx @colbymchenry/codegraph
```

或者全局安装：

```Plain Text
npm i -g @colbymchenry/codegraph
```

进入项目后初始化：

```Plain Text
codegraph init -i
```

它会生成：

```Plain Text
.codegraph/codegraph.db
```

注意，CodeGraph 的核心不是 JSON 文件，而是一个本地 SQLite 数据库。

### 入门时应该怎么用？

如果只是命令行体验，可以先试：

```Plain Text
codegraph status
```

看索引状态。

```Plain Text
codegraph query auth
```

搜索符号。

```Plain Text
codegraph files
```

看索引到的文件结构。

```Plain Text
codegraph context "用户登录流程是怎么走的？"
```

让它围绕一个任务构建上下文。

```Plain Text
codegraph callers login
codegraph callees login
```

看调用方和被调用方。

```Plain Text
codegraph impact login
```

看修改某个符号可能影响哪些地方。

如果接到 MCP 里，它会暴露这些工具：

- `codegraph_search`

- `codegraph_context`

- `codegraph_trace`

- `codegraph_callers`

- `codegraph_callees`

- `codegraph_impact`

- `codegraph_node`

- `codegraph_explore`

- `codegraph_files`

- `codegraph_status`

这才是它真正的杀手锏：让 Claude Code、Cursor、Codex 这类工具不用一上来就 grep/read，而是先问本地索引。

### 它底层是怎么做的？

CodeGraph 的设计更“工程化”。

核心流程是：

1. **Extraction**：用 tree\-sitter 解析源码，抽取函数、类、方法、import、call、extends、implements 等。

2. **Storage**：写入本地 SQLite，节点、边、文件、未解析引用都有独立表。

3. **Resolution**：统一解析引用关系，比如调用指向定义、import 指向文件、继承关系、框架路由关系等。

4. **Auto\-Sync**：MCP server 启动后监听文件变化，默认 debounce 2 秒自动同步。

源码里的 SQLite schema 很清楚：

- `nodes`：代码符号

- `edges`：符号关系

- `files`：文件索引状态

- `unresolved_refs`：等待解析的引用

- `nodes_fts`：FTS5 全文搜索

这就是一个典型的本地代码索引数据库。

它支持的语言也很丰富：TypeScript、JavaScript、Python、Go、Rust、Java、C\#、PHP、Ruby、C/C\+\+、Objective\-C、Swift、Kotlin、Dart、Lua、Svelte、Liquid、Pascal/Delphi 等。

尤其值得注意的是，它对一些框架和跨语言场景做了很多细节：

- Django / Flask / FastAPI

- Express / NestJS

- Laravel / Rails / Spring

- Gin / chi / gorilla / mux

- Axum / actix / Rocket

- React Router / SvelteKit

- Swift ↔ Objective\-C

- React Native bridge

- Expo Modules

- Fabric / Paper view managers

这说明 CodeGraph 的重点不是“把图画出来”，而是把真实项目里最麻烦的调用链补上。

### 它适合谁？

CodeGraph 适合这些场景：

**第一，你经常让 AI 改大项目。**
AI 每次都要重新找文件，成本很高。CodeGraph 可以把探索过程前置。

**第二，你更关心调用链和影响面。**
比如“这个 controller 最后调到哪个 repository？”、“改这个函数会影响哪些测试？”、“这个 symbol 有哪些 callers？”

**第三，你对数据本地化敏感。**
CodeGraph 强调 100% local，不需要 API key，不把代码发出去。

**第四，你想把代码理解能力接进 MCP。**
它天然就是给 agent 工具调用准备的，不只是给人看的。

---

## 四、如果我第一次接触，应该先玩哪个？

我的建议是：

**如果你是为了“读懂一个项目”，先用 Understand Anything。**

因为它的学习路径更友好。你跑完 `/understand`，再打开 dashboard，可以很快建立项目的空间感：有哪些模块、哪些层、哪些关键文件、应该从哪里读起。

它像一个有耐心的老员工，带你逛项目。

**如果你是为了“让 AI 更高效地改代码”，先用 CodeGraph。**

因为它的核心价值在 MCP 工具和本地索引。你不一定需要看图，你要的是 AI 直接回答：相关文件在哪里，调用链是什么，影响范围多大。

它像一个本地搜索引擎 \+ 调用关系数据库，给 AI 当外挂。

如果你两个都想用，我会这样组合：

1. 用 Understand Anything 做第一次全局理解。

2. 用 CodeGraph 做日常开发时的精准定位。

3. 团队 onboarding 用 Understand Anything 的图谱和导览。

4. AI coding session 用 CodeGraph 的 MCP 工具减少探索成本。

这两个项目不是完全替代关系，更像互补关系。

---

## 五、最后聊聊优劣点：两个项目到底怎么选？

### Understand Anything 的优点

5. **面向“理解”，不是只面向“检索”。**
它会生成摘要、标签、架构层、guided tour、业务域分析。对新人和团队知识沉淀很友好。

6. **Dashboard 体验更完整。**
可视化图谱、搜索、节点详情、导览，这些更适合人类浏览。

7. **图谱可以提交进仓库。**
`.understand-anything/knowledge-graph.json` 可以作为 docs\-as\-code 的一部分，团队共享成本低。

8. **支持知识库和业务域。**
它不只分析代码，还能分析 Karpathy\-pattern LLM wiki，把文章、实体、claim、source 等也放进图里。

### Understand Anything 的短板

9. **更依赖 LLM，成本和稳定性要关注。**
语义摘要、业务域、导览这类能力很强，但也意味着结果会受模型质量影响。

10. **首次分析可能更重。**
多 agent pipeline、批处理、语义生成，对大项目来说不是“秒开即用”。

11. **更适合学习和展示，未必是最高效的 agent 查询后端。**
它当然能问答，但从工程结构看，它更像知识图谱产物和 dashboard，而不是极致优化的本地查询引擎。

---

### CodeGraph 的优点

12. **本地优先，工程味很重。**
SQLite、FTS5、tree\-sitter、文件 watcher、增量 sync，都是实打实的开发工具设计。

13. **对 AI agent 很友好。**
MCP tools 设计得很细：search、context、trace、callers、callees、impact、explore。它知道 AI 最容易浪费在哪：重复探索文件。

14. **调用链和影响分析更强。**
尤其对“我要改代码，先看影响范围”这种场景，CodeGraph 很对味。

15. **100% local。**
不需要 API key，不依赖云端服务，对私有代码库更安心。

### CodeGraph 的短板

16. **对“新人学习”的表达不如 Understand Anything 友好。**
它更像数据库和工具集，不像一个会讲故事的项目讲解员。

17. **图谱语义层相对克制。**
它强在符号、关系、调用链、索引。业务域、知识库、导览式学习不是它的主战场。

18. **小项目收益有限。**
如果项目就几十个文件，AI 自己 grep/read 也不贵，CodeGraph 的优势会变小。

---

## 六、我的最终判断

这两个项目看起来都在做“代码知识图谱”，但背后的产品哲学不一样。

**Understand Anything 关心的是：人如何理解项目。**
所以它做 dashboard、guided tours、plain\-English summaries、domain view、knowledge base analysis。

**CodeGraph 关心的是：AI 如何更便宜、更快、更准确地探索项目。**
所以它做 SQLite、本地索引、MCP tools、call graph、impact analysis、auto\-sync。

如果你是个人开发者，我建议先装 CodeGraph，因为它马上能帮你的 AI coding session 降低探索成本。

如果你是团队负责人，尤其经常有人接手老项目，我建议认真试 Understand Anything，因为它更适合沉淀“项目是怎么运转的”。

如果你是重度 AI 编程用户，最理想的方案其实是：

> ***用 Understand Anything 建立认知地图，用 CodeGraph 提供日常检索引擎。***
> 
> 

一个负责“看懂全局”，一个负责“查准细节”。

这可能就是 AI 编程工具接下来真正需要的基础设施：不是更会聊天，而是更会理解你的代码世界。

---

## 参考项目

- Understand Anything：https://github\.com/Lum1104/Understand\-Anything\(\[3\]\)

- CodeGraph：https://github\.com/colbymchenry/codegraph\(\[4\]\)

### 引用链接

\[1\]*https://github\.com/Lum1104/Understand\-Anything*

\[2\]*https://github\.com/colbymchenry/codegraph*

\[3\]*https://github\.com/Lum1104/Understand\-Anything*

\[4\]*https://github\.com/colbymchenry/codegraph*

