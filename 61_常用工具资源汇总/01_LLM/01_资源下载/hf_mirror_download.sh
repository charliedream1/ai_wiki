export HF_HOME="G:/data_tmp"  # 配置缓存路径，否则默认使用home目录或C盘(windows下)可能导致空间不足
export HF_ENDPOINT=https://hf-mirror.com  # 配置镜像源网站
# 如果下载模型，则删除--repo-type dataset
# --local-dir-use-symlinks False 是不适用软链接，否则下载的文件会软链接链接
# --local-dir G:/data 下载的本地路径
# Tele-AI/TeleChat-PTD 为hf-mirror.com网址中待下载的数据集的下载名称
huggingface-cli download --repo-type dataset  --resume-download --local-dir-use-symlinks False Tele-AI/TeleChat-PTD --local-dir G:/data