内容来源：腾讯元宝

---

要使用这个 Docker 镜像（来自阿里云 ModelScope 官方镜像仓库），你需要先 **拉取（pull）** 镜像到本地，然后才能运行它。以下是详细步骤：

---

## **1. 拉取 Docker 镜像**
使用 `docker pull` 命令从阿里云 ModelScope 镜像仓库下载镜像：
```bash
docker pull modelscope-registry.cn-beijing.cr.aliyuncs.com/modelscope-repo/modelscope:ubuntu22.04-cuda12.4.0-py310-torch2.6.0-vllm0.8.5.post1-modelscope1.27.1-swift3.5.3
```
**说明：**
- `docker pull` 是 Docker 的拉取镜像命令。
- 镜像地址格式为：`<镜像仓库地址>/<镜像仓库名>/<镜像名>:<标签>`。
- 这里 `ubuntu22.04-cuda12.4.0-py310-torch2.6.0-vllm0.8.5.post1-modelscope1.27.1-swift3.5.3` 是镜像的 **标签（tag）**，表示该镜像基于 Ubuntu 22.04、CUDA 12.4.0、Python 3.10、PyTorch 2.6.0 等环境构建。

---

## **2. 检查镜像是否拉取成功**
拉取完成后，可以用 `docker images` 查看本地是否已有该镜像：
```bash
docker images
```
输出示例：
```
REPOSITORY                                                                 TAG                                                                 IMAGE ID       CREATED         SIZE
modelscope-registry.cn-beijing.cr.aliyuncs.com/modelscope-repo/modelscope  ubuntu22.04-cuda12.4.0-py310-torch2.6.0-vllm0.8.5.post1-modelscope1.27.1-swift3.5.3  abc123def456   2 hours ago     10GB
```
如果看到该镜像，说明拉取成功。

---

## **3. 运行 Docker 镜像**
拉取成功后，你可以使用 `docker run` 运行该镜像：
```bash
docker run -it --gpus all modelscope-registry.cn-beijing.cr.aliyuncs.com/modelscope-repo/modelscope:ubuntu22.04-cuda12.4.0-py310-torch2.6.0-vllm0.8.5.post1-modelscope1.27.1-swift3.5.3 /bin/bash
```
**参数说明：**
- `-it`：以交互模式运行（进入容器的终端）。
- `--gpus all`：分配所有可用的 GPU（如果你的系统支持 CUDA 并安装了 NVIDIA Docker 驱动）。
- `/bin/bash`：进入容器的 Bash shell（也可以换成其他命令，如 `/bin/sh` 或直接运行 Python 脚本）。

**如果没有 GPU 或不需要 GPU：**
```bash
docker run -it modelscope-registry.cn-beijing.cr.aliyuncs.com/modelscope-repo/modelscope:ubuntu22.04-cuda12.4.0-py310-torch2.6.0-vllm0.8.5.post1-modelscope1.27.1-swift3.5.3 /bin/bash
```

---

## **4. 如果拉取失败（可能的原因及解决方法）**
### **(1) 镜像地址错误**
确保镜像地址正确，特别是：
- 仓库地址：`modelscope-registry.cn-beijing.cr.aliyuncs.com`
- 仓库名：`modelscope-repo`
- 镜像名：`modelscope`
- 标签：`ubuntu22.04-cuda12.4.0-py310-torch2.6.0-vllm0.8.5.post1-modelscope1.27.1-swift3.5.3`

### **(2) 网络问题（无法访问阿里云镜像仓库）**
- 检查网络是否正常，能否访问 `https://modelscope-registry.cn-beijing.cr.aliyuncs.com`。
- 如果在国内，可能需要配置 Docker 的镜像加速器（阿里云提供免费加速服务）：
  1. 登录 https://cr.console.aliyun.com/。
  2. 获取你的 **加速器地址**（如 `https://<your-id>.mirror.aliyuncs.com`）。
  3. 修改 Docker 配置：
     ```bash
     sudo mkdir -p /etc/docker
     sudo tee /etc/docker/daemon.json <<-'EOF'
     {
       "registry-mirrors": ["https://<your-id>.mirror.aliyuncs.com"]
     }
     EOF
     ```
  4. 重启 Docker：
     ```bash
     sudo systemctl restart docker
     ```
  5. 再次尝试拉取镜像。

### **(3) 镜像不存在或标签错误**
- 检查镜像是否存在：访问 https://modelscope.cn/ 或联系 ModelScope 官方确认。
- 确保标签正确（如 `ubuntu22.04-cuda12.4.0-py310-torch2.6.0-vllm0.8.5.post1-modelscope1.27.1-swift3.5.3` 是否拼写正确）。

---

## **5. 其他常用 Docker 命令**
| 命令 | 用途 |
|------|------|
| `docker pull <镜像地址>` | 拉取镜像 |
| `docker images` | 查看本地镜像 |
| `docker run -it <镜像地址> /bin/bash` | 运行镜像并进入交互终端 |
| `docker ps` | 查看正在运行的容器 |
| `docker stop <容器ID>` | 停止容器 |
| `docker rm <容器ID>` | 删除容器 |
| `docker rmi <镜像ID>` | 删除镜像 |

---

## **总结**
1. **拉取镜像**：
   ```bash
   docker pull modelscope-registry.cn-beijing.cr.aliyuncs.com/modelscope-repo/modelscope:ubuntu22.04-cuda12.4.0-py310-torch2.6.0-vllm0.8.5.post1-modelscope1.27.1-swift3.5.3
   ```
2. **检查镜像**：
   ```bash
   docker images
   ```
3. **运行镜像**：
   ```bash
   docker run -it --gpus all <镜像地址> /bin/bash
   ```
4. **如果拉取失败**：
   - 检查网络、镜像地址、标签是否正确。
   - 配置阿里云镜像加速器（国内推荐）。

如果仍有问题，可以提供具体的错误信息，我可以帮你进一步排查！ 🚀