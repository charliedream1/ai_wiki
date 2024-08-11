# 1. asyncio使用

如下代码和解释来自GPT4o-mini，于20240810测试，验证代码正确。

## 1.1 基础使用

在Python中，`asyncio.gather` 是一个非常有用的函数，它可以并发地运行多个协程，并将它们的结果一起返回。使用 `asyncio.gather` 后，你会得到一个包含所有协程返回值的列表。下面是如何使用 `asyncio.gather` 并获取返回值的基本示例：

```python
import asyncio

async def fetch_data(num):
    # 模拟一个异步操作，比如从网络获取数据
    await asyncio.sleep(1)
    return f"Data {num}"

async def main():
    # 使用 asyncio.gather 并发运行多个协程
    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    )
    # results 将是一个包含所有协程返回值的列表
    print(results)

# 运行主函数
asyncio.run(main())
```

在这个例子中：

1. `fetch_data` 是一个模拟的异步函数，它接受一个参数并在等待一段时间后返回一个字符串。
2. `main` 函数使用 `asyncio.gather` 来并发运行三个 `fetch_data` 协程。
3. `asyncio.gather` 返回一个包含所有协程返回值的列表，这个列表在 `results` 变量中。

运行这个代码，你会看到输出是：

```
['Data 1', 'Data 2', 'Data 3']
```

这说明 `asyncio.gather` 成功地并发地执行了三个协程，并将它们的返回值收集到一个列表中。

## 1.2 设置最大并发

为了将并发的最大数量限制为2，你可以使用一个信号量（`asyncio.Semaphore`）来控制并发任务的数量。下面是如何修改你的代码来实现这一点：

```python
import asyncio

# 创建一个信号量，设置最大并发数量为2
semaphore = asyncio.Semaphore(2)

async def fetch_data(num):
    async with semaphore:
        # 模拟一个异步操作，比如从网络获取数据
        await asyncio.sleep(1)
        return f"Data {num}"

async def main():
    # 使用 asyncio.gather 并发运行多个协程
    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    )
    # results 将是一个包含所有协程返回值的列表
    print(results)

# 运行主函数
asyncio.run(main())
```

### 代码解释

1. **信号量创建**：`semaphore = asyncio.Semaphore(2)` 创建一个信号量实例，设置最大并发数量为2。

2. **使用信号量**：在 `fetch_data` 协程内部，使用 `async with semaphore` 语句来确保同一时间只有最多两个协程可以进入临界区（即执行 `fetch_data` 函数的核心代码）。

### 运行结果

在这种配置下，当你运行这个代码时，会有两个协程同时执行，第三个协程会等到前面两个协程中的一个完成后才开始执行。由于 `fetch_data` 中有 `await asyncio.sleep(1)` 模拟的延迟，运行顺序可能会有所不同，但并发数量会被限制在2以内。

这样做可以有效地控制并发的数量，避免同时执行过多的协程而导致资源过载。

## 1.3 和Thread对比

同等并发数量情况下，比如并发为3，上述代码使用async实现，和使用多线程ThreadPoolExecutor，哪个速度更快？相对来说，使用async是否更有优势，还是效果一样？

`asyncio` 和 `ThreadPoolExecutor` 都可以用于并发任务的执行，但它们适用于不同的场景，并且有不同的性能特征。选择其中之一通常取决于任务的性质和所需的并发特性。下面是它们之间的主要区别及优缺点：

### 1. `asyncio`（异步编程）

**优点**：
- **轻量级**：`asyncio` 是基于事件循环的，它不依赖于线程或进程，因此在任务数量非常大的情况下，内存开销较小。
- **高效处理 I/O 密集型任务**：对于网络请求、文件操作等 I/O 密集型任务，异步编程可以有效地利用 CPU 空闲时间，达到高并发处理。
- **更少的上下文切换**：由于没有线程上下文切换的开销，异步编程在处理大量小任务时通常比线程更高效。

**缺点**：
- **对 CPU 密集型任务效果差**：如果任务主要是 CPU 密集型（例如复杂的计算），`asyncio` 并不会比多线程或多进程更有效，因为 Python 的全局解释器锁（GIL）限制了线程在 CPU 密集型任务中的并行性。
- **复杂的代码结构**：异步代码可能比同步代码更复杂，尤其是在错误处理和状态管理方面。

### 2. `ThreadPoolExecutor`（多线程）

**优点**：
- **适合 CPU 密集型任务**：`ThreadPoolExecutor` 可以并发地处理 CPU 密集型任务，特别是在使用 `concurrent.futures` 的线程池时，每个线程都可以在多个核心上并行执行。
- **简单的编程模型**：对于很多开发者来说，多线程的编程模型更直观，相对容易理解和实现。

**缺点**：
- **线程开销**：线程创建和上下文切换有一定的开销，尤其是线程数量很大的时候，这可能会影响性能。
- **全局解释器锁（GIL）**：Python 的 GIL 会影响多线程的效率，特别是在 CPU 密集型任务中。虽然 `ThreadPoolExecutor` 可以使用多个线程，但 GIL 仍然会限制线程并行执行 Python 代码的效果。

### 性能对比

- **对于 I/O 密集型任务**：`asyncio` 通常会比 `ThreadPoolExecutor` 更快，因为它通过协程和事件循环高效地处理大量的 I/O 操作，而不会受到线程上下文切换的开销。
  
- **对于 CPU 密集型任务**：`ThreadPoolExecutor` 可能会更快，因为它能够利用多个 CPU 核心进行计算，虽然 Python 的 GIL 可能限制并行执行的效果，但多线程在 CPU 密集型任务中通常仍能带来性能提升。另一个选择是使用 `ProcessPoolExecutor`，它通过多进程绕过 GIL 限制，但也会带来进程创建和上下文切换的开销。

### 示例对比

#### 使用 `asyncio` 的代码示例：

```python
import asyncio

async def task(num):
    await asyncio.sleep(1)
    return f"Result {num}"

async def main():
    results = await asyncio.gather(
        task(1),
        task(2),
        task(3)
    )
    print(results)

asyncio.run(main())
```

#### 使用 `ThreadPoolExecutor` 的代码示例：

```python
from concurrent.futures import ThreadPoolExecutor
import time

def task(num):
    time.sleep(1)
    return f"Result {num}"

def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(task, i) for i in range(1, 4)]
        results = [future.result() for future in futures]
    print(results)

if __name__ == "__main__":
    main()
```

另一个Thread样例

```python
from tqdm import tqdm
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

graph_document_list=[]
futures=[]
start_time = datetime.now()
with ThreadPoolExecutor(max_workers=8) as executor:
    
    for i,chunk in tqdm(enumerate(documents), total=len(documents)):
        futures.append(executor.submit(extract_and_store_graph,chunk))
    
    for future in concurrent.futures.as_completed(futures):
        graph_document_list.append(future.result())
    
end_time = datetime.now()  
print("Processing_time = ", end_time-start_time) 
```

### 总结

- **对于 I/O 密集型任务**：`asyncio` 通常更高效。
- **对于 CPU 密集型任务**：`ThreadPoolExecutor` 或 `ProcessPoolExecutor` 通常更适合。

选择哪种方式取决于你的具体任务和性能需求。对于大量的 I/O 操作，异步编程提供了更好的性能和可扩展性；对于需要 CPU 并行处理的任务，多线程或多进程可能更为合适。
