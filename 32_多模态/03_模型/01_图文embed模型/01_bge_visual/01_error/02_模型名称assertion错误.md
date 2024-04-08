# 1. 问题

时间：问题记录于2024-04-08，之后该代码仓，可能已经更新。

当传入本地模型路径时，会存在如下的模型名称assertion错误。
FlagEmbedding/visual/modeling.py does have bug of assert with the name. I run code as below. I will meet assertion error.

# 2. 解决方案

```python
from torch import nn, Tensor

class Visualized_BGE(nn.Module):
    def __init__(self,
                 model_name_bge: str = None,
                 model_weight = None, # "/path/to/your/weight/file/"
                 normlized: bool = True,
                 sentence_pooling_method: str = 'cls',
                 negatives_cross_device: bool = False,
                 temperature: float = 0.02, # 1.0
                 ):
        super().__init__()
        # assert model_name_bge in ["BAAI/bge-base-en-v1.5", "BAAI/bge-m3"]
        assert model_weight is not None
        name_flag = False
        for name in ["bge-base-en-v1.5", "bge-m3"]:
            if name in model_name_bge:
                name_flag = True

        if not name_flag:
            raise ValueError(f"model_name_bge should not be {name}")
        
        self.model_name_bge = model_name_bge
        
        # if model_name_bge == 'BAAI/bge-base-en-v1.5':
        #     model_name_eva = "EVA02-CLIP-B-16"
        #     self.hidden_dim = 768
        #     self.depth = 12
        # elif model_name_bge == 'BAAI/bge-m3':
        #     model_name_eva = "EVA02-CLIP-L-14"
        #     self.hidden_dim = 1024
        #     self.depth = 24

        if 'bge-base-en-v1.5' in model_name_bge:
            model_name_eva = "EVA02-CLIP-B-16"
            self.hidden_dim = 768
            self.depth = 12
        elif 'bge-m3' in model_name_bge:
            model_name_eva = "EVA02-CLIP-L-14"
            self.hidden_dim = 1024
            self.depth = 24
```

# 参考

[1] Visualized_BGE No module named 'eva_clip' #627，https://github.com/FlagOpen/FlagEmbedding/issues/627
