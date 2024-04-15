1. AttributeError: 'QWenTokenizer' object has no attribute 'IMAGE_ST'
   
    参考：
    - https://github.com/QwenLM/Qwen-VL/issues/287
    - https://huggingface.co/MMInstruction/Silkie/discussions/1
    - https://github.com/Yuliang-Liu/Monkey/issues/69
   
    方法1：
 
    I put super().init() under IMAGE_ST in tokenization_qwen.py

    ![](.02_TextMonkey问题_images/代码修改.png)

     方法2：  
     使用transformers==4.32.0
