# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 20:48:18 2019

@author: lenovo
"""
# encoding=utf-8

import numpy as np
from sklearn.metrics.pairwise import rbf_kernel
from sklearn.preprocessing import normalize
from sklearn.cluster import KMeans
 

def spectral_clustering(points, k):
    n = points.shape[0]
    # 使用径向基函数计算相似度
    W = rbf_kernel(points)
    for i in range(n):
        W[i, i] = 0
    # 计算度矩阵D并计算D^(-1/2)    
    Dn = np.diag(np.power(np.sum(W, axis=1), -0.5))
    # 标准化拉普拉斯矩阵：L=Dn*(D-Sim)*Dn=I-Dn*Sim*Dn
    L = np.eye(n) - np.dot(np.dot(Dn, W), Dn)
    # 特征值分解
    eigvals, eigvecs = np.linalg.eig(L)
    # 前k小的特征值对应的索引
    indices = np.argsort(eigvals)[:k]
    # 取出前k小的特征值对应的特征向量，并进行归一化（默认按行）
    subvecs = normalize(eigvecs[:, indices])
    # 使用KMeans进行聚类
    return KMeans(n_clusters=k).fit_predict(subvecs)
