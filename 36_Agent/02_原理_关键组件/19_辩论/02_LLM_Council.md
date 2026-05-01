Andrej Karpathy（AK）又整活了！  

项目地址：https://github.com/karpathy/llm-council

中文名可直译为「大模型理事会」，核心创意：让一群大模型像联合国开会一样，互相匿名打分，最后由主席模型给出最客观、最高质量的答案。



三步走，彻底消灭单一模型偏见：



1. 并行提问：同时调用多个模型（GPT-4o、Claude 3.5、Gemini 等），快速收集“第一意见”。

2. 匿名互评：把所有答案打乱标签（A/B/C），每个模型给其他答案按「准确性」+「洞见度」打 1-10 分并写评语，强行实现客观排名。

3. 主席总结：指定一个最强模型（如 o1-preview）当“秘书长”，综合所有答案+评分，输出最终高质量答案。



技术栈极简本地可跑：

- 后端：FastAPI + async httpx + OpenRouter 一键调用几十个模型

- 前端：React + Vite + Markdown 渲染

- 存储：直接扔 JSON 文件

- 启动：一行 sh 脚本搞定



这就是它几天就 5k+ Star 的原因：  

既是生产力工具，又是顶级娱乐，还顺手演示了「集体智能」如何吊打单一模型。



这个思路，对我们在开发生产级的agent应用是蛮有启发的。

# 参考

[1] https://mp.weixin.qq.com/s/8vRiuWQDbXj0X1_XSfOdJQ