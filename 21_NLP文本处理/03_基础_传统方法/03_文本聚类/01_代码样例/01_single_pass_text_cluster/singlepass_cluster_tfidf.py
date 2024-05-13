# coding: utf-8
# File: singlepass_cluster_tfidf.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 21-09-04

import numpy as np
from gensim import corpora, models, matutils


class SingelPassClusterTfidf():
    '''
        1.利用tfidf vec计算cossim
    '''
    def tfidf_vec(self, corpus, pivot=10, slope=0.25):
        dictionary = corpora.Dictionary(corpus)  # 形成词典映射
        self.dict_size = len(dictionary)
        print('dictionary size:{}'.format(len(dictionary)))
        corpus = [dictionary.doc2bow(text) for text in corpus]  # 词的向量表示
        tfidf = models.TfidfModel(corpus, pivot=pivot, slope=slope)
        corpus_tfidf = tfidf[corpus]
        return corpus_tfidf

    def get_max_similarity(self, cluster_cores, vector):
        max_value = 0
        max_index = -1
        for k, core in cluster_cores.items():
            similarity = matutils.cossim(vector, core)
            if similarity > max_value:
                max_value = similarity
                max_index = k
        return max_index, max_value

    def single_pass(self, corpus_vec, corpus, theta):
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
                max_index, max_value = self.get_max_similarity(cluster_cores, vector)
                if max_value > theta:
                    clusters[max_index].append(vector)
                    text_matrix = matutils.corpus2dense(clusters[max_index], num_terms=self.dict_size,
                                                        num_docs=len(clusters[max_index])).T  # 稀疏转稠密
                    core = np.mean(text_matrix, axis=0)  # 更新簇中心
                    core = matutils.any2sparse(core)  # 将稠密向量core转为稀疏向量
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

    def fit_transform(self, corpus, raw_data, theta=0.6):
        tfidf_vec = self.tfidf_vec(corpus)  # tfidf_vec是稀疏向量
        clusters, cluster_text = self.single_pass(tfidf_vec, raw_data, theta)
        return clusters, cluster_text