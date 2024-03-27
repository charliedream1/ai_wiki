# 1. 简介
覆盖各类模型，包含pre-train, sft, rm, rflh
- https://github.com/hiyouga/LLaMA-Factory
- 5.7k Stars

# 常见bug

1. ModuleNotFoundError: No module named 'transformers_modules.chatglm3_6b_32k

    解决方法：模型输出的文件夹名称最后不要有小数点和数字，比如：xxx_1.0,
            ".0" 会被忽略，模型去找xxx_1，找不到就会报错