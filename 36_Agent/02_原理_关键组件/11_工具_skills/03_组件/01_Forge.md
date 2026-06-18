项目地址：github.com/antoinezambelli/forge

Forge是什么？

Forge是一个Python框架，核心就一句话：确保AI Agent正确地调用工具，而不是瞎猜。

它不替代你的LLM，不替代你的Agent框架。它就坐在中间，像一个安检员——每个工具调用进来，它检查一遍，有问题的拦住重试，没问题的放行。

它的作者Antoine Zambelli做了一个测试：同样的Agent任务，没有Forge的8B小模型得分只有个位数，加上Forge直接干到84%。连Sonnet 4.6这样的顶级模型，也从85%被拉到了98%。

四个关键能力

我一共跑了5个测试，覆盖了Forge的四个核心能力。直接看结果：

TEST 1: AI说了句话，但没调用工具   → 返回retry，告诉AI"你需要调用工具"   → 而不是直接放行，让下游报错                                                 TEST 2: AI正确调用search工具   → 放行，记录步骤   → ✅ 正常工作            TEST 3: AI跳过lookup，直接调用answer   → 被拦住！返回step_blocked   → "必须先完成lookup才能answer"   → 强制工具调用顺序                            TEST 4: AI调用了一个不存在的工具delete_all   → 返回tool_error，拒绝执行   → 防止AI胡来                                                             TEST 5: 完整流程search→lookup→answer   → ✅ 全部通过，workflow完成

这套机制叫什么？Guardrail（护栏）。不是你写完代码后的测试，而是在AI做出工具调用请求的那一瞬间，就检查它有没有出错。
