# 问题

```bash
  File "/home/miniconda3/envs/MinerU/lib/python3.10/site-packages/magic_pdf/model/doc_analyze_by_custom_model.py", line 98, in custom_model_init
    from magic_pdf.model.pdf_extract_kit import CustomPEKModel
  File "/home/miniconda3/envs/MinerU/lib/python3.10/site-packages/magic_pdf/model/pdf_extract_kit.py", line 23, in <module>
    from magic_pdf.model.sub_modules.model_init import AtomModelSingleton
  File "/home/miniconda3/envs/MinerU/lib/python3.10/site-packages/magic_pdf/model/sub_modules/model_init.py", line 9, in <module>
    from magic_pdf.model.sub_modules.mfr.unimernet.Unimernet import UnimernetModel
  File "/home/miniconda3/envs/MinerU/lib/python3.10/site-packages/magic_pdf/model/sub_modules/mfr/unimernet/Unimernet.py", line 9, in <module>
    from unimernet.common.config import Config
  File "/home/miniconda3/envs/MinerU/lib/python3.10/site-packages/unimernet/__init__.py", line 18, in <module>
    from unimernet.tasks import *
  File "/home/miniconda3/envs/MinerU/lib/python3.10/site-packages/unimernet/tasks/__init__.py", line 10, in <module>
    from unimernet.tasks.unimernet_train import UniMERNet_Train
  File "/home/miniconda3/envs/MinerU/lib/python3.10/site-packages/unimernet/tasks/unimernet_train.py", line 2, in <module>
    import evaluate

  File "/home/llm_trainer_yun/src/evaluate.py", line 1, in <module>
    from llmtuner import Evaluator

  File "/home/llm_trainer_yun/src/llmtuner/__init__.py", line 3, in <module>
    from .api import create_app

  File "/home/llm_trainer_yun/src/llmtuner/api/__init__.py", line 1, in <module>
    from .app import create_app

  File "/home/llm_trainer_yun/src/llmtuner/api/app.py", line 9, in <module>
    from ..chat import ChatModel

  File "/home/llm_trainer_yun/src/llmtuner/chat/__init__.py", line 1, in <module>
    from .chat_model import ChatModel

  File "/home/llm_trainer_yun/src/llmtuner/chat/chat_model.py", line 8, in <module>
    from ..data import get_template_and_fix_tokenizer

  File "/home/llm_trainer_yun/src/llmtuner/data/__init__.py", line 1, in <module>
    from .loader import get_dataset

  File "/home/llm_trainer_yun/src/llmtuner/data/loader.py", line 10, in <module>
    from .parser import get_dataset_list

  File "/home/llm_trainer_yun/src/llmtuner/data/parser.py", line 7, in <module>
    from ..extras.misc import use_modelscope

  File "/home/llm_trainer_yun/src/llmtuner/extras/misc.py", line 6, in <module>
    from peft import PeftModel

ModuleNotFoundError: No module named 'peft'
```

# 分析

可以看到其实不是MinerU需要peft，而是可能路径引用的问题，导致调用我自己的项目中的src文件从而引发了错误。很可能是路径引用以及同名文件导致。

即便尝试安装peft，又会出现其它错误。

# 解决

删除运行代码路径中的src文件夹，重新运行即可。
