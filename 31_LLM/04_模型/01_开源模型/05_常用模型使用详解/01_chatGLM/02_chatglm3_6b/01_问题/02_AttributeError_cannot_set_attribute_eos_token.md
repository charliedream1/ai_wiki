1. 问题
   ```bash
   OSError: C:\Users\Naozu\Downloads\chatglm3-6b-cantonese-stage1 does not appear to have a file named config.json. Checkout 'https://huggingface.co/C:\Users\Naozu\Downloads\chatglm3-6b-cantonese-stage1/main' for available files.
    10/29/2023 18:19:09 - WARNING - llmtuner.tuner.core.loader - Checkpoint is not found at evaluation, load the original model.
    Traceback (most recent call last):
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\gradio\routes.py", line 442, in run_predict
        output = await app.get_blocks().process_api(
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\gradio\blocks.py", line 1389, in process_api
        result = await self.call_function(
                 ^^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\gradio\blocks.py", line 1108, in call_function
        prediction = await utils.async_iteration(iterator)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\gradio\utils.py", line 346, in async_iteration
        return await iterator.__anext__()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\gradio\utils.py", line 339, in __anext__
        return await anyio.to_thread.run_sync(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\anyio\to_thread.py", line 33, in run_sync
        return await get_async_backend().run_sync_in_worker_thread(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\anyio\_backends\_asyncio.py", line 2106, in run_sync_in_worker_thread
        return await future
               ^^^^^^^^^^^^
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\anyio\_backends\_asyncio.py", line 833, in run
        result = context.run(func, *args)
                 ^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\gradio\utils.py", line 322, in run_sync_iterator_async
        return next(iterator)
               ^^^^^^^^^^^^^^
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\gradio\utils.py", line 691, in gen_wrapper
        yield from f(*args, **kwargs)
      File "C:\Users\Naozu\Downloads\LLaMA-Factory-main\src\llmtuner\webui\chatter.py", line 63, in load_model
        super().__init__(args)
      File "C:\Users\Naozu\Downloads\LLaMA-Factory-main\src\llmtuner\chat\stream_chat.py", line 15, in __init__
        self.model, self.tokenizer = load_model_and_tokenizer(model_args, finetuning_args)
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\Naozu\Downloads\LLaMA-Factory-main\src\llmtuner\tuner\core\loader.py", line 71, in load_model_and_tokenizer
        tokenizer = AutoTokenizer.from_pretrained(
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\transformers\models\auto\tokenization_auto.py", line 738, in from_pretrained
        return tokenizer_class.from_pretrained(pretrained_model_name_or_path, *inputs, **kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\transformers\tokenization_utils_base.py", line 2017, in from_pretrained
        return cls._from_pretrained(
               ^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\transformers\tokenization_utils_base.py", line 2249, in _from_pretrained
        tokenizer = cls(*init_inputs, **init_kwargs)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\Naozu/.cache\huggingface\modules\transformers_modules\chatglm3-6b-cantonese-stage1\tokenization_chatglm.py", line 93, in __init__
        super().__init__(padding_side=padding_side, clean_up_tokenization_spaces=clean_up_tokenization_spaces, **kwargs)
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\transformers\tokenization_utils.py", line 363, in __init__
        super().__init__(**kwargs)
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\transformers\tokenization_utils_base.py", line 1604, in __init__
        super().__init__(**kwargs)
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\transformers\tokenization_utils_base.py", line 861, in __init__
        setattr(self, key, value)
    AttributeError: property 'eos_token' of 'ChatGLMTokenizer' object has no setter
    Traceback (most recent call last):
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\gradio\routes.py", line 442, in run_predict
        output = await app.get_blocks().process_api(
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\gradio\blocks.py", line 1389, in process_api
        result = await self.call_function(
                 ^^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\gradio\blocks.py", line 1108, in call_function
        prediction = await utils.async_iteration(iterator)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\gradio\utils.py", line 346, in async_iteration
        return await iterator.__anext__()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\gradio\utils.py", line 339, in __anext__
        return await anyio.to_thread.run_sync(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\anyio\to_thread.py", line 33, in run_sync
        return await get_async_backend().run_sync_in_worker_thread(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\anyio\_backends\_asyncio.py", line 2106, in run_sync_in_worker_thread
        return await future
               ^^^^^^^^^^^^
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\anyio\_backends\_asyncio.py", line 833, in run
        result = context.run(func, *args)
                 ^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\gradio\utils.py", line 322, in run_sync_iterator_async
        return next(iterator)
               ^^^^^^^^^^^^^^
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\gradio\utils.py", line 691, in gen_wrapper
        yield from f(*args, **kwargs)
      File "C:\Users\Naozu\Downloads\LLaMA-Factory-main\src\llmtuner\webui\chatter.py", line 63, in load_model
        super().__init__(args)
      File "C:\Users\Naozu\Downloads\LLaMA-Factory-main\src\llmtuner\chat\stream_chat.py", line 15, in __init__
        self.model, self.tokenizer = load_model_and_tokenizer(model_args, finetuning_args)
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\Naozu\Downloads\LLaMA-Factory-main\src\llmtuner\tuner\core\loader.py", line 71, in load_model_and_tokenizer
        tokenizer = AutoTokenizer.from_pretrained(
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\transformers\models\auto\tokenization_auto.py", line 738, in from_pretrained
        return tokenizer_class.from_pretrained(pretrained_model_name_or_path, *inputs, **kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\transformers\tokenization_utils_base.py", line 2017, in from_pretrained
        return cls._from_pretrained(
               ^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\transformers\tokenization_utils_base.py", line 2249, in _from_pretrained
        tokenizer = cls(*init_inputs, **init_kwargs)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\Naozu/.cache\huggingface\modules\transformers_modules\chatglm3-6b-cantonese-stage1\tokenization_chatglm.py", line 93, in __init__
        super().__init__(padding_side=padding_side, clean_up_tokenization_spaces=clean_up_tokenization_spaces, **kwargs)
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\transformers\tokenization_utils.py", line 363, in __init__
        super().__init__(**kwargs)
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\transformers\tokenization_utils_base.py", line 1604, in __init__
        super().__init__(**kwargs)
      File "C:\Users\Naozu\AppData\Local\Programs\Python\Python311\Lib\site-packages\transformers\tokenization_utils_base.py", line 861, in __init__
        setattr(self, key, value)
      AttributeError: property 'eos_token' of 'ChatGLMTokenizer' object has no setter
     ```

# 2. 解决方法

参考: 
- chatglm3 微调完成之后导出成功，但无法加载 #1307
- https://github.com/hiyouga/LLaMA-Factory/issues/1307

把源目录除了 bin 和 pytorch_model.bin.index.json 以外的文件全部复制到导出目录中覆盖