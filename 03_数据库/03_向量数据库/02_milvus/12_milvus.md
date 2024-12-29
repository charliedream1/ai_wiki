# 1. 简介

- 文档：https://www.bookstack.cn/read/milvus-0.8/guides-get_started-install_milvus-gpu_milvus_docker.md
- Github (25.6k Stars): https://github.com/milvus-io/milvus

# 2. GPU版安装

![](.12_milvus_images/安装要求.png)

Milvus Docker 要求
- 在您的宿主机上 安装 Docker 19.03 或更高版本。
- 安装 NVIDIA driver 418 或更高版本。
- 安装 NVIDIA Docker。

## 2.1 确认 Docker 状态

确认 Docker daemon 正在运行：

```shell
docker info
```

如果无法正常打印 Docker 相关信息，请启动 Docker daemon.

```text
提示：
在 Linux 上，Docker 命令前面需加 sudo。若要在没有 sudo 情况下运行 
Docker 命令，请创建 docker 组并添加用户。更多详情，请参阅 Linux 安装后步骤。
```

## 2.2 拉取 Milvus 镜像

```shell
docker pull milvusdb/milvus:0.8.0-gpu-d041520-464400
```

注意：如果您在拉取镜像时速度过慢或一直失败，请参考操作常见问题中提供的解决办法。

## 2.3 下载并修改配置文件

```shell
# Create Milvus file
mkdir -p /home/$USER/milvus/conf
cd /home/$USER/milvus/conf
wget https://raw.githubusercontent.com/milvus-io/milvus/v0.8.0/core/conf/demo/server_config.yaml
wget https://raw.githubusercontent.com/milvus-io/milvus/v0.8.0/core/conf/demo/log_config.conf
```

注意：万一您遇到无法通过 wget 命令正常下载配置文件的情况，您也可以在 /home/$USER/milvus/conf 路径下创建 
server_config.yaml 和 log_config.conf 文件，然后复制粘贴 server config 文件 和 log config 文件的内容。

配置文件下载完成后，您需要将 server_config.yaml 中的 gpu_resource_config 部分的 enable 参数设置为 true

下载路径如下：
- https://github.com/milvus-io/milvus/blob/v0.8.0/core/conf/demo/server_config.yaml
- https://github.com/milvus-io/milvus/blob/v0.8.0/core/conf/demo/log_config.conf

## 2.4 启动 Milvus Docker 容器

```shell
# Start Milvus
docker run -d --name milvus_gpu --gpus all \
-p 19530:19530 \
-p 19121:19121 \
-p 9091:9091 \
-v /home/$USER/milvus/db:/var/lib/milvus/db \
-v /home/$USER/milvus/conf:/var/lib/milvus/conf \
-v /home/$USER/milvus/logs:/var/lib/milvus/logs \
-v /home/$USER/milvus/wal:/var/lib/milvus/wal \
milvusdb/milvus:0.8.0-gpu-d041520-464400
```

上述命令中用到的 docker run 参数定义如下：

- -d: 运行 container 到后台并打印 container id。
- --name: 为 container 分配一个名字。
- --gpus: 指定可用的 GPU。如未填写任何值，则所有 GPU 都可用。
- -p: 暴露 container 端口到 host。
- -v: 将路径挂载至 container。

## 2.5 验证 Milvus Docker 容器是否成功启动

```shell
# Confirm Milvus status
docker ps
```

如果 Milvus 服务没有正常启动，您可以执行以下命令查询错误日志。

```shell
# Get id of the container running Milvus
$ docker ps -a
# Check docker logs
$ docker logs <milvus container id>
```

# 参考

[1] Milvus 0.8 开源向量搜索引擎使用教程，https://www.bookstack.cn/read/milvus-0.8/guides-get_started-install_milvus-gpu_milvus_docker.md