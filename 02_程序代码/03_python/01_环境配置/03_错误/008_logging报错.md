# 1. 问题

安装包时，logging报错：raise NotImplementedError, 'emit must be implemented '


# 2. 解决方法

因为python内置里面已经有logging这个模块，所以不需要再安装

- 不要安装logging这个包
- 若已部分安装，在site-packages里面找到关于logging的文件，删掉

# 参考

[1] import logging报错raise notimplementederror 'emit must be implemented ' ^，https://www.cnblogs.com/aixiao07/p/8973531.html