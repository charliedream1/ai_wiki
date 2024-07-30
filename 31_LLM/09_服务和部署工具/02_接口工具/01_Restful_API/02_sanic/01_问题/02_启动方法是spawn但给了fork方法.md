# 问题

RuntimeError: Start method 'spawn' was requested, but 'fork' was already set.

# 原因

参考：https://sanic.dev/en/guide/running/manager.html#overcoming-a-coderuntimeerrorcode

If so, that means somewhere in your application you are trying to set the start method that conflicts with what Sanic is trying to do. You have a few options to resolve this:

# 解决

参考：https://sanic.dev/en/guide/running/manager.html#overcoming-a-coderuntimeerrorcode

实测完成option1和option2的方法，可以解决问题。


OPTION 1: You can tell Sanic that the start method has been set and to not try and set it again.

```python
from sanic import Sanic

Sanic.START_METHOD_SET = True
```

OPTION 2: You could tell Sanic that you intend to use fork and to not try and set it to spawn.

```python
from sanic import Sanic

Sanic.start_method = "fork"
```

OPTION 3: You can tell Python to use spawn instead of fork by setting the multiprocessing start method.

```python
import multiprocessing

multiprocessing.set_start_method("spawn")
```

In any of these options, you should run this code as early as possible in your application. Depending upon exactly what your specific scenario is, you may need to combine some of the options.

Note

The potential issues that arise from this problem are usually easily solved by just allowing Sanic to be in charge of multiprocessing. This usually means making use of the main_process_start and main_process_ready listeners to deal with multiprocessing issues. For example, you should move instantiating multiprocessing primitives that do a lot of work under the hood from the global scope and into a listener.

```python
# This is BAD; avoid the global scope
from multiprocessing import Queue

q = Queue()
```

```python
# This is GOOD; the queue is made in a listener and shared to all the processes on the shared_ctx
from multiprocessing import Queue

@app.main_process_start
async def main_process_start(app):
    app.shared_ctx.q = Queue()
```