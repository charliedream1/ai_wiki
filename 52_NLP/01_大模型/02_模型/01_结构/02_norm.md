1. BatchNorm

    BatchNorm主要对数据的一定维度在batch数据中进行归一，一般来说应用于图像。

    这种方法很难适用于序列数据，对于序列数据而言，在batch维度做归一意义不大，而且一个batch内的序列长度不同。

2. LayerNorm

    LayerNorm是针对序列数据提出的一种归一化方法，主要在layer维度进行归一化，即对整个序列进行归一化。layerNorm会计算一个layer的所有activation的均值和方差，利用均值和方差进行归一化。

    具体公式如下：
    
    

# 参考

[1] 大模型面经——大模型中用到的归一化方法总结，https://mp.weixin.qq.com/s?__biz=Mzg4MTkwMTQ4NA==&mid=2247484510&idx=1&sn=50821717fbd4783deb3641fb71a9dbea&chksm=cef184905c5696cb50e1b639587ce4f4cd6d33264dd9ebe1059631d767ad012c717d3d254e6d&scene=132&exptype=timeline_recommend_article_extendread_samebiz&show_related_article=1&subscene=0&scene=132#wechat_redirect