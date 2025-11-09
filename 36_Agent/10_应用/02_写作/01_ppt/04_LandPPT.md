AIGC开源项目PPT生成-LandPPTLandPPT 是一个基于大语言模型（LLM）的智能演示文稿生成平台，能够自动将文档内容转换为专业的PPT演示文稿。平台集成了多种AI模型、智能图像处理、深度研究功能和丰富的模板系统，让用户能够轻松创建高质量的演示文稿

PPT生成分为三个阶段：
1、项目创建和需求确认，首先通过项目工作流管理系统创建项目并确认需求；
2、大纲生成阶段，系统使用AI生成结构化的PPT大纲。
两种模式，一个是标准大纲生成，使用AI直接生成大纲结构；
研究增强模式，当启用网络模式时，系统会先进行深度研究，然后基于研究结果生成大纲。
大纲生成使用专门的提示词模板，确保输出标准化的JSON格式，在：https://github.com/sligter/LandPPT/blob/master/src/landppt/services/prompts/outline_prompts.py

# 参考

[1] AIGC开源项目PPT生成-LandPPTLandPPT , https://mp.weixin.qq.com/s/hHkJNccm_uAJ1nYEYg3GTw