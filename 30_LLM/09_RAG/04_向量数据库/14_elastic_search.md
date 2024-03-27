稀疏向量检索，目前来看速度也还可以，几乎是毫秒级返回结果

参考：https://github.com/FlagOpen/FlagEmbedding/issues/541

index构建为{
"mappings": {
"properties": {
"vector": {
"type": "object" //数据样例{"1": 0.8, "5": 0.1, "100000": 0.1}
}}
使用script_score查询match_all，编写painless脚本实现计算功能
Map docVector = doc['vector']或params._source['vector'];
for (Map.Entry entry : params.queryVector.entrySet()) {
String token = entry.getKey();
if (docVector.containsKey(token)) {
scores += entry.getValue() * docVector[token];
}
}
供参考。

我发现存成object会有索引超出1000限制的问题。
有两种解决办法：
1、扩大索引限制。可能需要较大内存，并在一定程度上影响效率。
2、不存成object，以字符串的形式存成keyword，就不会超出索引限制。此时painless的解析语言需要随之做出一定调整，由对object的解析转为对字符串的解析。同样能完美解决此问题。

使用request库进行ES的script接口调用就可以。速度是比较快的。
