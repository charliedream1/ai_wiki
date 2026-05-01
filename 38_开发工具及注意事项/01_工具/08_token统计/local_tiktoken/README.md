**完全可以离线使用！** 

`tiktoken` 之所以在无网环境报错，是因为它在首次调用时会“悄悄”去 OpenAI 的服务器下载对应的词汇表文件（`.tiktoken`）。只要我们在有网环境提前把这些文件“备好”，然后告诉 `tiktoken` 去哪里找，它就能完美工作在离线模式下。

以下是为你整理的**零基础离线部署方案**，只需两步：

### 第一步：在有网络的机器上“备货”

你需要提前拿到对应的词汇表文件。这里提供两种方法：

**方法 A：一键触发自动下载（最省心，推荐）**
在你个人电脑（能上网）的 Python 环境里运行以下几行代码。`tiktoken` 会乖乖把文件下载到它的默认缓存文件夹里（通常在用户目录下的 `.cache/tiktoken/`）。
```python
import tiktoken
# 把你离线环境里可能用到的模型都在这提前“预热”一下
tiktoken.get_encoding("cl100k_base")   # GPT-4, GPT-3.5-Turbo, Embedding 等常用
tiktoken.get_encoding("o200k_base")   # GPT-4o, GPT-4o-mini 等常用
```
运行完别关，我们接着用代码帮它们“改个名”（`tiktoken` 底层是靠网址算出来的哈希值当文件名的）：
```python
import os
import hashlib

# 这两行是用来生成 tiktoken 内部真正的缓存文件名的
def get_cache_filename(encoding_name):
    # tiktoken 内部的固定逻辑
    blobpath = f"https://openaipublic.blob.core.windows.net/encodings/{encoding_name}.tiktoken"
    cache_key = hashlib.sha1(blobpath.encode()).hexdigest()
    return cache_key

names = ["cl100k_base", "o200k_base"]
for name in names:
    print(f"{name} 对应的缓存文件名为: {get_cache_filename(name)}")
```
*运行后你会得到类似 `9b5ad71b2ce5302211f9c61530b329a4922fc6a4` 这样的字符串，这就是它在缓存文件夹里的真名。*

**方法 B：手动下载并重命名（硬核直连）**
如果你不想敲代码，也可以直接用浏览器或下载工具访问以下链接下载，然后手动重命名：
*   **cl100k_base**: 
    *   下载链接：https://openaipublic.blob.core.windows.net/encodings/cl100k_base.tiktoken
    *   重命名为：`9b5ad71b2ce5302211f9c61530b329a4922fc6a4`
*   **o200k_base**: 
    *   下载链接：https://openaipublic.blob.core.windows.net/encodings/o200k_base.tiktoken
    *   重命名为：`fb374d419588a4632f3f557e76b4b70aebbca790`

### 第二步：在离线机器上“安家”

1. **放置文件**：把你准备好的这几个无后缀的哈希文件，上传到离线服务器的任意一个目录，比如 `/opt/tiktoken_offline_cache/`。
2. **设置环境变量**：在你的 Python 代码**最开头**（`import tiktoken` 之前），指一下路即可：

```python
import os

# 把路径换成你刚才放文件的真实路径
os.environ["TIKTOKEN_CACHE_DIR"] = "/opt/tiktoken_offline_cache/"

# 现在可以放心导入了
import tiktoken

# 随便测一下，不会再报联网的错误了
enc = tiktoken.get_encoding("cl100k_base")
print(f"离线测试成功！编码结果：{enc.encode('Hello Offline World!')}")
```

### 💡 避坑指南
*   **顺序不能乱**：一定要先设置 `TIKTOKEN_CACHE_DIR` 环境变量，再 `import tiktoken`，否则它可能已经去尝试联网并报错了。
*   **文件名要对**：如果运行时报错说找不到文件，大概率是文件名没对应上。你可以故意让它联一次网（如果临时有网的话）让它自己生成，或者仔细检查文件名是否完整（比如有没有不小心加了 `.txt` 后缀）。

按这个流程走，你的项目就算部署在拔了网线的内网服务器或者严苛的 Docker 容器里，也能顺滑地跑起来！