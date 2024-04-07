# 1. 问题

使用paddle-gpu运行是，报如下错误：

```bash
Could not load library libcudnn_cnn_infer.so.8. Error: libcudnn_cnn_infer.so.8: cannot open shared object file: No such file or directory


--------------------------------------
C++ Traceback (most recent call last):
--------------------------------------
0   uv_run
1   uv__run_idle
2   paddle::AnalysisPredictor::ZeroCopyRun()
3   paddle::framework::NaiveExecutor::Run()
4   paddle::framework::OperatorBase::Run(paddle::framework::Scope const&, phi::Place const&)
5   paddle::framework::OperatorWithKernel::RunImpl(paddle::framework::Scope const&, phi::Place const&) const
6   paddle::framework::OperatorWithKernel::RunImpl(paddle::framework::Scope const&, phi::Place const&, paddle::framework::RuntimeContext*) const
7   void phi::KernelImpl<void (*)(phi::GPUContext const&, phi::DenseTensor const&, phi::DenseTensor const&, phi::DenseTensor const&, paddle::optional<phi::DenseTensor> const&, std::vector<int, std::allocator<int> > const&, std::vector<int, std::allocator<int> > const&, std::string const&, std::vector<int, std::allocator<int> > const&, int, std::string const&, std::string const&, bool, std::vector<int, std::allocator<int> > const&, int, phi::DenseTensor*, std::vector<phi::DenseTensor*, std::allocator<phi::DenseTensor*> >), &(void phi::fusion::ConvFusionKernel<float, phi::GPUContext>(phi::GPUContext const&, phi::DenseTensor const&, phi::DenseTensor const&, phi::DenseTensor const&, paddle::optional<phi::DenseTensor> const&, std::vector<int, std::allocator<int> > const&, std::vector<int, std::allocator<int> > const&, std::string const&, std::vector<int, std::allocator<int> > const&, int, std::string const&, std::string const&, bool, std::vector<int, std::allocator<int> > const&, int, phi::DenseTensor*, std::vector<phi::DenseTensor*, std::allocator<phi::DenseTensor*> >))>::KernelCallHelper<paddle::optional<phi::DenseTensor> const&, std::vector<int, std::allocator<int> > const&, std::vector<int, std::allocator<int> > const&, std::string const&, std::vector<int, std::allocator<int> > const&, int, std::string const&, std::string const&, bool, std::vector<int, std::allocator<int> > const&, int, phi::DenseTensor*, std::vector<phi::DenseTensor*, std::allocator<phi::DenseTensor*> >, phi::TypeTag<int> >::Compute<1, 3, 0, 0, phi::GPUContext const, phi::DenseTensor const, phi::DenseTensor const, phi::DenseTensor const>(phi::KernelContext*, phi::GPUContext const&, phi::DenseTensor const&, phi::DenseTensor const&, phi::DenseTensor const&)
8   void phi::fusion::ConvFusionKernel<float, phi::GPUContext>(phi::GPUContext const&, phi::DenseTensor const&, phi::DenseTensor const&, phi::DenseTensor const&, paddle::optional<phi::DenseTensor> const&, std::vector<int, std::allocator<int> > const&, std::vector<int, std::allocator<int> > const&, std::string const&, std::vector<int, std::allocator<int> > const&, int, std::string const&, std::string const&, bool, std::vector<int, std::allocator<int> > const&, int, phi::DenseTensor*, std::vector<phi::DenseTensor*, std::allocator<phi::DenseTensor*> >)
9   phi::fusion::(anonymous namespace)::CudnnConvDescManager::GetCudnnCacheInfo(std::vector<int, std::allocator<int> > const&, std::vector<int, std::allocator<int> > const&, std::vector<int, std::allocator<int> > const&, std::vector<int, std::allocator<int> > const&, std::vector<int, std::allocator<int> > const&, std::vector<int, std::allocator<int> > const&, std::vector<int, std::allocator<int> > const&, phi::DataType, int, cudnnDataType_t, cudnnTensorFormat_t, std::function<void (cudnnConvolutionFwdAlgo_t*, unsigned long*, cudnnTensorStruct*, cudnnFilterStruct*, cudnnTensorStruct*, cudnnConvolutionStruct*)> const&, std::string const&, double)
10  cudnnCreateConvolutionDescriptor

----------------------
Error Message Summary:
----------------------
FatalError: `Process abort signal` is detected by the operating system.
  [TimeInfo: *** Aborted at 1712490176 (unix time) try "date -d @1712490176" if you are using GNU date ***]
  [SignalInfo: *** SIGABRT (@0xebce) received by PID 60366 (TID 0x7fa5b591e4c0) from PID 60366 ***]
```

# 2. 原因

libcudnn和libcublas的软连接没有添加到shared library中

- 使用annaconda直接安装cudnn时，对应包不会被安装到shared library中
- 可能annaconda安装的版本和在系统中安装的cudnn版本不一致

# 3. 解决方法

1. 查找libcudnn.so和libcublas.so的位置：

   分别执行sudo find / -name libcudnn.so*和sudo find / -name libcublas.so*，如下图：
   - 注意：可以使用annaconda中的cudnn包
   - ![](.01_cudnn_version及各类so找不到_images/查找的图片.png)

2. 在/usr/lib中建立/usr/lib/x86_64-linux-gnu/libcudnn.so.7.5.0和/usr/local/cuda-10.0/targets/x86_64-linux/lib/libcublas.so.10.0.130的软链接（注意，你查找到的这两个文件很大可能与我不一样）：

   ```bash
   $ sudo ln -s /usr/lib/x86_64-linux-gnu/libcudnn.so.7.5.0 /usr/lib/libcudnn.so
   $ sudo ln -s /usr/local/cuda-10.0/targets/x86_64-linux/lib/libcublas.so.10.0.13 /usr/lib/libcublas.so
   ```

3. 查看/usr/lib下是否已有libcudnn.so和libcublas.so文件：

   ```bash
   $ ls /usr/lib/ |grep libcu
   ```
   
   如下图即添加成功

   ![](.01_cudnn_version及各类so找不到_images/成功添加检查.png)

此外，可能还会遇到libcudnn_cnn_infer.so.8，libcudnn_ops_infer.so.8等找不到，参照上述方法添加即可：

```bash
# sudo ln -s /root/miniconda3/envs/py310/lib/python3.10/site-packages/nvidia/cudnn/lib/libcudnn_cnn_infer.so.8 /usr/lib/libcudnn_cnn_infer.so.8
# sudo ln -s /root/miniconda3/envs/py310/lib/python3.10/site-packages/nvidia/cudnn/lib/libcudnn_ops_infer.so.8 /usr/lib/libcudnn_ops_infer.so.8
```

# 参考

[1] 报错“Cannot load cudnn shared library. Cannot invoke method cudnnGetVersion at (/paddle/paddle/fluid/“，https://blog.csdn.net/weixin_43220532/article/details/112472706