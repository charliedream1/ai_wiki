tqdm模块是python进度条库

```python
import time
from tqdm import tqdm

with tqdm(total=200) as pbar:
    pbar.set_description('Processing:')
    # total表示总的项目, 循环的次数20*10(每次更新数目) = 200(total)
    for i in range(20):
        # 进行动作, 这里是过0.1s
        time.sleep(0.1)
        # 进行进度更新, 这里设置10个
        pbar.update(10)
Processing:: 100%|██████████| 200/200 [00:02<00:00, 91.94it/s]
```