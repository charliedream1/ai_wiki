# 1. n8n mcp

在最近的1.88.0版本，n8n终于官宣支持MCP了！

而且它不仅支持双向MCP，还支持添加本地（stdio）MCP。

高德的MCP-Server的SSE地址
https://mcp.amap.com/sse?key=在高德官网上申请的key
获取高德的key
https://console.amap.com/dev/key/app

# 2. Open WebUI MCP

资源链接：

- WebSite：https://docs.openwebui.com/
- Github：https://github.com/open-webui/mcpo

它能够将 MCP 工具的接口转换为 OpenAPI 兼容的 HTTP 服务器接口。其核心原理在于对 MCP 工具的 API 进行封装和转换，使得它们能够像标准的 OpenAPI 服务一样被调用。代理服务器负责处理传入的 HTTP 请求，将其转换为 MCP 工具能够理解的格式，然后将 MCP 工具的响应转换回标准的 HTTP 响应格式，从而实现了两者的无缝集成。


# 参考

[1] 斩获86K Star！最强开源MCP平台【双向+本地MCP】自由度拉满，太绝了～https://mp.weixin.qq.com/s/4sW9r_RCKPMgZy3eIbqCGw
[2] GitHub 十大开源 AI 项目盘点：从 MCP 到多智能体协作（万字）, https://mp.weixin.qq.com/s/SEZoyfxW4IQ2GinZdb-eWg