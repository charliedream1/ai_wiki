问题

/bin/sh:1:nvcc:not found

![](.02_llama_cpp_images/nvcc找不到.png)

解决方法

查看/usr/local/cuda/bin下是否有nvcc可执行程序，如果有则说明nvcc没有被设置为系统变量，执行如下命令

$ cd /usr/local/cuda/bin && ls

发现了nvcc确实已安装，则只需执行如下命令将其加入系统变量中:

$ sudo vi ~/.bashrc

在末尾行添加环境变量export PATH=$PATH:/usr/local/cuda/bin

这时再新建终端，然后切换到目录下进行make时就不会出现错误了。

# 参考

[1] 解决nvcc找不到的问题/bin/sh:1:nvcc:not found，https://blog.csdn.net/weixin_43046653/article/details/100019901