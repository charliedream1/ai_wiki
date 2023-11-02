问题：Error loading wikitext data raise NotImplementedError(f"Loading 
     a dataset cached in a {type(self._fs).name} is not supported.")

```markdown
I was trying to load the wiki dataset, but i got this error
 
traindata = load_dataset('wikitext', 'wikitext-2-raw-v1', split='train')
File "/home/aelkordy/.conda/envs/prune_llm/lib/python3.9/site-packages/datasets/load.py", line 1804, in load_dataset
ds = builder_instance.as_dataset(split=split, verification_mode=verification_mode, in_memory=keep_in_memory)
File "/home/aelkordy/.conda/envs/prune_llm/lib/python3.9/site-packages/datasets/builder.py", line 1108, in as_dataset
raise NotImplementedError(f"Loading a dataset cached in a {type(self._fs).name} is not supported.")
NotImplementedError: Loading a dataset cached in a LocalFileSystem is not supported.
```

方法：升级

```shell
pip install -U datasets
```

# 参考
[1] Error loading wikitext data raise NotImplementedError
    (f"Loading a dataset cached in a {type(self._fs).name} is not supported.")，
    https://www.cnblogs.com/michaelcjl/p/17803604.html#:~:text=NotImplementedError%3A%20Loading%20a%20dataset%20cached%20in%20a%20LocalFileSystem,pip%20install%20-U%20datasets%20should%20fix%20the%20issue.