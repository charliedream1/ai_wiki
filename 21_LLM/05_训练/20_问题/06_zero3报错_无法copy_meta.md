1. 错误：

   NotImplementedError: Cannot copy out of meta tensor； no data!(多机多卡)

2. 解决

    模型参数初始化有问题
    在模型文件中，有个modeling_chatglm.py文件，大概750多行左右，将默认的empty_init=True，改为empty_init=False，即可

    ```python
    class ChatGLMModel(ChatGLMPreTrainedModel):
            # 修改这里的默认值
        def __init__(self, config: ChatGLMConfig, device=None, empty_init=True): 
            super().__init__(config)
            if empty_init:
                init_method = skip_init
            else:
                init_method = default_init
            init_kwargs = {}
    ```
   
   解释：

    按照原博的解释，这个错误通常是由于 Deepspeed 在使用自定义权重初始化时出现问题，
    而这些初始化可能需要从先前的训练中加载权重。如果在使用 Deepspeed 进行分布式训练时出现此错误，
    则需要在初始化模型时指定empty_init=False，以便在加载权重之前，权重矩阵不会被初始化为空。
    
    AutoModel.from_pretrained 是 Hugging Face Transformers 库中的一个方法，用于从预训练模型中加载权重。
    在 Deepspeed 分布式训练中，模型的初始化和权重加载可能需要特殊处理，因此需要使用 empty_init=False 
    参数来指定在加载权重之前不要将权重矩阵初始化为空。


# 参考

[1] 错误： NotImplementedError: Cannot copy out of meta tensor； no data!(多机多卡)，
    https://blog.csdn.net/Chrsitina_S/article/details/135129229