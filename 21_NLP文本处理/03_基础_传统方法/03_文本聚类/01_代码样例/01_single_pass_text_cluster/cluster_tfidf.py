# coding: utf-8
# File: cluster_tfidf.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 21-09-04

from singlepass_cluster_tfidf import *

class ClusterTfidf:
    def __init__(self):
        self.clustor = SingelPassClusterTfidf()
        return

    """聚类主函数"""
    def cluster(self, corpus, text2index, theta=0.6):
        clusters, cluster_text = self.clustor.fit_transform(corpus, text2index, theta)
        return clusters, cluster_text
