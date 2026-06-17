multica-ai/andrej-karpathy-skills

它和另一个版本 `forrestchang/andrej-karpathy-skills` 同时处于高位，分别拿到了约167k和120k的星标。

Karpathy 的「CLAUDE.md」爆了：65 行规则把 AI coding 准确率从 65% 拉到 94%，GitHub 16 万星标

拆开看：65 行里到底写了什么
打开这份 `CLAUDE.md`，内容短到有点出乎意料。四条原则，每条带几行行为约束：

原则一：Think Before Coding（写代码之前先想清楚）

核心要求：不要假设、不要隐藏困惑、有多种解释时主动问、把 tradeoff 摆到台面上。

这条规则直接对准 AI coding 最常见的坑——模型替你做了错误假设，然后不核对就一路跑下去。

"The models make wrong assumptions on your behalf and just run along with them without checking."
「模型会替你做错误假设，而且不核对就一路执行下去。」

原则二：Simplicity First（简洁优先）

核心要求：只写解决问题的最小代码、不加用户没要的功能、不为一次性代码做抽象、200 行能缩成 50 行就该重写。

对准的另一个高频问题——LLM 特别喜欢把代码和 API 复杂化。明明只要修一个点，它会顺手搭起一整套架构。

"They really like to overcomplicate code and APIs..."
「它们特别喜欢把代码和 API 复杂化。」

原则三：Surgical Changes（精准修改）

核心要求：只动必须动的地方、不顺手"改善"邻近代码、不重构没坏的部分、匹配既有风格。

这条可能是团队开发中最刚需的——对抗 diff 污染。你只让 AI 修一个 bug，结果 PR 里多出了一堆格式变更、注释重写、命名修改和无关 import。Review 成本直接翻倍。

原则四：Goal-Driven Execution（目标驱动执行）

核心要求：先定义 success criteria、把模糊指令改写成可验证的目标、用测试驱动 loop。

README 里给了几个转换示例：

"Add validation" → "Write tests for invalid inputs, then make them pass"
"Fix the bug" → "Write a test that reproduces it, then make it pass"
这条规则要解决的问题是：LLM 擅长在目标明确时循环逼近结果，但如果只说"把它弄好"，模型会把自己的完成感错当成真实完成。

CLAUDE.md 内容
▲ CLAUDE.md 的四条原则与对应的 LLM 编码问题映射

四条"常识"为什么能拿 16 万星标
这四条单独拿出来看，资深工程师可能觉得"这不就是常识吗"。

但它能在 GitHub 拿到 16 万星标、在 X 上被近 2000 人收藏，恰恰说明：大家隐约知道这些道理，但没人把它压缩成一份可以直接塞进 repo 根目录的默认工作流。

这份文件的使用门槛几乎为零：

不用换模型
不用学新框架
不用买新工具
只要把 `CLAUDE.md` 放进项目根目录
它可以和 Claude Code、Cursor、Codex 等各种 coding harness 搭配使用。比起"等更强的模型"或者"搭更复杂的 workflow"，一份 65 行的文本文件更容易让人产生"今天就能试"的冲动。

这也解释了为什么 GitHub 上会同时出现多个版本——`multica-ai` 和 `forrestchang` 两个 repo 都在热榜高位。门槛低、复制快，模板级内容天然适合裂变。

参考：https://mp.weixin.qq.com/s/6VStv6oOIz4qTcl5NUWq8Q
