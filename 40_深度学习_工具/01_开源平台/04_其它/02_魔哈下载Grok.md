# 1. 命令行下载

1. 安装包

    ```bash
    pip install -U huggingface_hub
    pip install -U "huggingface_hub[cli]"
    ```

2. 设置环境变量
    
   Linux

   ```bash
    # 指定下载网址
    export HF_ENDPOINT=https://moha.xiaoshiai.cn/huggingface
    # 指定下载路径
    export HF_HOME=/home/username/.cache/huggingface
    ```
   
    windows Powershell设置 （未测试）
   
    ```bash
    $env:HF_ENDPOINT = "https://hf-mirror.com"  # 暂时不知如何使用
    ```
   
3. 下载

    ```bash
    
    
    huggingface-cli download xai-org/grok-1
    ```

# 参考

[1] huggingface-cli下载数据（含国内镜像源方法）, https://blog.csdn.net/lanlinjnc/article/details/136709225
[2] https://wenku.csdn.net/answer/6m662bcknj