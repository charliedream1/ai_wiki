在验证（evaluation）阶段，`Trainer` 会默认收集所有批次的 `logits`（或 `predictions`）到内存里，最后再一次性把它们 `torch.cat`，这在数据量大、GPU 显存不够时就容易出现 OOM。解决思路主要有三种：

1. **分批次累积（eval\_accumulation\_steps）**
   在 `TrainingArguments` 里加上

   ```python
   eval_accumulation_steps=1
   ```

   这样 `Trainer` 就不会把所有批次的输出一次性保存在显存里，而是每 `eval_accumulation_steps` 批拼一次，再释放前面的缓存。

2. **只返回 Loss，不缓存 Logits（prediction\_loss\_only）**
   如果你在验证阶段只关心 `eval_loss` 而不需要用 `compute_metrics` 对输出做统计，可以在 `TrainingArguments` 里加：

   ```python
   prediction_loss_only=True
   ```

   这样 Trainer 在 `evaluate()` 时只会计算并返回 loss，不会保存 `logits`、`predictions`。

3. **降低 eval batch size**
   把

   ```python
   per_device_eval_batch_size=8
   ```

   改成更小的，比如 4 或 2，也能显著减少单次显存占用。

---

### 推荐改法

下面给出一个示例，把上述三点都加进去（你可以根据需要只选其中一两点）：

```python
training_args = TrainingArguments(
    output_dir=save_dir,
    num_train_epochs=3,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=4,      # ↓ 把 eval batch size 减半
    eval_accumulation_steps=1,         # ↓ 分批次累积 eval 输出
    prediction_loss_only=True,         # ↓ 只返回 loss，不缓存 logits
    learning_rate=2e-5,
    weight_decay=0.01,
    warmup_steps=100,
    logging_steps=10,
    evaluation_strategy="steps",
    eval_steps=100,
    save_steps=500,
    save_total_limit=2,
    seed=3407,
    fp16=not torch.cuda.is_bf16_supported(),
    bf16=torch.cuda.is_bf16_supported(),
    load_best_model_at_end=True,
    metric_for_best_model="eval_loss",
)
```

然后继续用原来的 `Trainer(...)`、`trainer.train()` 就可以避免在验证阶段把所有 logits 一次性拼到显存里，从而解决 OOM 问题。
