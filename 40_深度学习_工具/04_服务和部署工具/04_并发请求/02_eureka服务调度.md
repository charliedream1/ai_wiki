Q: 如何多进程运行paddleocr？
A：实例化多个paddleocr服务，然后将服务注册到注册中心，之后通过注册中心统一调度即可，关于注册中心，可以搜索eureka了解一下具体使用，其他的注册中心也行。

# 参考

[1] PaddleOCR FAQ，https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.7/doc/doc_ch/FAQ.md