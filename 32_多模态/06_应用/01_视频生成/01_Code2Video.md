AIGC开源推荐-视频生成/制作-Code2VideoCode2Video 是一个基于代码的教育视频生成框架,通过可执行的 Manim Python 代码来生成高质量的教学视频 https://github.com/showlab/Code2Video

核心理念

该项目采用代码中心范式(Code-Centric Paradigm),将可执行代码作为统一媒介来组织教育视频的时间序列和空间布局  。与基于像素的文本到视频模型不同,Code2Video 通过生成可调试的 Manim 代码来确保视频的清晰度、连贯性和可重现性 

三智能体架构

项目采用模块化的三智能体设计 

1. Planner Agent (规划器)

负责将知识点扩展为详细的分镜脚本(storyboard) README.md:78 。它首先生成教学大纲(TeachingOutline),包含主题、目标受众和章节结构 agent.py:182-186 ,然后将大纲扩展为包含讲解词(lecture_lines)和动画描述(animations)的详细分镜

2. Coder Agent (编码器)

将分镜脚本转换为可执行的 Manim Python 代码 README.md:78 。它通过 LLM API 为每个章节生成代码,支持并行处理(使用 6 个工作线程) agent.py:518-519 ,并集成外部视觉资源(通过 SmartSVGDownloader 从 IconFinder 和 Iconify API 下载图标) 。

3. Critic Agent (评论器)

使用多模态 LLM 分析渲染后的视频,提供布局优化建议 README.md:78 。它提取代码中的网格位置信息 agent.py:405-407 ,通过 Gemini 视频 API 分析视频质量 agent.py:438 ,并使用 GridCodeModifier 或 LLM 重新生成来应用改进建议 

工作流程

完整的视频生成流程包括:
生成大纲 → 2. 生成分镜 → 3. 资源增强(可选) → 4. 并行代码生成 → 5. 调试修复 → 6. 视频渲染 → 7. 反馈优化(可选)
配置参数通过 RunConfig 数据类管理,包括 API 选择、token 限制、重试次数等


# 参考

[1] AIGC开源推荐-视频生成/制作-Code2Video, https://mp.weixin.qq.com/s/JRERDLu-dB1OaOFHN5vEZA