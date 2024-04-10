# 问题

pycharm远程调试时，debug （sanic/gradio）模型出现如下错误，但是直接运行是没有问题的。

报了这个错：`RuntimeError: Cannot run the event loop while another loop is running`

# 解决

解决：`pip uninstall uvloop`

(但不确定是否会有其他问题，暂时解决了这个问题，因为uvloop可以提高异步并发性能，可能会影响性能)

使用pycharm 2023.3版本之前没有发现这个问题，2024.1远程调试时会出现此问题

# 参考

[1] nest_asyncio出现错误，https://www.cnblogs.com/rianley/p/14790675.html