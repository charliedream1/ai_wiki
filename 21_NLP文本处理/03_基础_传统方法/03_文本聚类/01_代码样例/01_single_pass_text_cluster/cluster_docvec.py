# coding: utf-8
# File: cluster_docvec.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 21-09-04

from doc_vector import *
from singlepass_cluster_doc2vec import *

class ClusterDocvec:
    def __init__(self):
        self.clustor = SingelPassClusterDoc2vec()
        self.docvec = Doc2vec()
        return

    """聚类主函数"""
    def cluster(self, docs, text2index, theta):
        print('vectorizing docs....')
        doc_vectors = [self.docvec.get_sentvector(s) for s in docs]
        print('clustering docs....')
        clusters, cluster_text = self.clustor.cluster(doc_vectors, text2index, theta)
        return clusters, cluster_text
