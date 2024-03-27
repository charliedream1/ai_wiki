# 1. 简介

- Github (36.6 k)：https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.7/ppstructure/layout/README_ch.md
- 文档来源：PaddleOCR
- 数据：包含数据汇总和自己开源的数据

安装
```text
paddleocr==2.7.0.3
paddlepaddle-gpu==2.5.2
```

如使用图像方向分类功能，需安装paddleclas，安装过程可能出现faiss-cpu编译失败 (网上issue说使用python3.9, 未进行验证)
```shell
# 安装 图像方向分类依赖包paddleclas（如不需要图像方向分类功能，可跳过）
pip3 install paddleclas>=2.4.3
```

# 2. 问题

1. 问题：ImportError: cannot import name 'PaddleOCR' from partially initialized module 
   'paddleocr' (most likely due to a circular import) #4780
   - 来源：https://github.com/PaddlePaddle/PaddleOCR/issues/4780
   - 解决方法：可能文件名可库里的名字冲突，重命名文件名(比如，不要有ppstructure.py文件)

2. ppstructure输出的版面图比原始的图片多出来一些无关的东西
   - https://github.com/PaddlePaddle/PaddleOCR/issues/11617
   - 解决方法：右侧是检测模型的可视化输出效果哈，如果不需要可以只输出draw_layout （注释ocr部分）:
     https://github.com/PaddlePaddle/PaddleOCR/blob/0525f6bb01bfed401f767894619f6a25ee750892/ppstructure/utility.py#L131C5-L131C16