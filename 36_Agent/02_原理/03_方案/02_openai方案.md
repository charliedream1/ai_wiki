OpenAI官方突然发布了一份长达34页的《Agent实践指南》。

**核心观点二：从“能力失控”到“安全可控”——为Agent戴上“护栏”**

指南花了大量篇幅强调“护栏（Guardrails）”的重要性。

一个不受约束的Agent是危险且不可靠的。

官方建议构建一个分层的防御体系，包括相关性分类器（防止跑题）、安全分类器（防止恶意攻击）、PII过滤器（防止隐私泄露）、工具保障措施（评估工具风险）等。

同时，必须规划好人工干预（Human Intervention）机制，在关键时刻将控制权交还给人类。

# 参考

[1] 熬夜啃完OpenAI34页Agent指南，这3点让可研智能体开发提速50%, https://mp.weixin.qq.com/s/Ci1s0ujyf3bUaw804LSQFA
[2] OpenAI:构建Agent的实用指南, https://mp.weixin.qq.com/s/AgREA-yN6kjTW8CaSx19HQ