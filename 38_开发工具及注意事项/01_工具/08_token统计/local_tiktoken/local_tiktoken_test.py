import os

# 把路径换成你刚才放文件的真实路径
os.environ["TIKTOKEN_CACHE_DIR"] = "/opt/tiktoken_offline_cache/"

# 现在可以放心导入了
import tiktoken

# 随便测一下，不会再报联网的错误了
enc = tiktoken.get_encoding("cl100k_base")
print(f"离线测试成功！编码结果：{enc.encode('Hello Offline World!')}")