You have two levers to move your cache off of C:

1. **Tell `datasets` (and Transformers) exactly where to put all of its caches**, by setting the right environment‐variables *before* you ever import anything from `datasets` or `transformers`.
2. **Turn off caching in the `.map()` calls** so that you don’t write out an intermediate Arrow file to disk at all.

---

## 1. Redirect all HF caches to your workspace

Add, at the very top of your script (before any `from datasets` or `from transformers`):

```python
import os

# this must come before any HuggingFace imports:
os.environ['HF_HOME']            = '/mnt/mdl/mdl_zoo/cache'   # root for all HF state
os.environ['HF_DATASETS_CACHE']  = os.path.join(os.environ['HF_HOME'], 'datasets')
os.environ['TRANSFORMERS_CACHE'] = os.path.join(os.environ['HF_HOME'], 'transformers')
```

With that in place, *every* cache (dataset arrow files, downloaded models, tokenizer files, ...) will live under `/mnt/share-workspace/mdl/mdl_zoo/cache` instead of `C:\Users\…\.cache`.

---

## 2. (Optional) Disable `.map()` caching entirely

By default, when you do:

```python
train_dataset = raw_train.map(
  preprocess_fn,
  batched=False,
  remove_columns=raw_train.column_names,
)
```

the `datasets` library will serialize the result to disk under your cache dir.  You can turn that off:

```diff
-train_dataset = raw_train.map(
-    preprocess_fn,
-    batched=False,
-    remove_columns=raw_train.column_names,
-)
+train_dataset = raw_train.map(
+    preprocess_fn,
+    batched=False,
+    remove_columns=raw_train.column_names,
+    load_from_cache_file=False,     # <— do _not_ write a cache file
+)
```

Do the same for your validation split:

```diff
-valid_dataset = raw_valid.map(
+valid_dataset = raw_valid.map(
     preprocess_fn,
     batched=False,
     remove_columns=raw_valid.column_names,
     load_from_cache_file=False,
)
```

---

### Putting it all together

```python
import os
# 1) Redirect all HF caches off of C:
os.environ['HF_HOME']            = '/mnt/share-workspace/mdl/mdl_zoo/cache'
os.environ['HF_DATASETS_CACHE']  = os.path.join(os.environ['HF_HOME'], 'datasets')
os.environ['TRANSFORMERS_CACHE'] = os.path.join(os.environ['HF_HOME'], 'transformers')

import torch
import numpy as np
from datasets import load_dataset
from transformers import (
    AutoConfig,
    Trainer,
    TrainingArguments,
    DataCollatorWithPadding,
    PreTrainedModel,
    PretrainedConfig,
)
# … rest of your imports …

# your constants, model setup, etc…

# 5.1 load raw parquet with a custom cache dir (optional, since HF_HOME covers it):
raw_train = load_dataset(
    "parquet",
    data_files=train_data_path,
    cache_dir=os.environ['HF_DATASETS_CACHE']
)["train"]
raw_valid = load_dataset(
    "parquet",
    data_files=valid_data_path,
    cache_dir=os.environ['HF_DATASETS_CACHE']
)["train"]

# 5.2 preprocess & disable map‐caching:
train_dataset = raw_train.map(
    preprocess_fn,
    batched=False,
    remove_columns=raw_train.column_names,
    load_from_cache_file=False,
)
valid_dataset = raw_valid.map(
    preprocess_fn,
    batched=False,
    remove_columns=raw_valid.column_names,
    load_from_cache_file=False,
)

# … the rest of your Trainer setup …
```

With these two changes, you will never again fill up your C:\ drive with HuggingFace cache files.
