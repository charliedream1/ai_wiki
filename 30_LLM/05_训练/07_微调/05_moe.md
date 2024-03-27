1. Mstral MOE
    
   - Github:（非官方） https://github.com/open-compass/MixtralKit
   - 模型（hugging face格式版本）：https://huggingface.co/DiscoResearch/DiscoLM-mixtral-8x7b-v2
   - 评测脚本：https://github.com/EleutherAI/lm-evaluation-harness
   
   训练数据
   ```text
    * [Synthia](https://huggingface.co/datasets/migtissera/Synthia-v1.3)
    * [MetaMathQA](https://huggingface.co/datasets/meta-math/MetaMathQA)
    * NousReseach Capybara (currently not public)
   ```
   
   Prompt格式
   ```text
    <|im_start|>system
    You are DiscoLM, a helpful assistant.
    <|im_end|>
    <|im_start|>user
    Please tell me possible reasons to call a research collective "Disco Research"<|im_end|>
    <|im_start|>assistant
   ```
   
   使用模板
   ```python
    chat = [
      {"role": "system", "content": "You are DiscoLM, a helpful assistant."},
      {"role": "user", "content": "Please tell me possible reasons to call a research collective Disco Research"}
    ]
    tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
    ```
   
    ```python
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer
    
    model = AutoModelForCausalLM.from_pretrained("DiscoResearch/DiscoLM-mixtral-8x7b-v2", low_cpu_mem_usage=True, device_map="auto", trust_remote_code=True)
    tok = AutoTokenizer.from_pretrained("DiscoResearch/DiscoLM-mixtral-8x7b-v2")
    chat = [
      {"role": "system", "content": "You are DiscoLM, a helpful assistant."},
      {"role": "user", "content": "Please tell me possible reasons to call a research collective Disco Research"}
    ]
    x = tokenizer.apply_chat_template(chat, tokenize=True, return_tensors="pt", add_generation_prompt=True).cuda()
    x = model.generate(x, max_new_tokens=128).cpu()
    print(tok.batch_decode(x))
    ```

2. 斯坦福轻量MOE框架

   - https://github.com/stanford-futuredata/megablocks
   
   
# 参考

[1] 疯狂24小时：一系列基于Mstral MOE模型微调模型、框架被网友开源, https://mp.weixin.qq.com/s/jdzHVS-0sfkMraPVb2f9XA