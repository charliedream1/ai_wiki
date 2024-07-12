参考：
- https://github.com/TencentARC/InstantMesh/issues/116
- cannot import name 'split_torch_state_dict_into_shards' from 'huggingface_hub' #116

解决方法

```bash
pip install --upgrade huggingface_hub
```