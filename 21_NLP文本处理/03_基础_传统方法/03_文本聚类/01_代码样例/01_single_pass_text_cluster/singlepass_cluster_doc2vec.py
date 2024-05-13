# coding: utf-8
# File: singlepass_cluster_doc2vec.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 21-09-04

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class SingelPassClusterDoc2vec():
    def cluster(self, doc_vec, text2index, theta):
        clusters, cluster_text = self.doc2vec_single_pass(doc_vec, text2index, theta)
        return clusters, cluster_text

    def get_doc2vec_similarity(self, cluster_cores, vector):
        max_value = 0
        max_index = -1
        for k, core in cluster_cores.items():
            similarity = cosine_similarity(vector.reshape(1, -1), core.reshape(1, -1))
            similarity = similarity[0, 0]
            if similarity > max_value:
                max_value = similarity
                max_index = k
        return max_index, max_value

    def doc2vec_single_pass(self, corpus_vec, corpus, theta):
        clusters = {}
        cluster_cores = {}
        cluster_text = {}
        num_topic = 0
        cnt = 0
        for vector, text in zip(corpus_vec, corpus):
            if num_topic == 0:
                clusters.setdefault(num_topic, []).append(vector)
                cluster_cores[num_topic] = vector
                cluster_text.setdefault(num_topic, []).append(text)
                num_topic += 1
            else:
                max_index, max_value = self.get_doc2vec_similarity(cluster_cores, vector)
                if max_value > theta:
                    clusters[max_index].append(vector)
                    core = np.mean(clusters[max_index], axis=0)  # 更新簇中心
                    cluster_cores[max_index] = core
                    cluster_text[max_index].append(text)
                else:  # 创建一个新簇
                    clusters.setdefault(num_topic, []).append(vector)
                    cluster_cores[num_topic] = vector
                    cluster_text.setdefault(num_topic, []).append(text)
                    num_topic += 1
            cnt += 1
            if cnt % 100 == 0:
                print('processing {}...'.format(cnt))
        return clusters, cluster_text