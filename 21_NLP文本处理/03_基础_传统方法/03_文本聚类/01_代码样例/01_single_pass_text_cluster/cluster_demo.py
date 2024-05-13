#coding = utf-8
# File: cluster_demo.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 21-09-04

import jieba
import json
import collections
from cluster_docvec import *
from cluster_tfidf import *

handler_docvec = ClusterDocvec()
handler_tfidf = ClusterTfidf()

class SinglePassCluster(object):
    """初始化"""
    def __init__(self, train_corpus_filepath, cluster_path):
        self.train_corpus_filepath = train_corpus_filepath
        self.cluster_path = cluster_path

    """读取文件数据"""
    def load_data(self, filepath):
        datas = []
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                datas.append(line)
        return datas

    """加载文档，并进行转换"""
    def load_docs(self, docs):
        corpus = [list(jieba.cut(s)) for s in docs]
        index2corpus = collections.OrderedDict()
        for index, line in enumerate(docs):
            index2corpus[index] = line
        text2index = list(index2corpus.keys())
        print('docs total size:{}'.format(len(text2index)))
        return text2index, index2corpus, corpus

    """保存聚类结果"""
    def save_cluster(self, method, index2corpus, cluster_text, cluster_path):
        clusterTopic_list = sorted(cluster_text.items(), key=lambda x: len(x[1]), reverse=True)
        print(clusterTopic_list)
        with open(cluster_path + '/cluster_%s.json' % method, 'w+', encoding='utf-8') as save_obj:
            for k in clusterTopic_list:
                data = dict()
                data["cluster_id"] = k[0]
                data["cluster_nums"] = len(k[1])
                data["cluster_docs"] = [{"doc_id": index, "doc_content": index2corpus.get(value)} for index, value in
                                        enumerate(k[1], start=1)]
                json_obj = json.dumps(data, ensure_ascii=False)
                save_obj.write(json_obj)
                save_obj.write('\n')

    """聚类运行主控函数"""
    def cluster(self, method="doc2vec", theta=0.6):
        docs = self.load_data(self.train_corpus_filepath)
        text2index, index2corpus, corpus = self.load_docs(docs)
        print("loaded %s samples...." % len(docs))
        if method == "tfidf":
            clusters, cluster_text = handler_tfidf.cluster(corpus, text2index, theta)
            self.save_cluster(method, index2corpus, cluster_text, cluster_path)
        else:
            clusters, cluster_text = handler_docvec.cluster(corpus, text2index, theta)
            self.save_cluster(method, index2corpus, cluster_text, cluster_path)
        return

if __name__ == '__main__':
    train_corpus_filepath = "data/train.txt"
    cluster_path= "result"
    method = "doc2vec"
    theta = 0.85
    handler = SinglePassCluster(train_corpus_filepath, cluster_path)
    handler.cluster(method=method, theta=theta)