# 1. 资源 

- Github (13.8k stars): https://github.com/opendatalab/MinerU
- 文档：https://mineru.readthedocs.io/en/latest/index.html
- 在线体验：https://modelscope.cn/studios/OpenDataLab/MinerU
- 协议：AGPL-3.0 license

# 2. 模型下载

使用download.py之后，配置文件路径：/home/cestc/magic-pdf.json

# 3. 使用

模型加载：

```python
def init_model():
    from magic_pdf.model.doc_analyze_by_custom_model import ModelSingleton
    try:
        model_manager = ModelSingleton()
        txt_model = model_manager.get_model(False, False)
        logger.info(f"txt_model init final")
        ocr_model = model_manager.get_model(True, False)
        logger.info(f"ocr_model init final")
        return 0
    except Exception as e:
        logger.exception(e)
        return -1


model_init = init_model()
logger.info(f"model_init: {model_init}")
```

文本转markdown

```python
import os

from loguru import logger
from magic_pdf.pipe.UNIPipe import UNIPipe
from magic_pdf.rw.DiskReaderWriter import DiskReaderWriter


try:
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    demo_name = "demo1"
    pdf_path = os.path.join(current_script_dir, f"{demo_name}.pdf")
    pdf_bytes = open(pdf_path, "rb").read()
    jso_useful_key = {"_pdf_type": "", "model_list": []}
    local_image_dir = os.path.join(current_script_dir, 'images')
    image_dir = str(os.path.basename(local_image_dir))
    image_writer = DiskReaderWriter(local_image_dir)
    pipe = UNIPipe(pdf_bytes, jso_useful_key, image_writer)
    pipe.pipe_classify()
    pipe.pipe_analyze()
    pipe.pipe_parse()
    md_content = pipe.pipe_mk_markdown(image_dir, drop_mode="none")
    with open(f"{demo_name}.md", "w", encoding="utf-8") as f:
        f.write(md_content)
except Exception as e:
    logger.exception(e)
```

FAQ: https://github.com/opendatalab/MinerU/issues/932

```text
1. 问：也就是是说Pipeline的那段代码还是可以原封不动的使用，init_model调用之后，pipeline自动就能识别模型已经加载，就不会加载了吧？
   答：是的，init_model调用之后，pipeline自动就能识别模型已经加载，就不会加载了。
2. 问：您说的模型是整包加载的，相当于只需要model_manager = ModelSingleton()这一句就够了，就自动加载所有模型？
   答： 是的，model_manager = ModelSingleton()这一句就够了，就自动加载所有模型。
3. 问：txt_model = model_manager.get_model(False, False)，这个False, False代表什么？
   答：ocr和ocrlog的开关，可以跳转到方法实现自己看源码
4. 问：image_writer = DiskReaderWriter(local_image_dir)这段代码会不会写缓存文件，如果我启动好几个进程，但local_image_dir都指定的一个目录，会不会导致最后的markdown结果互相干扰？
   答：不会干扰，设计之初就是为了将所有图片平铺写入到同一目录的，图片有自己的独特的命名，保证不会互相干扰
5. 问：如果布使用Pipeline，如何使用流程种某一个模型，单独识别？比如我只想识别公式或者ocr？
   答：参考magic_pdf/model/pdf_extract_kit.py 中的实现

```