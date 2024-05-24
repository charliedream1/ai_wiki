在线可视化RDF工具：https://www.ldf.fi/service/rdf-grapher

![](.04_RDF表示_images/配置格式.png)

RDF样例
```RDF
@prefix ex: <http://example.org/> .

ex:Event1 a ex:TariffIncrease ;
ex:eventDate "2024-05-14" ;
ex:location ex:USA ;
ex:participant ex:JoeBiden, ex:WhiteHouse ;
ex:impact "Higher tariffs on Chinese goods" .
```

![](.04_RDF表示_images/关系图.png)
