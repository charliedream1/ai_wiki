# 1. 资源
- 本数据集为中文开源蒸馏满血R1的数据集，数据集中不仅包含math数据，还包括大量的通用类型数据，总数量为110K。
- 中文基于满血DeepSeek-R1蒸馏数据集-110k-SFT版本:https://modelscope.cn/datasets/liucong/Chinese-DeepSeek-R1-Distill-data-110k-SFT
- 中文基于满血DeepSeek-R1蒸馏数据集-110k:https://modelscope.cn/datasets/liucong/Chinese-DeepSeek-R1-Distill-data-110k
- 数据分布
  - Math：共计36568个样本，
  - Exam：共计2432个样本，
  - STEM：共计12648个样本，
  - General：共计58352，包含弱智吧、逻辑推理、小红书、知乎、Chat等
  
# 2. 数据集蒸馏细节

数据的prompt源来自如下数据集：
- Haijian/Advanced-Math
- gavinluo/applied_math
- meta-math/GSM8K_zh
- EduChat-Math
- m-a-p/COIG-CQIA
- m-a-p/neo_sft_phase2
- hfl/stem_zh_instruction

同时为了方便大家溯源，在每条数据的repo_name字段中都加入的原始数据源repo。

在蒸馏过程中，按照DeepSeek-R1官方提供的细节，进行数据蒸馏。
- 不增加额外的系统提示词
- 设置temperature为0.6
- 如果为数学类型数据，则增加提示词，“请一步步推理，并把最终答案放到 \boxed{}。”
- 防止跳出思维模式，强制在每个输出的开头增加"\n"，再开始生成数据

# 3. 数据打分细节

数据生成结果进行了二次校验，并保留了评价分数。

针对Math和Exam数据，先利用Math-Verify进行校对，无法规则抽取结果的数据，再利用Qwen2.5-72B-Instruct模型进行打分，正确为10分，错误为0分。

针对其他数据，直接利用Qwen2.5-72B-Instruct模型从无害性、有用性、正确性/完整性三个角度进行打分，分值范围为0-10分。

本数据集保留了最后打分结果，为后续的数据筛选提供帮助，但注意，所有打分均基于模型，因此评分可能并不准确，请斟酌使用。

# 4. 局限性

由于数据是由蒸馏DeepSeek-R1生成的，未经严格验证，在事实性和其他方面还存在一些不足。因此，在使用此数据集时，请务必注意甄别。

本数据集不代表任何一方的立场、利益或想法，无关任何团体的任何类型的主张。因使用本数据集带来的任何损害、纠纷，本项目的开发者不承担任何责任。

# 参考

[1] 强强联合，开源中文DeepSeek-R1蒸馏数据集联合魔搭社区，一起来训练中文版推理模型！https://mp.weixin.qq.com/s/b_pd_Tml9G-7bOODZ-GzKA