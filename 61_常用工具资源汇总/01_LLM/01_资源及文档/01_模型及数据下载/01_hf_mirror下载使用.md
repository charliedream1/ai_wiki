# 介绍

此网站是hugging-face镜像站 （包含大部分常见模型和数据集）：

https://hf-mirror.com

除了需要导入网站地址外，其它所有使用和huggingface下载方法一致。

实测可用，但有时下载会中断

# 使用

## 1.1 直接在网页下载

在浏览器中打开网站，找到需要的模型或数据集，点击下载即可。

## 1.2 使用代码下载

1. 安装依赖
    
   ```bash
   export HF_ENDPOINT=https://hf-mirror.com
   ```

2. 设置环境变量
    Linux
    ```bash
     export HF_ENDPOINT=https://hf-mirror.com
    ```

    Windows Powershell
    ```bash
    $env:HF_ENDPOINT = "https://hf-mirror.com"
    ```
    
    建议将上面这一行写入 ~/.bashrc。

3. 下载模型
   ```bash
   huggingface-cli download --resume-download THUDM/chatglm-6b --local-dir model
   ```

4. 下载数据集

    ```bash
    huggingface-cli download --repo-type dataset --resume-download wikitext --local-dir wikitext
    ```

   可以添加 --local-dir-use-symlinks False 参数禁用文件软链接，这样下载路径下所见即所得，详细解释请见上面提到的教程。
   
   ```bash
   huggingface-cli download --resume-download --local-dir-use-symlinks False bigscience/bloom-560m --local-dir bloom-560m
   ```

5. 使用Python

   在import huggingface库相关语句之前执行环境设置
   ```python
   import os
   os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
   from huggingface_hub import hf_hub_download
   ```

# 参考

[1] 国内如何下载huggingface模型、数据集，https://blog.csdn.net/tangsiqi130/article/details/136815313