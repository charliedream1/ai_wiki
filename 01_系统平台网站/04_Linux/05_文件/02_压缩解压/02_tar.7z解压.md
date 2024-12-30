在 Ubuntu 中，解压 `.tar.7z` 文件可以通过以下步骤完成：

### 1. 安装必要的软件
确保安装了 `p7zip-full` 和 `tar`，可以通过以下命令进行安装：

```bash
sudo apt update
sudo apt install p7zip-full
```

### 2. 解压 `.tar.7z` 文件
假设你的文件名为 `example.tar.7z`，可以使用以下命令进行解压：

```bash
# 解压 .tar.7z 文件
7z x example.tar.7z
```

此命令会提取出一个 `example.tar` 文件。

### 3. 解压 `.tar` 文件
接下来使用 `tar` 命令解压得到的 `.tar` 文件：

```bash
tar -xf example.tar
```

### 总结
以上步骤将 `example.tar.7z` 文件解压到当前目录。如果需要将文件解压到特定目录，可以在 `tar` 命令中添加 `-C` 选项指定目标路径，例如：

```bash
tar -xf example.tar -C /path/to/directory
```

这样就可以将解压后的文件放入指定目录中。
