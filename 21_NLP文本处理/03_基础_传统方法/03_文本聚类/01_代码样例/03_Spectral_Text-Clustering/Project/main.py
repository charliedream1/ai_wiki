# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 21:41:55 2019

@author: lenovo
"""

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn import metrics
from scipy import sparse
from sklearn.preprocessing import normalize

from LDAModel import LDA
import Spectral

import warnings
warnings.filterwarnings("ignore")


# 加载数据集
categories = ['comp.graphics',
              'rec.autos',
              'sci.crypt']
dataset = fetch_20newsgroups(subset = 'all', 
                             categories = categories,
                             remove=('headers', 'footers', 'quotes'))
size = dataset.target.shape[0]
documents = dataset.data

# 标签
labels = dataset.target

# 将文档转成TF-IDF向量
vectorizer = TfidfVectorizer(max_df = 0.5,
                             max_features = 2500,
                             min_df = 2,
                             stop_words = 'english',
                             use_idf = True)
tfidf_matrix = vectorizer.fit_transform(dataset.data)

# 计算每个文档单词出现的次数 tf:document-term matrix
tf_vectorizer = CountVectorizer(max_features=2500, stop_words='english')
tf = tf_vectorizer.fit_transform(documents)
tf_feature_names = tf_vectorizer.get_feature_names()


# 运行LDA
model = LDA(n_topics=180, n_iter=500, random_state=1)
topic_matrix=model.fit_transform(tf)

# 合并前先做归一化
sAnorm=normalize(tfidf_matrix, norm='l1', axis=1)    
sB = sparse.csr_matrix(topic_matrix) 
sBnorm= normalize(sB, norm='l1', axis=1)

# ----------------------------------------------------------

# TF-IDF特征

# 谱聚类
labels_=Spectral.spectral_clustering(tfidf_matrix,3)

# 匹配矩阵
cm = metrics.confusion_matrix(labels, labels_)
print("TF-IDF特征")
print("Matching matrix:")
print(cm)

# 聚类评价指标
print("ARI: %.3f" % metrics.adjusted_rand_score(labels, labels_))
print("NMI: %.3f" % metrics.normalized_mutual_info_score(labels, labels_))
print("FMI: %.3f" % metrics.fowlkes_mallows_score(labels, labels_))
print("\n")

# ----------------------------------------------------------

# 基于 LDA 的文档隐含主题 multinomial 分布特征

# 谱聚类
labels_=Spectral.spectral_clustering(topic_matrix,3)

# 匹配矩阵
cm = metrics.confusion_matrix(labels, labels_)
print("文档隐含主题分布特征：")
print("Matching matrix:")
print(cm)

# 聚类评价指标
print("ARI: %.3f" % metrics.adjusted_rand_score(labels, labels_))
print("NMI: %.3f" % metrics.normalized_mutual_info_score(labels, labels_))
print("FMI: %.3f" % metrics.fowlkes_mallows_score(labels, labels_))

print("\n")

# -----------------------------------------------------------------

# 组合特征
mat=sparse.hstack((sAnorm,sBnorm))

# 谱聚类
labels_=Spectral.spectral_clustering(mat,3)

# 匹配矩阵
cm = metrics.confusion_matrix(labels, labels_)
print("组合特征：")
print("Matching matrix:")
print(cm)

# 聚类评价指标
print("ARI: %.3f" % metrics.adjusted_rand_score(labels, labels_))
print("NMI: %.3f" % metrics.normalized_mutual_info_score(labels, labels_))
print("FMI: %.3f" % metrics.fowlkes_mallows_score(labels, labels_))
