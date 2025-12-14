AIGC开源推荐-PPT演示视频生成https://github.com/eric-ai-lab/EvoPresent/tree/main
https://evopresent.github.io/  pdf到转PPT了 做成PPT演示视频（PPT的演示视频 可以clone自己的声音)之前也也介绍过课件视频生成方案#PresentationGenerationPipeline #智能演讲稿生成 
AIGC开源推荐-视频生成/制作-Code2Video

EvoPresent 是什么？

一句话：这是一个自动把论文变成“像人类宣讲”的高质量学术汇报（含逐页幻灯片 + 讲稿 + 配图 + 讲解视频）的多智能体流水线系统。

它不只是“把 PDF 变成 PPT 文本”。它主打三件事：

内容讲故事：自动梳理论文卖点、主线逻辑、逐页脚本，而不是死抄摘要。
GitHub

视觉设计：自动铺版、配色、留白、字号、插图（甚至用图像生成补充示意），并强制执行统一视觉风格，比如 tech_dark 这种深色科技感模板。

自我迭代美化：它内置了一个“审美裁判”模型 PresAesth。这个模型会像设计导师一样，对每一页幻灯片打分、指出丑点（如版式拥挤、层级混乱、字体不协调），并要求重新排版，直到达到给定阈值（比如评分 ≥ 8.7）。

最后一步，它还能把整套幻灯片“讲出来”：自动生成讲解语音（可用你自己的音色或内置音色）、驱动一个虚拟讲者的口型 / 面部表情、合成解说视频，形成一条完整的“学术宣传片”

# 参考

[1] AIGC开源推荐-PPT演示视频生成, https://mp.weixin.qq.com/s/VPJ7N_uMYUPR0f4JRokFeg