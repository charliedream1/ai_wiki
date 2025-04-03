强化学习框架（6.1k stars）：https://github.com/volcengine/verl

Verl 是一个灵活、高效且可用于生产用途的 RL 训练库，适用于大型语言模型 （LLM）。

verl 是 HybridFlow： A Flexible and Efficient RLHF Framework 论文的开源版本。

VERL 非常灵活且易于使用：

- 轻松扩展各种 RL 算法：混合控制器编程模型支持灵活表示和高效执行复杂的训练后数据流。用几行代码构建 RL 数据流，例如 GRPO、PPO。
- 现有 LLM 基础设施与模块化 API 的无缝集成：解耦计算和数据依赖性，实现与现有 LLM 框架的无缝集成，例如 FSDP、Megatron-LM、vLLM、SGLang 等
- 灵活的设备映射：支持将模型以各种方式放置在不同的 GPU 集上，以实现不同集群大小的高效资源利用率和可扩展性。
- 与流行的 HuggingFace 模型随时集成

Verl 在以下方面速度快：
- 最先进的吞吐量：SOTA LLM 训练和推理引擎集成以及 SOTA RL 吞吐量。
- 使用 3D-HybridEngine 进行高效的参与者模型重新分片：消除内存冗余，并显著减少训练和生成阶段之间过渡期间的通信开销。