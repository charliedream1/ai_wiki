多平台新闻聚合skill，一个指令扫全网

GitHub 上 last30days-skill 的项目今天冲到了 Trending 第一，28,445 颗星，2,400 多 forks，直接杀疯了。

这是啥？就是一个 AI agent 技能，你给一个话题，它自动在 Reddit、X、YouTube、TikTok、HN、Polymarket、GitHub 等十几个平台检索最近 30 天的讨论，然后合成一份有据可查的研究报告。

之前想做竞品调研或者热点追踪，要在各个平台之间切来切去，截图、复制、粘贴，累死。这玩意一行指令全搞定。

几个让我觉得牛逼的地方：

覆盖 10+ 平台
Reddit、X（Twitter）、YouTube、TikTok、Instagram、Hacker News、Polymarket、GitHub、Web Search，还有 Bluesky。基本上你能想到的社交/媒体平台都在了。

双模式检索
--quick 模式快速出结果，适合日常扫一眼；--deep 模式深度挖掘，适合写报告做研究。还有个 --competitors 自动对比竞品讨论热度，写产品分析文章绝了。

多种输出格式
compact 摘要、json 数据、完整 markdown 报告、甚至直接出 HTML。想怎么用就怎么用。

谁适合用？
内容创作者：写文章前扫一下社区真实反馈，找到最佳切入角度，不再拍脑袋选题

产品/竞品分析：想知道"最近大家怎么评价XX"，一行指令出报告
开发者：为开源项目写 README 时，扫一下近 30 天社区对同类工具的评价
安装也简单，有 OpenClaw 的话直接 openclaw skills install last30days-skill，或者 git clone 下来就行。Python 3.12+ 环境，部分源免 API Key 可用。

这项目 1 月上线的，半年冲到 28K stars，说明这个需求是真的硬。

参考：https://mp.weixin.qq.com/s/3O5t1l7fkOVzWUEbzebooA
