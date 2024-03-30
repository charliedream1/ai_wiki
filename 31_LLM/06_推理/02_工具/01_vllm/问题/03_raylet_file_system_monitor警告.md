# 问题

在使用 Ray 时，出现了如下警告：

```text
(raylet)file_system_monitor.cc:105: - “Object creation will fail if spilling is required”
OSError: [Errno 122] Disk quota exceeded: '/tmp/ray/session_2023-09-26_08-01-37_150792_36444/ray_spilled_objects/37bfa45c93374ac3b70fc230a50fcfa9-multi-587'                                               
An unexpected internal error occurred while the IO worker was spilling objects: [Errno 122] Disk quota exceeded: '/tmp/ray/session_2023-09-26_08-01-37_150792_36444/ray_spilled_objects/37bfa45c93374ac3b70
fc230a50fcfa9-multi-587'
```

问题描述：使用服务器进行ray训练，tmp文件夹对应的挂载硬盘空间较小导致运行中出现磁盘空间不足

看着任务还在跑，但一直结束不了

# 解决方案

空间不足导致

方案1：删除无用文件
方案2：
```python
ray.init(..., _temp_dir=your/path)
```

# 参考

[1] (raylet)file_system_monitor.cc:105: - “Object creation will fail if spilling is required”，https://discuss.ray.io/t/raylet-file-system-monitor-cc-object-creation-will-fail-if-spilling-is-required/7372