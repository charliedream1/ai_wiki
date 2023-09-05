# 1. 简介

在内存不够大时，需要开启Swap，使用一部分硬盘，作为虚拟内存，解决内存容量不足的情况。

# 2. 配置
## 2.1 确定当前没有开启 Swap

```shell
free -m
```

```
total              used       free     shared    buffers     cached
Mem:               1840       1614     226       15          36       1340
-/+ buffers/cache:            238      1602
Swap:              0          0        0
```

最后一行是0 0 0，则表示当前没有开启。

## 2.2 创建 Swap 文件

使用下面命令创建交换文件。因为要分配硬盘空间，所以有可能比较慢，等待一会

```shell
dd if=/dev/zero of=/swapfile count=2048 bs=1M
```

count=1024*2 表示创建 2G 的虚拟内存，因为这里用到的单位是 M

使用命令查看一下，确保交换文件存在，创建成功。

```
ls / | grep swapfile
```

## 2.3 激活 Swap 文件

```shell
chmod 600 /swapfile
mkswap /swapfile
```

依次运行上面两个命令后，如果成功，将会看到类似下面的输出

```
Setting up swapspace version 1, size = 2097148 KiB
no label, UUID=ff3fc469-9c4b-4913-b653-ec53d6460d0e
```

## 2.4 开启 Swap

```shell
swapon /swapfile
```

查看是否成功开启
```
free -m
```

如果成功开启，最后一行 Swap 将不再是0 0 0，而是我们上面设置的大小。

```
total       used       free     shared    buffers     cached
Mem:          1840       1754         86         16         23       1519
-/+ buffers/cache:        210       1630
Swap:         2047          0       2047
```

## 2.5 设置系统启动时自动开启 Swap

使用编辑器编辑 /etc/fstab 文件，添加 Swap 自动开启的配置

```shell
vim /etc/fstab
```

在 fstab 文件最后一行添加下面的内容

```
/swapfile none swap sw 0 0
```

然后保存，退出。

好了，现在 Swap 已经配置完，并且可以在系统启动时自动开启。

# 参考
[1] （实测有效）在Ubuntu上开启Swap，https://zhuanlan.zhihu.com/p/106327686
[2] （强烈推荐，非常详细）How To Add Swap Space on Ubuntu 20.04，https://www.digitalocean.com/community/tutorials/how-to-add-swap-space-on-ubuntu-20-04