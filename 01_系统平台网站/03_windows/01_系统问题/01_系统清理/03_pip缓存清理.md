直接用这条命令就能一键清空 pip 的缓存：

```
pip cache purge
```

---

### 💡 附带几个超实用的 pip 缓存管理技巧：

**1. 查看缓存占用了多大空间及存放位置**

想知道你的 pip 到底缓存了多少东西，或者它把文件藏在哪了，可以运行：

```
pip cache info
```

**2. 如果不想让它产生缓存（临时一次性）**

如果你只是临时装一个包，不想让它留下缓存垃圾，可以在安装时加上 `--no-cache-dir`参数：

```
pip install 包名 --no-cache-dir
```

**3. 永久修改缓存路径（C盘救星）**

如果你用的是 Windows 且 C 盘空间告急，每次用 `purge`清缓存太麻烦，可以一劳永逸地把 pip 的缓存文件夹“搬”到其它盘（比如 D 盘）：

* **Windows 系统**：

  在 `D:`盘新建一个文件夹（如 `D:\pip_cache`）。

  然后按下 `Win + R`键，输入 `sysdm.cpl`回车打开“系统属性” -> 点“高级” -> 点“环境变量”。

  在“用户变量”或“系统变量”里点击“新建”，变量名填 `PIP_CACHE_DIR`，变量值填 `D:\pip_cache`。

  重启终端后，以后所有的 pip 缓存就会自动存到 D 盘了。
* **Linux / macOS 系统**：

  直接在终端编辑 `~/.bashrc`或 `~/.zshrc`，在末尾添加：

  ```
  export PIP_CACHE_DIR="/path/to/your/custom/cache"
  ```
  *(将 `/path/to/your/custom/cache`替换为你想存放的绝对路径，比如 `/home/user/pip_cache`)*

  保存后执行 `source ~/.bashrc`即可生效。
