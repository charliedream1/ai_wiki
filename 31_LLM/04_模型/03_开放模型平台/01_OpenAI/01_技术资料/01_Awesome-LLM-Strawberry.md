# 1. 相关论文
1. Github (2.6k stars): https://github.com/hijkzzz/Awesome-LLM-Strawberry

包含大量信息：

1. 关于o1的博客
   - 博客：Learning to Reason with LLMs
   - 作者：OpenAI
   - 链接：https://openai.com/index/learning-to-reason-with-llms/
   - 概述：这篇博客介绍了OpenAI o1的训练方法，其中包括链式推理、自我批评、验证、多步骤推理、任务分解和蒙特卡洛树搜索等技术。

2. 博客：OpenAI o1-mini
   - 作者：OpenAI
   - 链接：https://openai.com/index/openai-o1-mini-advancing-cost-efficient-reasoning/
   - 概述：介绍了o1 mini模型在推理成本和效率方面的改进，在保持高推理性能的同时，显著降低了计算和运行成本。

3. 博客：Finding GPT-4’s mistakes with GPT-4
   - 作者：OpenAI
   - 链接：https://openai.com/index/finding-gpt4s-mistakes-with-gpt-4/
   - 概述：讨论了如何利用GPT-4模型自身来发现和修正生成的错误。文章中提到的“自我审查方法”通过双重评估提高了错误检测的准确性，从而让模型输出的内容变得更加可靠。（文章发表时，已有OpenAI超级对齐团队成员离职，因此也被称为团队的“遗作”）

4. 博客：Summary of what we have learned during AMA hour with the OpenAI o1 team
   - 作者：Tibor Blaho
   - 链接：https://twitter-thread.com/t/1834686946846597281
   - 𝕏：https://x.com/btibor91/status/1834686946846597281
   - 概述：这篇博客总结了OpenAI团队在AMA（问答环节）中分享的关于o1模型的主要内容和特性。
   - 其中包括：模型的推理范式以及规模和性能、输入token上下文和模型能力、CoT（思维链）推理、API和使用限制、定价、微调和扩展等内容。

5. 博客：OpenAI’s Strawberry, LM self-talk, inference scaling laws, and spending more on inference
   - 作者：Nathan Lambert
   - 链接：https://www.interconnects.ai/p/openai-strawberry-and-inference-scaling-laws
   - 概述：文章探讨了OpenAI的新活“Strawberry”以及推理扩展定律，强调了推理计算在提升AI能力方面的重要性。而相较于单纯扩大模型规模，作者认为增加推理计算的投入能更有效地提高模型性能。（具有前瞻性的一篇博客，文章发布的时候o1还没发布）

6. 博客：Reverse engineering OpenAI’s o1
   - 作者：Nathan Lambert
   - 链接：https://www.interconnects.ai/p/reverse-engineering-openai-o1
   - 概述：文章详细讲了OpenAI的o1模型，重点在于它的推理能力。o1通过生成复杂的思维链来处理复杂任务，比以前的模型表现更出色。
     还讨论了o1的设计和训练细节，特别是它如何通过优化数据处理和算法来提高推理效率。同时指出，相比单纯增加模型规模，提升推理计算投入对提升模型性能更有效。

# 2. 其它论文

OpenAI o1贡献者参与撰写的论文
论文：Training Verifiers to Solve Math Word Problems
作者：Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, Christopher Hesse, John Schulman
团队：OpenAI
链接：https://arxiv.org/abs/2110.14168

概述：发布于2021年10月，文中指出虽然当前的先进语言模型在很多任务上表现很强，但它们在解决复杂的数学题时仍然遇到困难。为了解决这个问题，作者创建了一个叫GSM8K的数据集，其中包含8500个不同的小学数学题。
研究发现，即使是大规模的Transformer模型在这些题目上也表现不佳。为了提升表现，作者建议使用一个验证器来检查模型答案的准确性。
具体做法是让模型生成多个答案，然后选择验证器评分最高的答案。而这种方法显著提高了模型在GSM8K数据集上的表现，比传统的调整方法效果更好。

图片

论文：Generative Language Modeling for Automated Theorem Proving
作者：Stanislas Polu, Ilya Sutskever
团队：OpenAI
链接：https://arxiv.org/abs/2009.03393

概述：发布于2020年9月，探讨了基于Transformer的语言模型如何在自动定理证明中发挥作用。
研究的核心问题是，自动定理证明器在生成原创数学术语方面比不上人类，而这可能通过语言模型的生成能力得到解决。
作者介绍了一种叫做GPT-f的自动证明工具，用于Metamath形式化语言，并分析了它的效果。GPT-f成功发现了一些新短证明，这些证明被Metamath主要库接受，这是深度学习系统首次为形式数学社区提供并被采纳的证明。

图片

论文：Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
作者：Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
团队：Google Research, Brain Team（谷歌大脑)
链接：https://arxiv.org/pdf/2201.11903

概述：发布于2022年1月，文章讨论了如何通过生成一系列中间推理步骤（思维链）来大幅提升大型语言模型的复杂推理能力。
作者提出了一种叫做“思维链提示”的方法，具体做法是在提示中给出一些思维链的示例，帮助模型进行更深入的推理。最终实验结果显示，它在三个大型语言模型上都显著提高了它们在算术、常识和符号推理任务中的表现。

图片

论文：Let’s Verify Step by Step
作者：Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, Karl Cobbe
团队：OpenAI
链接：https://arxiv.org/abs/2305.20050

概述：发布于2023年5月，文章讨论了大型语言模型在复杂多步推理任务中的表现。
作者比较了两种训练方法：一种只关注最终结果，另一种关注每一步推理。结果显示，关注每一步推理的方法更有效，能在MATH数据集上提高到78%的成功率。
文中还强调了主动学习在提升训练效果中的重要性，并发布了一个包含80万个步骤级反馈的PRM800K数据集，用于训练最佳模型。

图片

论文：LLM Critics Help Catch LLM Bugs
作者：Nat McAleese, Rai Michael Pokorny, Juan Felipe Ceron Uribe, Evgenia Nitishinskaya, Maja Trebacz, Jan Leike
团队：OpenAI
链接：https://arxiv.org/abs/2407.00215

概述：发布于2024年6月，文中介绍了用“批评者”（CriticGPT）模型来提升机器学习模型输出的评估。
这些批评者模型能更有效地发现代码中的错误，甚至能找到人类可能忽略的问题。尽管这些模型有时会出错，但与人类结合使用可以减少误导，同时提高错误检测的效率。

图片

论文：Self-critiquing models for assisting human evaluators
作者：William Saunders, Catherine Yeh, Jeff Wu, Steven Bills, Long Ouyang, Jonathan Ward, Jan Leike
团队：OpenAI
链接：https://arxiv.org/pdf/2206.05802

概述：发布于2022年6月，文中介绍了一种方法，通过微调大型语言模型，让它们生成批评性评论，从而帮助找出摘要中的问题。
研究发现，这些评论可以有效识别摘要中的错误，包括有意误导的信息。大模型在生成有用评论和自我改进方面表现更好。
同时论文还提出了一个框架来评估模型的批评、生成和辨别能力，并指出即使是大型模型也可能有遗漏的知识。研究展示了如何用AI辅助人类改进机器学习系统，并公开了相关数据和样本。

图片

论文：Scalable Online Planning via Reinforcement Learning Fine-Tuning
作者：Arnaud Fickinger, Hengyuan Hu, Brandon Amos, Stuart Russell, Noam Brown
团队：Facebook AI
链接：https://arxiv.org/pdf/2109.15316

概述：文章介绍了一种新方法来改进图神经网络（GNN）的训练，特别是针对“图卷积”操作中的效率问题。
作者提出了一种名为“FastGCN”的算法，旨在提高图神经网络的计算速度和缩放能力。通过在训练过程中进行近似和优化，这种方法能够处理更大规模的图数据，从而在图数据分析任务中取得更好的性能。

# 参考

[1] 关注o1必备GitHub仓库，上线3天狂揽1.5k星！英伟达工程师出品，承诺持续更新, https://mp.weixin.qq.com/s/5C-wB8bzr-ysNO99Zg4DYQ