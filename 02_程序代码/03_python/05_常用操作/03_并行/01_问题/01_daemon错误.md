
# 更新时间：2024-06-13

文中方法未验证

# 问题

multiprocessing是Python内建的多进程库。似乎它的Pool有一个问题是，当起了多进程后，在这些进程中很难再起新的进程，因为会报错 - AssertionError: daemonic processes are not allowed to have children.

因为 multiprocessing 的 Pool 起的进程是守护进程（daemon），而daemon又不允许spawn出自己的子进程，所以上面的foo()中就无法生成新的进程了。

# 解决方法1

解决的办法是自己写一个wrapper，封装一下 multiprocessing 的 Pool，令其生成的 Process 不是 daemon. 完整的代码如下：

```python
import multiprocessing
import multiprocessing.pool
import time

class NoDaemonProcess(multiprocessing.Process):
    # make 'daemon' attribute always return False
    def _get_daemon(self):
        return False
    def _set_daemon(self, value):
        pass
    daemon = property(_get_daemon, _set_daemon)


# We sub-class multiprocessing.pool.Pool instead of multiprocessing.Pool
# because the latter is only a wrapper function, not a proper class.
class NoDaemonProcessPool(multiprocessing.pool.Pool):
    Process = NoDaemonProcess


def work(index):
    count = 5
    while (count > 0):
        print("Process %s is running in round %d..." % (index, 6-count))
        time.sleep(1)
        count -= 1

def foo(index):
    worker_number = 4
    process_pool = multiprocessing.Pool(worker_number)
    
    for i in range(worker_number):
        worker_index = "%s.%s" % (index, i)
        process_pool.apply_async(work, (worker_index, ))
        
    process_pool.close()
    process_pool.join()


def test_pool():
    process_number = 2
    process_pool = NoDaemonProcessPool(process_number)
    
    process_pool.map(foo, range(process_number))
    
    process_pool.close()
    process_pool.join()
    
    print("Test ends")
    

def main():
    test_pool()
    
if __name__ == '__main__':
    main()

```

# 解决方法2

如果不使用 multiprocessing 的 Pool，只是使用其 Process，则相对简单很多，只要在创建 Process 的时候，令其daemon参数为False即可；或者完全不写daemon参数也可以，因为它默认就是False的。

```python
import multiprocessing
import time

def work(index):
    count = 5
    while (count > 0):
        print("Process %s is running in round %d..." % (index, 6-count))
        time.sleep(1)
        count -= 1

def foo(index):
    worker_number = 4
    process_list = list()
    
    for i in range(worker_number):
        worker_index = "%s.%s" % (index, i)
        process_list.append(multiprocessing.Process(target=work, args=(worker_index,)))
        
    for process in process_list:
        process.start()
    for process in process_list:
        process.join()

def main():
    process_number = 2
    process_list = list()
    
    for i in range(process_number):
        process_list.append(multiprocessing.Process(target=foo, args=(i,), daemon=False))
    
    for process in process_list:
        process.start()
    for process in process_list:
        process.join()
        
    print("Test ends")
    
    
if __name__ == '__main__':
    main()

```

那么，为什么Pool里的Process默认daemon参数是True，而直接使用Process的时候daemon参数默认又是False呢？
这是否说明Pool里的进程如果不是daemon的话，一旦运行函数结束，它就不存在了呢？
其实也不是。进程池里的进程就算不是daemon，也依然能很好地保持固定的数量。
看下面的例子：创建10个任务，但进程池NoDaemonProcessPool里只有2个进程，也依然能够完成10个任务，而不会因为不是daemon就完成一个任务而退出。

```python
import multiprocessing
import multiprocessing.pool
import time

class NoDaemonProcess(multiprocessing.Process):
    # make 'daemon' attribute always return False
    def _get_daemon(self):
        return False
    def _set_daemon(self, value):
        pass
    daemon = property(_get_daemon, _set_daemon)


# We sub-class multiprocessing.pool.Pool instead of multiprocessing.Pool
# because the latter is only a wrapper function, not a proper class.
class NoDaemonProcessPool(multiprocessing.pool.Pool):
    Process = NoDaemonProcess


def foo(index):
    print("Task %d is done" % index)


def test_pool():
    process_number = 2
    process_pool = NoDaemonProcessPool(process_number)
    
    process_pool.map(foo, range(10))
    
    process_pool.close()
    process_pool.join()
    
    print("Test ends")
    

def main():
    test_pool()
    
if __name__ == '__main__':
    main()


```

# 解决方法3

```python
# 新写法
from billiard.pool import Pool
pool = Pool(processes=20)
    for n in range(100):
        pool.apply_async(func=func_name, args=(n))
    pool.close()
    pool.join()
```

# 总结

multiprocessing的Pool所起的进程是守护进程(daemon), 因此它无法再起子进程；
如果需要让Pool所起的进程能够创建子进程，就需要自己写类包装原有的multiprocessing.pool.Pool，令其产生的进程不是daemon. 见示例程序-3.
当Pool所起的进程不是daemon时，进程池Pool依然能够维持固定的进程数量；
multiprocessing的Process被创建出来时默认就不是daemon，因此它可以创建子进程，但也可以使用daemon=True的参数令其为daemon.

# 参考

[1] 在multiprocessing的Pool所起的进程中再起进程，https://blog.csdn.net/nirendao/article/details/128945428
[2] 解决daemonic processes are not allowed to have children，https://blog.csdn.net/dqchouyang/article/details/133707879