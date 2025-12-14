
AICG开源推荐-PPT生成-presenton  https://github.com/presenton/presenton

Presenton 是一个开源 AI 演示文稿生成工具及 API，定位为 Gamma、Beautiful AI、Decktopus 等商业工具的替代方案，核心优势是本地运行、数据隐私可控，支持多模型集成与高度自定义，适合个人、团队及企业级演示文稿自动化生成场景。

一、核心定位与核心价值

1. 核心定位
功能定位：AI 驱动的演示文稿生成器，支持从文本提示（Prompt）、上传文档（PDF/PPTX/DOCX 等）或现有 PPTX 模板生成专业演示文稿。
隐私定位：所有数据处理在本地设备完成，无云端依赖，避免数据泄露风险。
生态定位：开源可扩展（Apache 2.0 协议），支持自定义模型、模板及 API 部署，适配开发者与非技术用户双重需求。

2. 核心价值（与商业工具的差异）
优势维度具体说明数据隐私本地运行，无数据上传至第三方服务器，适合处理敏感内容（如企业内部报告）。成本透明使用自有 API 密钥（如 OpenAI/Gemini），仅支付模型调用费用，无订阅费或隐藏成本。高度灵活支持多模型（OpenAI/Gemini/Ollama/ 自定义 API）、多图片生成源（DALL-E 3/pexels 等）。开源可定制可修改代码、自定义 HTML/Tailwind CSS 模板，甚至二次开发为团队内部 API 服务。

整体逻辑还是，先生成PPT每一个大纲，在根据每一页大纲生成对应内容和图片布局

# 参考

[1] AICG开源推荐-PPT生成-presenton, https://mp.weixin.qq.com/s/XmsNKx8iZh6n8hKsFzKSXw