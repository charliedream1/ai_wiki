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

2. 雅意信息抽取数据集
    - 论文 2023.12.24
       - YAYI-UIE: A Chat-Enhanced Instruction Tuning Framework for Universal Information Extraction
       - https://arxiv.org/abs/2312.15548
    - Github (162 star): https://github.com/wenge-research/YAYI-UIE
    - 模型下载地址：https://modelscope.cn/models/wenge-research/yayi-uie/
    - 数据下载地址：https://modelscope.cn/datasets/wenge-research/yayi_uie_sft_data/summary
    - 百万级语料中文54%，英文46%；其中其中数据集包括12个领域包括金融，社会，生物，商业，工业制造，化学，车辆，科学，疾病医疗，个人生活，安全和通用。覆盖数百个使用场景
      - NER：中文覆盖28个实体类型包括人物，地缘政治，组织，身体部位，药物等，英文覆盖130个实体类型包括Animal, Weapon, Conference, Book等。
      - RE：中文覆盖232种关系包括买资，增持，重组，国籍，别名，亲属，入股，转让，导致，发生地点，制造商等，英文覆盖236种关系包括founded by，state or province of headquarters，employee of，occupation，creator等。
      - EE：中文覆盖84种事件类型,包括中标，高管变动，产品行为-发布，公司上市等，和203种论元，英文覆盖45种事件类型，包括Born, Demonstrate, Meet, End Organization, Divorce等，和62种论元。
    - ![](.20_其它NLP数据_images/数据分布.png)
    - ![](.20_其它NLP数据_images/数据样例.png)