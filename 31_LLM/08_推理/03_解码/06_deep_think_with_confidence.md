
DEEP THINK WITH CONFIDENCE
这篇文章的核心观点在于：在多路径推理/思考过程中，不应将所有轨迹一视同仁，而应依据置信度区分其“质量”。基于此，作者提出了数种置信度指标，并在实验中发现“最弱环节”相关的两个指标效果最优。具体来说：

Bottom-10% Group Confidence：对每条推理轨迹，先用滑动窗口（例如每 n token 一个窗口）计算每个窗口的 token-置信度平均值，得到一组窗口置信度；然后取其中最低 10 % 窗口的平均值，作为该轨迹的底部置信度指标。这个指标试图反映“推理途中最薄弱那部分”的平均置信度。
Lowest Group Confidence：同样基于滑动窗口，对轨迹中所有窗口取最低一个窗口的置信度，作为该轨迹的最差段落的置信度指标。即关注“最糟糕的一段”。
有了这两个指标之后，在思考模式上，作者分别探讨了两种场景：

在线模式（online thinking）：在推理过程中实时监控置信度信号，一旦路径落入低置信度状态，可以及时中止、剔除或者调整；最终，当多条路径都输出答案时，每条轨迹的输出置信度（例如使用 Bottom-10% Confidence）会参与投票加权，对高置信度路径赋予更大权重。
离线模式（offline thinking）：先生成多条完整轨迹，然后再依据置信度进行筛选或加权，只让高置信度的轨迹参与最终的答案决定。
整个方法是 training-free, inference-time only 的，和self-evlove相关的工作，如SE-Agent（SE-Agent: Self-Evolution Trajectory Optimization in Multi-Step Reasoning with LLM-Based Agents）一样都可以产生高质量的轨迹来做agentic rl的训练