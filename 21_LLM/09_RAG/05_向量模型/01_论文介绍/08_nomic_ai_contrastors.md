1. nomic
   - Github (361 stars): https://github.com/nomic-ai/contrastors
   - 代码、数据、模型全量开放，以英文为主
   - 数据下载方法：
     - 1.注册账户：atlas.nomic.ai
     - 2.安装python客户端 (注意：nomic login会给出网址，点击后，获取api token，然后输入nomic login --token=token)
       - ```bash
         pip install nomic
         nomic login # follow prompts to login
         python -c "from nomic import atlas; print(atlas._get_datastream_credentials(name='contrastors'))"
         ```
     - 获取AWS的登录密钥（数据存储在亚马逊AWS服务上）：通过上述步骤可获取AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY
     - 安装amazon aws (数据存放在该s3桶上):
       - AWS官方使用文档：https://docs.aws.amazon.com/zh_cn/cli/latest/userguide/getting-started-quickstart.html
       - windows安装方法直接安装msi包，linux安装方法如下：
         - ```bash
           curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
           unzip awscliv2.zip
           sudo ./aws/install
           ```
     - 验证是否安装成功（linux和windows都可以在命令行下操作）：
       - ```bash
         aws --version
         ```
     - 配置aws
       - aws configure：（命令行输出如下提示，可以配置，之后就可以了）
       - ```bash 
          AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
          AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
          Default region name [None]: us-west-2
          Default output format [None]: json
         ```
     - 查看数据
       - ```bash
         aws s3 ls --endpoint-url=https://9fa58365a1a3d032127970d0bd9a1290.r2.cloudflarestorage.com/ s3://contrastive
         aws s3 ls --endpoint-url=https://9fa58365a1a3d032127970d0bd9a1290.r2.cloudflarestorage.com/ s3://contrastive-index-filtered
         ```
     - 下载数据
       - 单个数据文件夹 （如果不加--recursive，会报错）
         - ```bash
           aws s3 cp --endpoint-url=https://9fa58365a1a3d032127970d0bd9a1290.r2.cloudflarestorage.com/ s3://contrastive-index-filtered/contrastive-index-filtered-000000000000.jsonl . --recursive
           ```
       - 整个s3桶下载
         - ```bash
           aws s3 sync --endpoint-url=https://9fa58365a1a3d032127970d0bd9a1290.r2.cloudflarestorage.com/ s3://contrastive . 
           ```