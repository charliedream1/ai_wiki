# 1. 命令行指定

```bash
export CUDA_VISIBLE_DEVICES=0 #这里是要使用的GPU编号，正常的话是从0开始编号
python train.py
```

```bash
CUDA_VISIBLE_DEVICES=2,3,4 python train.py
```

# 2. python代码指定

1. 设置环境变量

   ```python
    import os 
    os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"  #（保证程序cuda序号与实际cuda序号对应）
    os.environ['CUDA_VISIBLE_DEVICES'] = "0,1"  #（代表仅使用第0，1号GPU）
   ```

2. 初始化模型时

   以model.cuda()为例，加载方法为：
    
    ```python
     model.cuda(gpu_id) # gpu_id为int类型变量，只能指定一张显卡
     model.cuda('cuda:'+str(gpu_ids)) #输入参数为str类型，可指定多张显卡
     model.cuda('cuda:1,2') #指定多张显卡的一个示例
    ```
  
3. 使用torch.cuda.set_device()接口

    在生成网络对象之前执行：torch.cuda.set_device(0)

    使用torch.cuda.set_device()可以更方便地将模型和数据加载到对应GPU上, 
    直接定义模型之前加入一行代码即可
    
    ```python
    torch.cuda.set_device(gpu_id) #单卡
    torch.cuda.set_device('cuda:'+str(gpu_ids)) #可指定多卡
    ```
    
     但是这种写法的优先级低，如果model.cuda()中指定了参数，
     那么torch.cuda.set_device()会失效，而且pytorch的官方文档中明确说明，不建议用户使用该方法。

4. 使用pytorch的并行GPU接口
   
   net = torch.nn.DataParallel(model, device_ids=[0])

# 3 叠加使用

第1节和第2节所说的方法同时使用是并不会冲突，而是会叠加。比如在运行代码时使用

```shell
CUDA_VISIBLE_DEVICES=2,3,4,5 python3 train.py
```

而在代码内部又指定

```python
model.cuda(1)
loss.cuda(1)
tensor.cuda(1)
```

那么代码会在GPU3上运行。原理是CUDA_VISIBLE_DEVICES使得只有GPU2,3,4,5可见，
那么这4张显卡，程序就会把它们看成GPU0,1,2,3，.cuda(1)把模型/loss/数据都加载
到了程序所以为的GPU1上，则实际使用的显卡是GPU3。

如果利用.cuda()或torch.cuda.set_device()把模型加载到多个显卡上，
而实际上只使用一张显卡运行程序的话，那么程序会把模型加载到第一个显卡上，比如如果在代码中指定了

```python
model.cuda('cuda:2,1')
```

在运行代码时使用

```shell
CUDA_VISIBLE_DEVICES=2,3,4,5 python3 train.py
```

这一指令，那么程序最终会在GPU4上运行。   


# 参考

[1] python运行程序设置指定GPU(查看GPU使用情况), https://blog.csdn.net/weixin_43818631/article/details/118856558
[2] 在pytorch中指定显卡, shttps://zhuanlan.zhihu.com/p/166161217