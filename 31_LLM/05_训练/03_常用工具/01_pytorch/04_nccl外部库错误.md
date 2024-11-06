# 错误

```text
: [rank18]: Traceback (most recent call last):                                                                                                                                    
: [rank18]:   File "/data/nvme3/src/train.py", line 28, in <module>                                                        
: [rank18]:     main()                                                                                                                                                            
: [rank18]:   File "/data/nvme3/src/train.py", line 19, in main                                                            
: [rank18]:     run_exp()                                                                                                                                                         
: [rank18]:   File "/data/nvme3/remote_prg/llm_trainer/src/llamafactory/train/tuner.py", line 50, in run_exp                                                             
: [rank18]:     run_sft(model_args, data_args, training_args, finetuning_args, generating_args, callbacks)                                                                        
: [rank18]:   File "/data/nvme3/remote_prg/llm_trainer/src/llamafactory/train/sft/workflow.py", line 47, in run_sft                                                      
: [rank18]:     dataset_module = get_dataset(template, model_args, data_args, training_args, stage="sft", **tokenizer_module)                                                     
: [rank18]:   File "/data/nvme3/remote_prg/llm_trainer/src/llamafactory/data/loader.py", line 260, in get_dataset                                                        
: [rank18]:     with training_args.main_process_first(desc="load dataset"):                                                                                                       
: [rank18]:   File "/home/miniconda3/envs/lf_trainer_py310/lib/python3.10/contextlib.py", line 135, in __enter__                                                            
: [rank18]:     return next(self.gen)                                                                                                                                             
: [rank18]:   File "/home/miniconda3/envs/lf_trainer_py310/lib/python3.10/site-packages/transformers/training_args.py", line 2460, in main_process_first                    
: [rank18]:     dist.barrier()                                                                                                                                                    
: [rank18]:   File "/home/miniconda3/envs/lf_trainer_py310/lib/python3.10/site-packages/torch/distributed/c10d_logger.py", line 83, in wrapper                              
: [rank18]:     return func(*args, **kwargs)                                                                                                                                      
: [rank18]:   File "/home/miniconda3/envs/lf_trainer_py310/lib/python3.10/site-packages/torch/distributed/distributed_c10d.py", line 4159, in barrier                       
: [rank18]:     work = group.barrier(opts=opts)                                                                                                                                   
: [rank18]: torch.distributed.DistBackendError: NCCL error in: ../torch/csrc/distributed/c10d/NCCLUtils.hpp:317, unhandled system error (run with NCCL_DEBUG=INFO for details), NC
CL version 2.21.5                                                                                                                                                                         
: [rank18]: ncclSystemError: System call (e.g. socket, malloc) or external library call failed or device error.                                                                   
: [rank18]: Last error:                                                                                                                                                           
: [rank18]: Call to ibv_reg_mr failed with error Bad address
```

# 解决方案

he traceback error you're encountering is a NCCL system error during the distributed training process. This error often happens in multi-GPU environments due to issues with inter-GPU communication, particularly with NCCL (NVIDIA Collective Communications Library). Here are some possible solutions to try:

实测方法4有用

1. 打印日志

    ```bash
    export NCCL_DEBUG=INFO
    ```

2. Verify Hardware/Driver Compatibility: 
   
    Ensure that the NCCL version is compatible with your hardware, drivers, and CUDA version. You mentioned NCCL version 2.21.5, so check if there are known issues with this specific version for your environment.

3. Set NCCL Socket Interface: 

   If you're using networked GPUs (e.g., across multiple machines), specifying the interface explicitly can help:

    ```bash
    export NCCL_SOCKET_IFNAME=<your_interface_name>
    ```

    Replace <your_interface_name> with your specific network interface (e.g., eth0 or ib0).

4. Disable Infiniband (if applicable): 
   
   If you're not using Infiniband or if it's not set up correctly, you might try disabling it:

    ```bash
    export NCCL_IB_DISABLE=1
    ```

5. 重启
