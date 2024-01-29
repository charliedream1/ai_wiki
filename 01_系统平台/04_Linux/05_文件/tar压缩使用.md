# tar打包压缩

压缩和解压

```shell
tar -czvf xxx.tar.gz  source_file (tar -czvf 包名.tar.gz  源文件)        #以tar.gz方式打包并gz方式压缩
tar -xzvf xxx.tar.gz -C path (tar -xzvf xxx.tar.gz -C 目标路径)          #解压缩包
```

如果不压缩，仅打包解包，则去掉z(即czvf, xzvf中的z)

tar命令常用格式

```shell
[root@RedHat_test ~]# man tar
 -c新建打包文件，同 -v一起使用 查看过程中打包文件名
 -v压缩或解压过程中，显示过程
 -f要操作的文件名
 -r表示增加文件，把要增加的文件追加在压缩文件的末尾
 -t表示查看文件，查看文件中的文件内容
 -x解压文件
 -z通过gzip方式压缩或解压，最后以.tar.gz 为后缀
 -j通过bzip2方式压缩或解压，最后以.tar.br2 为后缀。压缩后大小小于.tar.gz
 -u更新压缩文件中的内容
 -p保留绝对路径，即允许备份数据中含有根目录
 -P保留数据原来权限及属性
```

# 参考

[1] tar 打包压缩命令，https://blog.csdn.net/MssGuo/article/details/117387213#:~:text=tar%20%E5%91%BD%E4%BB%A4%E7%94%A8%E4%BA%8E%E6%96%87%E4%BB%B6%E7%9A%84%E6%89%93%E5%8C%85%E6%88%96%E5%8E%8B%E7%BC%A9%EF%BC%8C%E6%98%AF%E6%9C%80%E4%B8%BA%E5%B8%B8%E7%94%A8%E7%9A%84%E6%89%93%E5%8C%85%E5%8E%8B%E7%BC%A9%E5%91%BD%E4%BB%A4%EF%BC%8C%E5%85%B6%E8%AF%AD%E6%B3%95%E6%A0%BC%E5%BC%8F%E5%A6%82%E4%B8%8B%EF%BC%9A%20tar%20%5B%E9%80%89%E9%A1%B9%5D%20%E6%96%87%E4%BB%B6%E5%90%8D.tar.gz%20%E6%BA%90%E6%96%87%E4%BB%B6%201%20tar,path%20%28tar%20-xzvf%20xxx.tar.gz%20-C%20%E7%9B%AE%E6%A0%87%E8%B7%AF%E5%BE%84%29%20%23%E8%A7%A3%E5%8E%8B%E7%BC%A9%E5%8C%85%201