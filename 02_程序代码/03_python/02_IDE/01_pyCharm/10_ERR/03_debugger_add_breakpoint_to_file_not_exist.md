# 问题

在使用pycharm远程连接服务器上的 python 解释器进行调试的时候，每次都会提示

```text
pydev debugger: warning: trying to add breakpoint to file that does not exist：XXX(has no effect)
```

# 解决

这是因为有 breakpoint 记录，以前的文件的 breakpoint都会保存下来，所以虽然路径不在该项目中，所以pydev还是会尝试去添加 breakpoint 。

解决的方法是Run->View Breakpoint, 去掉显示出的breakpoint的勾选就可以了，可以看到和显示出的文件路径是一样的。


# 参考

[1] pydev debugger: warning: trying to add breakpoint to file that does not exist, 
    https://blog.csdn.net/u011394059/article/details/78668551