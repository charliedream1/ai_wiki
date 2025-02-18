# 问题

挂载盘无法访问，报错`Stale NFS file handle`。强行卸载挂载盘后，重新挂载，仍然无法访问，还报同样的错误

# 原因

有的时候，NFS Client已经mount上的文件或者目录，在NFS Server上突然被remove或者unexport，就会出现这样的信息。例如NFS Client端mount上了NFS Server端的目录后，如果NFS Server端把这个目录进行了unshare。就会在NFS Client端出现这个错误。

# 解决方法

在服务端，重启服务

```bash
service nfs-kernel-server restart
```

# 参考

[1] NFS故障：Stale NFS file handle的解决一例，https://blog.csdn.net/mcwolf/article/details/110921604
