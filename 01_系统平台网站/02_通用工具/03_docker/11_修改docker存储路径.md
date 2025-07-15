**来自腾讯元宝**

---

在 Ubuntu 系统中，若需为 Docker 指定新的存储路径以解决系统盘空间不足的问题，可通过以下步骤实现（支持 Docker 17.05+ 版本）：

---

### **方法一：通过 `daemon.json` 直接修改存储路径（推荐）**
#### 1. **停止 Docker 服务**
```bash
sudo systemctl stop docker
```

#### 2. **创建新存储目录**
选择剩余空间充足的分区（如 `/mnt/data`）：
```bash
sudo mkdir -p /mnt/data/docker
sudo chmod 755 /mnt/data/docker
```

#### 3. **修改配置文件**
编辑 `/etc/docker/daemon.json`（若不存在则创建）：
```bash
sudo nano /etc/docker/daemon.json
```
添加以下内容（指定新路径）：
```json
{
  "data-root": "/mnt/data/docker"
}
```

#### 4. **重启 Docker 服务**
```bash
sudo systemctl daemon-reload
sudo systemctl start docker
```

#### 5. **验证路径修改**
```bash
docker info | grep "Docker Root Dir"
# 输出示例：Docker Root Dir: /mnt/data/docker
```

---

### **方法二：迁移现有数据到新路径（适用于已有数据）**
#### 1. **停止 Docker 服务**
```bash
sudo systemctl stop docker
```

#### 2. **复制现有数据**
使用 `rsync` 保留权限和元数据：
```bash
sudo rsync -aP /var/lib/docker/ /mnt/data/docker/
```

#### 3. **修改配置文件**
同方法一的步骤 3-5。

#### 4. **清理旧数据（可选）**
确认新路径正常后，可删除原数据释放空间：
```bash
sudo rm -rf /var/lib/docker
```

---

### **方法三：通过 systemd 服务参数覆盖（兼容旧版本）**
#### 1. **创建 systemd 配置文件**
```bash
sudo mkdir -p /etc/systemd/system/docker.service.d
sudo nano /etc/systemd/system/docker.service.d/docker.conf
```

#### 2. **添加存储路径参数**
```ini
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd --graph=/mnt/data/docker
```

#### 3. **重启服务**
```bash
sudo systemctl daemon-reload
sudo systemctl restart docker
```

---

### **关键注意事项**
1. **存储空间要求**  
   - 新路径所在分区需有 **至少 20GB 可用空间**（镜像层、容器、缓存等均占用空间）。
   - 若使用机械硬盘，建议预留 **2-3 倍镜像大小** 的缓冲空间。

2. **权限问题**  
   - 确保新目录的属主和属组为 `root:root`，权限为 `755`：
     ```bash
     sudo chown -R root:root /mnt/data/docker
     sudo chmod -R 755 /mnt/data/docker
     ```

3. **数据备份**  
   - 迁移前建议备份关键数据：
     ```bash
     sudo tar -czvf /backup/docker_backup.tar.gz /var/lib/docker
     ```

4. **存储驱动兼容性**  
   - 若使用 `overlay2` 存储驱动，需确保新路径的文件系统支持（如 ext4、XFS）。

---

### **扩展方案：挂载外部存储（如 NAS/移动硬盘）**
若本地磁盘空间不足，可将新路径挂载到外部存储：
```bash
# 假设外接硬盘挂载在 /mnt/external
sudo mount /dev/sdb1 /mnt/external
sudo ln -s /mnt/external/docker /mnt/data/docker  # 创建软链接
```

---

### **验证镜像拉取**
```bash
docker pull <镜像名称>:<标签>
docker images | grep <镜像名称>  # 确认镜像已下载到新路径
```

通过以上方法，可彻底解决 Docker 存储空间不足的问题。若需进一步优化存储，可结合镜像分层缓存、定期清理无用数据（`docker system prune`）等策略。