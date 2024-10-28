在 Linux 下可以使用 `unzip` 命令解压带密码的 ZIP 文件。以下是具体命令格式：

```bash
unzip -P your_password file.zip
```

其中：
- `-P` 参数指定密码，可以替换 `your_password` 为 ZIP 文件的实际密码。
- `file.zip` 是需要解压的 ZIP 文件的路径。

### 例子
假设 ZIP 文件名是 `archive.zip`，密码是 `12345`，可以使用以下命令：

```bash
unzip -P 12345 archive.zip
```

### 其他解压工具
如果 `unzip` 不适用，可以试试 `7z`（7-Zip 命令行工具）来解压带密码的 ZIP 文件：

```bash
7z x file.zip -p12345
```

在这个命令中，`x` 参数表示解压操作，`-p12345` 指定密码。

****

# 执行上面后报错

报这个错：Archive:  tmp.zip
   skipping: tmp.txt                 need PK compat. v5.1 (can do v4.6)

### 解决方法

出现“`need PK compat. v5.1 (can do v4.6)`”的错误，是因为 ZIP 文件使用的压缩方式（PKZIP 5.1）不受 `unzip` 工具的支持。可以尝试以下方法来解压这种 ZIP 文件格式：

### 方法 1：使用 `7z` 工具
`7z` 工具（7-Zip）支持更多的压缩格式，可能可以解压该文件。若未安装 `7z`，可以通过以下命令安装：

```bash
# Ubuntu 或 Debian 系列
sudo apt update
sudo apt install p7zip-full

# CentOS 或 RHEL 系列
sudo yum install p7zip
```

然后解压 ZIP 文件：

```bash
7z x tmp.zip -pYOUR_PASSWORD
```

### 方法 2：使用 `unar`
`unar` 是另一个解压工具，支持多种压缩格式。如果安装了 `unar`，可以直接使用以下命令来解压文件：

```bash
# 安装 unar (在 Ubuntu/Debian 系列系统)
sudo apt install unar

# 解压文件
unar -p YOUR_PASSWORD tmp.zip
```

### 方法 3：使用 Python 脚本
如果上述工具无法解压，可以编写 Python 脚本，借助 `zipfile` 模块进行解压：

```python
import zipfile

with zipfile.ZipFile("tmp.zip", "r") as zip_ref:
    zip_ref.extractall(pwd=b"YOUR_PASSWORD")
```

请将 `"YOUR_PASSWORD"` 替换为实际密码。