Gemini CLI OpenAI Worker是一个基于Cloudflare Workers的项目，其核心功能是将Google Gemini模型转换为OpenAI兼容的API端点，使用户能够通过熟悉的OpenAI API模式（包括官方SDK和第三方客户端如Open WebUI）无缝访问Gemini的最新模型。该项目利用OAuth2认证机制，无需传统的API密钥，而是通过用户的Google账户进行身份验证，并智能地管理和缓存访问令牌。它支持多模态对话，可处理Base64编码或URL形式的图像输入，提供实时流式响应，并能通过Google Code Assist API利用Google的免费层服务，甚至为特定模型生成模拟的思考过程输出，作为一个高效的中间转换层。

地址：https://github.com/GewoonJaap/gemini-cli-openai

# 参考

[1] 微软开源AI编程伴侣GitHub Copilot；腾讯开源高效多专家大语言模型Hunyuan-A13B, https://mp.weixin.qq.com/s/fDGP7Y6AL65NfKiKOh6cmw