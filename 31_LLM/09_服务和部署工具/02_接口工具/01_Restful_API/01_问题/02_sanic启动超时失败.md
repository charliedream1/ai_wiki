分析：
- 首先，检查是否是代码内部存在问题，导致无法即时启动
- 如果不是代码问题，考虑加长超时时间

When all of your workers are running in a subprocess a potential problem is created: deadlock. This can occur when the child processes cease to function, but the main process is unaware that this happened. Therefore, Sanic servers will automatically send an ack message (short for acknowledge) to the main process after startup.

In version 22.9, the ack timeout was short and limited to 5s. In version 22.12, the timeout was lengthened to 30s. If your application is shutting down after thirty seconds then it might be necessary to manually increase this threshhold.

The value of WorkerManager.THRESHOLD is in 0.1s increments. Therefore, to set it to one minute, you should set the value to 600.

This value should be set as early as possible in your application, and should ideally happen in the global scope. Setting it after the main process has started will not work.

```python
from sanic.worker.manager import WorkerManager

WorkerManager.THRESHOLD = 600
```

# 参考

[1] https://sanic.dev/en/guide/running/manager.html#worker-ack