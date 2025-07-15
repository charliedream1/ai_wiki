**来自腾讯元宝**

---

### **一、检查Ubuntu是否已安装Docker**  
要验证Ubuntu系统是否安装了Docker，可通过以下**3种常用方法**（优先推荐前两种）：  

#### 1. **检查Docker版本信息（最快捷）**  
在终端执行以下命令，若返回Docker版本号（如`Docker version 24.0.5, build 24.0.5-0ubuntu1~22.04.1`），则说明已安装；若提示`command not found`，则表示未安装。  
```bash
docker --version
```  

#### 2. **查看Docker详细信息**  
执行`docker info`命令，若返回Docker系统信息（如容器数量、镜像数量、存储驱动等），则说明已安装；若提示`Cannot connect to the Docker daemon`，则表示未安装或服务未启动。  
```bash
docker info
```  

#### 3. **运行测试容器（验证功能完整性）**  
执行`docker run hello-world`命令，若下载并运行测试镜像（输出`Hello from Docker!*`），则说明已安装且功能正常；若提示`command not found`，则表示未安装。  
```bash
docker run hello-world
```  


### **二、Ubuntu未安装Docker时的安装步骤**  
若未安装Docker，可通过**官方APT仓库**安装（推荐，版本最新且稳定），以下是详细步骤（基于Ubuntu 22.04/24.04，适用于64位系统）：  

#### **1. 更新系统包索引**  
首先更新系统的软件包列表，确保获取最新的Docker版本：  
```bash
sudo apt update
```  

#### **2. 安装必要依赖**  
安装Docker所需的依赖包（如APT传输协议、CA证书、curl等）：  
```bash
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
```  

#### **3. 添加Docker官方GPG密钥**  
为确保安装的Docker包来自官方来源，需添加Docker的GPG密钥（验证包的完整性）：  
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```  

#### **4. 添加Docker APT仓库**  
将Docker的官方仓库添加到Ubuntu的软件源列表中（选择稳定版`stable`，若需测试版可替换为`edge`）：  
```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```  

#### **5. 再次更新包索引**  
添加仓库后，需更新包索引以生效：  
```bash
sudo apt update
```  

#### **6. 安装Docker CE（社区版）**  
安装Docker的核心组件（`docker-ce`：容器引擎；`docker-ce-cli`：命令行工具；`containerd.io`：容器运行时）：  
```bash
sudo apt install -y docker-ce docker-ce-cli containerd.io
```  

#### **7. 启动并启用Docker服务**  
安装完成后，启动Docker服务并设置为开机自启：  
```bash
sudo systemctl start docker   # 启动服务
sudo systemctl enable docker  # 开机自启
```  

#### **8. 验证安装（可选但推荐）**  
执行以下命令验证Docker是否正常运行：  
```bash
docker --version   # 查看版本
docker info        # 查看系统信息
docker run hello-world  # 运行测试容器（输出"Hello from Docker!"表示成功）
```  


### **三、常见问题与解决方法**  
#### 1. **权限问题（非root用户无法运行Docker）**  
默认情况下，Docker命令需要`root`权限或`docker`组权限。若需以普通用户运行，可将当前用户添加到`docker`组：  
```bash
sudo usermod -aG docker $USER  # 将当前用户添加到docker组
newgrp docker                   # 立即生效（或注销后重新登录）
```  

#### 2. **安装失败（网络问题）**  
若因网络问题无法连接到Docker官方仓库，可使用**国内镜像源**（如阿里云）替换官方源：  
- 替换步骤：将步骤4中的`https://download.docker.com/linux/ubuntu`改为`http://mirrors.aliyun.com/docker-ce/linux/ubuntu`。  

#### 3. **旧版本Docker未卸载**  
若之前安装过旧版本Docker（如`docker.io`），需先卸载旧版本：  
```bash
sudo apt remove -y docker docker-engine docker.io containerd runc  # 卸载旧包
sudo rm -rf /var/lib/docker  # 删除旧数据（可选，会清除镜像、容器等）
```  


### **四、补充说明**  
- **Docker Desktop（可选）**：若需图形化界面，可安装Docker Desktop（要求RAM≥4G），但Ubuntu推荐使用命令行工具（更轻量）。  
- **存储路径修改（可选）**：若默认存储路径（`/var/lib/docker`）空间不足，可修改`/etc/docker/daemon.json`文件中的`data-root`字段（需重启Docker服务）。  


通过以上步骤，可在Ubuntu系统上快速检查并安装Docker。若遇到问题，可参考Docker官方文档（https://docs.docker.com/engine/install/ubuntu/）获取更多帮助。