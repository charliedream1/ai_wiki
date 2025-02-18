# 1. 推荐写法

```shell
python -u main.py |& tee log.txt 2>&1
```

# 2. 更多说明

```text
tee命令
python main.py | tee log.txt
但是当输出量很大的时候，你会发现终端也没输出，log里也没输出，这是因为它会先在缓冲区里存，一定时间再刷新，这样输出的log或终端的输出可能就不是很及时了，可以使用下面

python -u main.py | tee log.txt
python命令加上-u（unbuffered）参数后会强制其标准输出也同标准错误一样不通过缓存直接打印到屏幕

-a 是append，即不覆盖而是追加内容

但是这样，程序的报错信息不会保存到文件中

这样写

python -u main.py |& tee log.txt 2>&1
|& 是 2>&1 | 的简写

script
先输入script，就会将后面所有linux的输出全部记录到日志文件中

script myfile
直到输入exit退出
```

# 参考
[1] linux终端屏幕输出的同时输出到log日志文件(tee)(script)，https://blog.csdn.net/hxxjxw/article/details/119008969