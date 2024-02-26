# 1. 中文
## 1.1 综合数据

1. BelleGroup/train_1M_CN
   - https://huggingface.co/datasets/BelleGroup/train_1M_CN
   - 917k条， 458M
   - ![](.02_SFT数据_images/Belle_train_1m_cn数据样例.png) 

2. MOSS数据
   - Github: https://github.com/OpenLMLab/MOSS/tree/main/SFT_data
   - https://huggingface.co/datasets/fnlp/moss-003-sft-data
   - 3G
   - ![](.02_SFT数据_images/moss数据样例.png)
   - ![](.02_SFT数据_images/MOSS数据类别.png)

3. c-s-ale/alpaca-gpt4-data-zh
   - https://huggingface.co/datasets/c-s-ale/alpaca-gpt4-data-zh
   - license: cc-by-sa-4.0
   - 48.8k条，35.1M
   - 论文：Instruction Tuning with GPT-4
   - ![](.02_SFT数据_images/alpaca-gpt4-cn数据样例.png)

4. FlagInstruct
   - 智源开源数据
   - Github: https://github.com/FlagOpen/FlagInstruct
   - Data: https://huggingface.co/datasets/BAAI/COIG/tree/main
   - 翻译指令：67,798
   - 考试指令：63,532, CoT数据
   - Human Value Alignment Instructions (34,471)
   - Counterfactural Correction Multi-round Chat (13,653)：平均5轮对话
   - Leetcode Instructions (11,737)

5. Alplca_zn_51k
   - https://github.com/enze5088/Chatterbox/tree/main/docs/datasets

6. Firefly-train-1.1M
   - (建议从Huggingface下载，modelscope存在问题) https://huggingface.co/datasets/YeungNLP/firefly-train-1.1M
   - Github (3.6k stars) https://github.com/yangjianxin1/Firefly
   - 模型（使用LLM pruner对Bloom词表裁剪，仅取出常用的中英文词表，大大降低了模型参数量）：https://huggingface.co/YeungNLP/firefly-bloom-1b4
   - ![](.02_SFT数据_images/数据样例.png)
   - 收集了23个常见的中文数据集，对于每个任务，由人工书写若干种指令模板，保证数据的高质量与丰富度，数据量为115万 。数据分布如下图所示：
   - ![](.02_SFT数据_images/Firefly数据分布.png)
   - 训练数据集的token长度分布如下图所示，绝大部分数据的长度都小于600：
   - ![](.02_SFT数据_images/长度分布.png)

## 1.2 对话数据

1. 中文闲聊语料库LCCC
   - 论文名称：《A Large-Scale Chinese Short-Text Conversation Dataset》
   - 论文链接：https://arxiv.org/abs/2008.03946
   - 项目地址：https://github.com/thu-coai/CDial-GPT
   
   ![](.02_对话数据_images/LCCC数据集.png)

2. ShareGPT
   - https://sharegpt.com/
   - 使用多轮对话历史记录,包括约9w条来自人类的提问和来自ChatGPT和其他聊天机器人的回复。
     我们通用能力的评测指标为MT-Bench。


## 1.3 问答数据

1. 百度问答100w
   - https://github.com/CyberCommy/baidu-qa-100w

## 1.4 特定类别
### 1.4.1 代码
1. Code Alpaca
   - https://github.com/sahil280114/codealpaca
   - 旨在构建一个遵循指令，生成代码的LLaMA模型，构建方式完全基于Stanford Alpaca，
      包含20K对的代码数据，我们代码生成的评测指标为HumanEval。

### 1.4.2 数学
1. GSM8K RFT 
   - https://huggingface.co/datasets/gsm8k
   - https://arxiv.org/pdf/2110.14168v1.pdf
   - 是一个增强的数学推理数据集，它基于GSM8K数据集[4]并结合RFT策略整合了多条推理路径。
     训练集中包含7.5K个问题和110K个回答，我们所有实验数学的评测指标为GSM8k测试集分数。
   
2. YeungNLP/school_math_0.25M
   - https://huggingface.co/datasets/YeungNLP/school_math_0.25M
   - 25w, Belle开源

### 1.4.3 字词错误检测、纠正和文本润色

1. 序列猴子
   - 出自出门问问
   - 各5000条
   - 下载：http://share.mobvoi.com:5000/sharing/HXB6QPLAi

### 1.4.4 古诗

1. 序列猴子
   - 古诗今译
   - 出自出门问问
   - 共计逾680,000首
   - 下载：http://share.mobvoi.com:5000/sharing/WNpEqItCg

## 1.5 专有领域

1. 医疗类数据
   - https://huggingface.co/datasets/shibing624/medical
   - 预训练362k条，约1G
    ![](.01_预训练数据_images/医疗预训练中文数据.png)
   - 微调2.07M条
     ![](.01_预训练数据_images/医疗微调中文数据.png)
   - 奖励模型4k条
     ![](.01_预训练数据_images/奖励模型.png)

## 1.6 其它数据

1. 对话重写：
   - 1.64M 个数据
   - https://huggingface.co/datasets/infgrad/dialogue_rewrite_llm
   
***

# 2. 英文

## 2.1 对话数据

1. ultrchat
   - https://huggingface.co/datasets/YeungNLP/ultrachat
   - 清华大学140w+对话数据

## 2.2 特定类别
### 2.2.1 复杂指令

1. WizardLM_evol_instruct_V2_143k 
   - https://huggingface.co/datasets/YeungNLP/WizardLM_evol_instruct_V2_143k
   - 复杂指令143k

# 参考

[1] 动手做个DialoGPT：生成式多轮对话模型, https://blog.csdn.net/xixiaoyaoww/article/details/108656532
[2] 百度QA100万数据集, https://mp.weixin.qq.com/s/SJQX2tNJ5kz3--ReWAbZDg
