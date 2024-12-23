# 背景和问题

- 由于paddle OCR加了特殊的校验机制，需要.git文件夹下的版本信息校验，否则会导致安装失败。
- 直接下载代码仓或者从release下载的代码，都不包含.git文件夹，因此无法直接安装。
- 你需要直接clone项目，然后再安装，这样才能成功。

- Github (45.2k stars): https://github.com/PaddlePaddle/PaddleOCR
- 文档：https://paddlepaddle.github.io/PaddleOCR/latest/quick_start.html#__tabbed_1_2

# 解决方案

- 直接clone项目
- 注意（准备你所需要的文件）：
  - 原始代码仓有接近700M，拷贝到服务器，可能会比较费劲
  - 查看，主要是PaddleOCR\.git\objects\pack文件夹，这个文件夹很大，
    - 这个文件夹是git的版本信息，如果没有这个文件夹，就无法安装
    - 这个文件夹下一般有3个文件，你只需要拷贝最小的那2个，有一个最大的500M左右，不需要拷贝，也可也正常安装
- 将整个文件拷贝到服务器，然后再安装
- 安装
  - 进入PaddleOCR文件夹
  - 先安装paddlepaddle
    - cpu: `pip install paddlepaddle`
    - gpu: `python -m pip install paddlepaddle-gpu==3.0.0b1 -i https://www.paddlepaddle.org.cn/packages/stable/cu118/`
  - 执行安装命令
    - `pip install -e .`

# ppstructure多语种支持

由于layout及formula模型只支持中文英文, ch/zh，传入其它语种会报错，但ocr是支持多语种的，因此，修改源码，
将paddleocr主目录下的paddleocr.py，修改853行，加入`lang = 'ch'`即可。然后传入别的语种，
ocr可以进行多语种，而layout和formula对语种不是强依赖，所以多语种下也基本可以正常工作，唯独
table的识别可能存在问题，因为不支持多语种。

```python
lang = 'ch'
layout_model_config = get_model_config(
    "STRUCTURE", params.structure_version, "layout", lang
)
params.layout_model_dir, layout_url = confirm_model_dir_url(
    params.layout_model_dir,
    os.path.join(BASE_DIR, "whl", "layout"),
    layout_model_config["url"],
)
formula_model_config = get_model_config(
    "STRUCTURE", params.structure_version, "formula", lang
)
```
