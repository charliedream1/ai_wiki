```json
{
    "train_batch_size": "auto",
    "train_micro_batch_size_per_gpu": "auto"
}
```

the Trainer will automatically set train_micro_batch_size_per_gpu 
to the value of args.per_device_train_batch_size and train_batch_size 
to args.world_size * args.per_device_train_batch_size * args.gradient_accumulation_steps.