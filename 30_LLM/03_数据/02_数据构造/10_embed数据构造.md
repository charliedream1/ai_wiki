1. BAAI-MLDR
   - 13国多语种文件检索数据，BGE-M3模型开源数据
   - 基于Wikipeida, Wudao and mC4构建，随机抽取片段，GPT3.5生成问题，问题和片段
     构成pair对
   - 下载路径：https://huggingface.co/datasets/Shitao/MLDR
   - prompt: “You are a curious AI assistant, please generate one 
     specific and valuable question based on the following text. 
     The generated question should revolve around the core 
     content of this text, and avoid using pronouns (e.g., ”this”). 
     Note that you should generate only one question, without 
     including additional content:”.