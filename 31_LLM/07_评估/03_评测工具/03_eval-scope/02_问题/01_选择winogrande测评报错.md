# 参考

https://github.com/modelscope/evalscope/issues/148

https://github.com/modelscope/evalscope/issues/188

# 问题

```bash
Traceback (most recent call last):
  File "/home/miniconda3/envs/train_py310/lib/python3.10/site-packages/opencompass/tasks/openicl_eval.py", line 462, in <module>
    inferencer.run()
  File "/home/miniconda3/envs/train_py310/lib/python3.10/site-packages/opencompass/tasks/openicl_eval.py", line 114, in run
    self._score()
  File "/home/miniconda3/envs/train_py310/lib/python3.10/site-packages/opencompass/tasks/openicl_eval.py", line 250, in _score
    result = icl_evaluator.score(**preds)
  File "/home/miniconda3/envs/train_py310/lib/python3.10/site-packages/opencompass/openicl/icl_evaluator/icl_hf_evaluator.py", line 83, in score
    metric = evaluate.load(local_path)
AttributeError: module 'evaluate' has no attribute 'load'
```

# 解决方法

尝试升级：
pip install evalscope[opencompass] -U

同时check一下ms-opencompass版本是否>=0.1.1，如果不是，则升级： pip install ms-opencompass -U

另外，OpenCompass backend也支持按需加载数据集，无需预先下载data.zip压缩包，可设置： export DATASET_SOURCE=ModelScope
