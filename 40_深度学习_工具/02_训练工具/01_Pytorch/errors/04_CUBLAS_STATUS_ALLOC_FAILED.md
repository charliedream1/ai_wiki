# 1. 问题

```text
Iteration:   0% 0/2971 [00:00<?, ?it/s]/pytorch/aten/src/THC/THCTensorIndex.cu:361: void indexSelectLargeIndex(TensorInfo<T, IndexType>, TensorInfo<T, IndexType>, TensorInfo<long, IndexType>, int, int, IndexType, IndexType, long) [with T = float, IndexType = unsigned int, DstDim = 2, SrcDim = 2, IdxDim = -2, IndexIsMajor = true]: block: [116,0,0], thread: [96,0,0] Assertion `srcIndex < srcSelectDimSize` failed. 
/pytorch/aten/src/THC/THCTensorIndex.cu:361: void indexSelectLargeIndex(TensorInfo<T, IndexType>, TensorInfo<T, IndexType>, TensorInfo<long, IndexType>, int, int, IndexType, IndexType, long) [with T = float, IndexType = unsigned int, DstDim = 2, SrcDim = 2, IdxDim = -2, IndexIsMajor = true]: block: [116,0,0], thread: [97,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
/pytorch/aten/src/THC/THCTensorIndex.cu:361: void indexSelectLargeIndex(TensorInfo<T, IndexType>, TensorInfo<T, IndexType>, TensorInfo<long, IndexType>, int, int, IndexType, IndexType, long) [with T = float, IndexType = unsigned int, DstDim = 2, SrcDim = 2, IdxDim = -2, IndexIsMajor = true]: block: [116,0,0], thread: [98,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
...
/pytorch/aten/src/THC/THCTensorIndex.cu:361: void indexSelectLargeIndex(TensorInfo<T, IndexType>, TensorInfo<T, IndexType>, TensorInfo<long, IndexType>, int, int, IndexType, IndexType, long) [with T = float, IndexType = unsigned int, DstDim = 2, SrcDim = 2, IdxDim = -2, IndexIsMajor = true]: block: [116,0,0], thread: [61,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
/pytorch/aten/src/THC/THCTensorIndex.cu:361: void indexSelectLargeIndex(TensorInfo<T, IndexType>, TensorInfo<T, IndexType>, TensorInfo<long, IndexType>, int, int, IndexType, IndexType, long) [with T = float, IndexType = unsigned int, DstDim = 2, SrcDim = 2, IdxDim = -2, IndexIsMajor = true]: block: [116,0,0], thread: [62,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
/pytorch/aten/src/THC/THCTensorIndex.cu:361: void indexSelectLargeIndex(TensorInfo<T, IndexType>, TensorInfo<T, IndexType>, TensorInfo<long, IndexType>, int, int, IndexType, IndexType, long) [with T = float, IndexType = unsigned int, DstDim = 2, SrcDim = 2, IdxDim = -2, IndexIsMajor = true]: block: [116,0,0], thread: [63,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
Traceback (most recent call last):
  File "run_language_modeling.py", line 799, in <module>
    main()
  File "run_language_modeling.py", line 749, in main
    global_step, tr_loss = train(args, train_dataset, model, tokenizer)
  File "run_language_modeling.py", line 353, in train
    outputs = model(inputs, masked_lm_labels=labels) if args.mlm else model(inputs, labels=labels)
  File "/usr/local/lib/python3.6/dist-packages/torch/nn/modules/module.py", line 532, in __call__
    result = self.forward(*input, **kwargs)
  File "/usr/local/lib/python3.6/dist-packages/transformers/modeling_bert.py", line 987, in forward
    encoder_attention_mask=encoder_attention_mask,
  File "/usr/local/lib/python3.6/dist-packages/torch/nn/modules/module.py", line 532, in __call__
    result = self.forward(*input, **kwargs)
  File "/usr/local/lib/python3.6/dist-packages/transformers/modeling_bert.py", line 790, in forward
    encoder_attention_mask=encoder_extended_attention_mask,
  File "/usr/local/lib/python3.6/dist-packages/torch/nn/modules/module.py", line 532, in __call__
    result = self.forward(*input, **kwargs)
  File "/usr/local/lib/python3.6/dist-packages/transformers/modeling_bert.py", line 407, in forward
    hidden_states, attention_mask, head_mask[i], encoder_hidden_states, encoder_attention_mask
  File "/usr/local/lib/python3.6/dist-packages/torch/nn/modules/module.py", line 532, in __call__
    result = self.forward(*input, **kwargs)
  File "/usr/local/lib/python3.6/dist-packages/transformers/modeling_bert.py", line 368, in forward
    self_attention_outputs = self.attention(hidden_states, attention_mask, head_mask)
  File "/usr/local/lib/python3.6/dist-packages/torch/nn/modules/module.py", line 532, in __call__
    result = self.forward(*input, **kwargs)
  File "/usr/local/lib/python3.6/dist-packages/transformers/modeling_bert.py", line 314, in forward
    hidden_states, attention_mask, head_mask, encoder_hidden_states, encoder_attention_mask
  File "/usr/local/lib/python3.6/dist-packages/torch/nn/modules/module.py", line 532, in __call__
    result = self.forward(*input, **kwargs)
  File "/usr/local/lib/python3.6/dist-packages/transformers/modeling_bert.py", line 216, in forward
    mixed_query_layer = self.query(hidden_states)
  File "/usr/local/lib/python3.6/dist-packages/torch/nn/modules/module.py", line 532, in __call__
    result = self.forward(*input, **kwargs)
  File "/usr/local/lib/python3.6/dist-packages/torch/nn/modules/linear.py", line 87, in forward
    return F.linear(input, self.weight, self.bias)
  File "/usr/local/lib/python3.6/dist-packages/torch/nn/functional.py", line 1372, in linear
    output = input.matmul(weight.t())
RuntimeError: CUDA error: CUBLAS_STATUS_ALLOC_FAILED when calling `cublasCreate(handle)`
`
```

# 2. 解决方法

很可能是batch过大，调小batch size，即解决

# 参考

[1] CUDA error: CUBLAS_STATUS_ALLOC_FAILED When running language modeling using bert-base-cased #3495，
    https://github.com/huggingface/transformers/issues/3495
[2] python运行报错RuntimeError: CUDA error: CUBLAS_STATUS_ALLOC_FAILED when calling `cublasCreate(handle)`，
    https://blog.csdn.net/m0_52347246/article/details/120177149