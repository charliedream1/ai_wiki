获取AWS的登录密钥（数据存储在亚马逊AWS服务上）：通过上述步骤可获取AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY
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
- 查看文件大小
  - ```bash
    aws s3 ls --summarize --human-readable --recursive s3://bucket/folder/*
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

下载命令
```bash
我下载AOI_4shanghai的，先获取
aws s3 ls s3://spacenet-dataset/AOIs/AOI_4_Shanghai/ --request-payer requester
 
下载数据示例
aws s3 cp s3://spacenet-dataset/AOIs/AOI_4_Shanghai . --recursive
 
aws s3 cp s3://arn:aws:s3:us-east-1:604877620213:accesspoint/dfdc-data-ap-1/test/metadata.json . --request-payer --region=us-east-1
 
aws s3 sync s3://livecell-dataset/ .
 
 
比如下载到D盘
aws s3 cp s3://spacenet-dataset/AOIs/AOI_4_Shanghai d:\ 
```

使用如下命令时，必须使用-recursive，否则会报错
```bash
aws s3 cp s3://<src-key>/ <dest-local> --recursive
```

cp表示复制，  src-key表示s3上的key（路径），<dest-local>是本地文件夹路径， --recursive表示路径下全部内容都下载，如果没有这个，可能会报错

An error occurred (404) when calling the HeadObject operation

如果一切正常，那么就会完成下载，国内访问外网速度还是可以的，2M左右的速度

# 参考

[1] 新手AWS S3下载数据集必学入门教程，https://blog.csdn.net/qq_41397220/article/details/133308580
[2] 用aws cli 下载s3中数据到本地，https://www.cnblogs.com/xuanmanstein/p/9603369.html
