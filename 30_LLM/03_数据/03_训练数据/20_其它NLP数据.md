# 1. 专项数据
## 1.1. 总结类任务

1. ADGEN

    ADGEN 数据集任务为根据输入（content）生成一段广告词（summary）。
    
    数据集包含：train.json, dev.json
    
    ```json
    {
        "content": "类型#上衣*版型#宽松*版型#显瘦*图案#线条*衣样式#衬衫*衣袖型#泡泡袖*衣款式#抽绳",
        "summary": "这件衬衫的款式非常的宽松，利落的线条可以很好的隐藏身材上的小缺点，穿在身上有着很好的显瘦效果。领口装饰了一个可爱的抽绳，漂亮的绳结展现出了十足的个性，配合时尚的泡泡袖型，尽显女性甜美可爱的气息。"
    }
    ```
    
    从 [Google Drive](https://drive.google.com/file/d/13_vf0xRTQsyneRKdD1bZIr93vBGOczrk/view?usp=sharing) 或者 
    [Tsinghua Cloud](https://cloud.tsinghua.edu.cn/f/b3f119a008264b1cabd1/?dl=1) 下载处理好的 ADGEN 数据集，将解压后的 `AdvertiseGen` 目录放到本目录下。


# 2. NLP类任务

1. CLUEDatasetSearch
    - https://github.com/CLUEbenchmark/CLUEDatasetSearch
    - 3.5k stars

