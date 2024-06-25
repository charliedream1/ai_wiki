# 问题

RuntimeError: No such operator torchvision::nms

![](.006_RuntimeError No such operator torchvision nms_images/问题.png)

# 解决方案

一般都是由于torchvision版本和torch及cuda toolkit不配套

卸载了在conda中重新安装即可
- 查看一下如果torch和cuda toolkit版本配套，只重安torchvision即可
- 如果都不配套，则全部重新安装

# 参考

[1] RuntimeError: No such operator torchvision::nms问题解决方法，https://blog.csdn.net/qq_41590635/article/details/112384718
