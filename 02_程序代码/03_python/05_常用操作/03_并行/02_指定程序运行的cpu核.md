# 1. 用multiprocessing模块来指定特定的CPU核心运行代码

```python
import multiprocessing

def my_function():
    # 在此处编写你的代码
    print("Hello from process:", multiprocessing.current_process().name)

if __name__ == '__main__':
    # 指定要运行的CPU核心
    cpu_core = 0  # 将0替换为你想要的CPU核心编号

    # 创建进程对象
    process = multiprocessing.Process(target=my_function)

    # 绑定进程到特定的CPU核心
    process.cpu_affinity([cpu_core])

    # 启动进程
    process.start()
```

在上述代码中，我们首先定义了一个my_function函数，它是你想要在特定CPU核心上运行的代码。然后，我们在主程序中创建了一个进程对象process，将目标函数设置为my_function。接下来，我们使用cpu_affinity方法将进程绑定到指定的CPU核心，其中cpu_core变量表示要使用的核心编号。最后，我们启动进程，它将在指定的CPU核心上运行。

请注意，这段代码只能在支持绑定到特定CPU核心的操作系统上运行，如Linux。在某些操作系统上，如Windows，Python的multiprocessing模块可能没有提供绑定到特定核心的功能。在这种情况下，你可能需要使用特定于操作系统的其他方法来实现相同的效果。

如果是windows系统，可以使用如下方式：
    
```python
# coding: utf-8
import psutil


# 写个斐波那契数列计算函数，用于消耗cpu资源
def fibbo(number):
    if number <= 2:
        return 1
    else:
        return fibbo(number - 1) + fibbo(number - 2)


# 获取逻辑cpu的数量
count = psutil.cpu_count()
print(f"逻辑cpu的数量是{count}")
# Process实例化时不指定pid参数，默认使用当前进程PID，即os.getpid()
p = psutil.Process()
cpu_lst = p.cpu_affinity()
print("cpu列表", cpu_lst)
# 将当前进程绑定到cpu15上运行，列表中也可以写多个cpu
p.cpu_affinity([15])
# 运行函数消耗cpu资源
fibbo(80)
```

运行效果:

```text
逻辑cpu的数量是16
cpu列表 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
```

![](.02_指定程序运行的cpu核_images/cpu状态监控.png)

# 参考

[1] python如何指定cpu某个核运行，https://www.cnblogs.com/chentiao/p/17510620.html