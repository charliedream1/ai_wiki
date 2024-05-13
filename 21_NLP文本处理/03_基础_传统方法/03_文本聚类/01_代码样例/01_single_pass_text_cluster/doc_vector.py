# coding: utf-8
# File: doc_vector.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 21-09-04

import jieba.posseg as pseg
import os
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import numpy as np


class Doc2vec:
    def __init__(self):
        base_path = '/'.join(os.path.abspath(__file__).split('/')[:-1])
        self.embedding_path = os.path.join(base_path, 'model/token_vector.bin')
        self.model = gensim.models.KeyedVectors.load_word2vec_format(self.embedding_path, binary=False)

    '''获取词向量文件'''
    def get_wordvector(self, word):
        try:
            return self.model[word]
        except:
            return np.zeros(200)

    """average pooling对句子进行向量化表示"""
    def get_sentvector(self, text):
        words = [i for i in text]
        sent_vector = np.zeros(200)
        for word in words:
            sent_vector += self.get_wordvector(word)
        sent_vector = sent_vector/len(words)
        return sent_vector

    '''基于余弦相似度计算句子之间的相似度，句子向量等于字符向量求平均'''
    def similarity_cosine(self, vector1, vector2):
        cos1 = np.sum(vector1*vector2)
        cos21 = np.sqrt(sum(vector1**2))
        cos22 = np.sqrt(sum(vector2**2))
        similarity = cos1/float(cos21*cos22)
        return similarity

