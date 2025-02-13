再按照lightRAG等包后，可能导致调用chromadb等向量库时出现和hnswlib库冲突的问题，解决方案如下：

```bash
pip uninstall hnswlib chroma-hnswlib && pip install chroma-hnswlib
```

这个issue见：[this issue](https://github.com/Cinnamon/kotaemon/issues/440)
