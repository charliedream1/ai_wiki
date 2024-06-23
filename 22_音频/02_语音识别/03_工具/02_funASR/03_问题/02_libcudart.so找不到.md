# 问题

torchaudio报错libcudart.so找不到

# 解决

发现conda环境中，torch的cuda版本和cudatoolkit版本不一致。卸载torch、torchaudio重新安装即可

# 参考

[1] OSError: libcudart.so.11.0: cannot open shared object file: No such file or directory，https://blog.csdn.net/zengNLP/article/details/135566503