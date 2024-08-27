export HF_HOME="G:/data_tmp"  # 配置缓存路径，否则默认使用home目录或C盘(windows下)可能导致空间不足
export HF_ENDPOINT=https://hf-mirror.com  # 配置镜像源网站
huggingface-cli download --repo-type dataset  --resume-download --local-dir-use-symlinks False Tele-AI/TeleChat-PTD --local-dir G:/data