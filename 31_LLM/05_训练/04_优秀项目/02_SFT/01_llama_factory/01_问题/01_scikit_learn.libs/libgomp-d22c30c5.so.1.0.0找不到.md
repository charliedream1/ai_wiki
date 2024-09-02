# 问题

scikit_learn.libs/libgomp-d22c30c5.so.1.0.0: cannot allocate memory in static TLS block

# 原因

经过网络查询，这是libgomp在arm平台上的一个bug。libgomp gets the statically allocated TLS space that it needs, before the optimization of handing out that space to other libraries kicks in .
即：libgomp-d22c30c5.so.1.0.0运行时占用了TLS部分内存.

# 解决方案

方法一

注意报错信息中已经提示了找不到的库的路径，直接引用该库即可（实测有效）

```bash
export LD_PRELOAD=$LD_PRELOAD:/usr/local/python3.7.5/lib/python3.7/site-packages/scikit_learn.libs/libgomp-d22c30c5.so.1.0.0
```

方法二

（未验证）如参考文献1，升级glibc版本到2.32.

# 参考文献

[1] 【解决scikit_learn.libs/libgomp-d22c30c5.so.1.0.0:cannot allocate memory in static TLS block问题】, https://blog.csdn.net/lhb_0531/article/details/121508293