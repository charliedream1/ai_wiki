# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 21:02:53 2019

@author: lenovo
"""

"""Latent Dirichlet allocation using collapsed Gibbs sampling"""

import numpy as np
import numbers
import logging
import sample

# 日志
logger = logging.getLogger('LDAModel')


def check_random_state(seed):
    """返回一个随机种子"""
    if seed is None:
        return np.random.mtrand._rand
    if isinstance(seed, (numbers.Integral, np.integer)):
        return np.random.RandomState(seed)
    if isinstance(seed, np.random.RandomState):
        return seed
    raise ValueError("{} cannot be used as a random seed.".format(seed))

def matrix_to_lists(doc_word):
    """
    将稀疏计数矩阵转换为单词和文档索引数组
    """
    if np.count_nonzero(doc_word.sum(axis=1)) != doc_word.shape[0]:
        logger.warning("all zero row in document-term matrix found")
    if np.count_nonzero(doc_word.sum(axis=0)) != doc_word.shape[1]:
        logger.warning("all zero column in document-term matrix found")
    sparse = True
    try:
        doc_word = doc_word.copy().tolil()
    except AttributeError:
        sparse = False

    if sparse and not np.issubdtype(doc_word.dtype, int):
        raise ValueError("expected sparse matrix with integer values, found float values")

    ii, jj = np.nonzero(doc_word)
    if sparse:
        ss = tuple(doc_word[i, j] for i, j in zip(ii, jj))
    else:
        ss = doc_word[ii, jj]

    DS = np.repeat(ii, ss).astype(np.intc)
    WS = np.repeat(jj, ss).astype(np.intc)
    return WS, DS

class LDA:
    """
    LDA模型(Gibbs 采样)
    """

    def __init__(self, n_topics, n_iter=2000, alpha=0.1, beta=0.01,random_state=None):
        self.n_topics = n_topics # 主题数
        self.n_iter = n_iter     # 迭代次数
        self.alpha = alpha       # alpha初值
        self.beta = beta         # beta初值
        
		# 错误提示
        if alpha <= 0 or beta <= 0:
            raise ValueError("alpha and beta must be greater than zero.")

        # 生成随机数
        self.random_state=random_state
        rng = check_random_state(self.random_state)
        self._rands = rng.rand(1024**2 // 8) 

    def fit_transform(self, X, y=None):
        """
        对X降维,拟合模型
        """
        if isinstance(X, np.ndarray):
            X = np.atleast_2d(X)
        self.fit(X)
        return self.theta
    
    
    def fit(self, X):
        """
        拟合模型
        X:  (样本, 特征向量)
        """
        random_state = check_random_state(self.random_state)
        rands = self._rands.copy()
        self.parameter_init(X)
        for it in range(self.n_iter):
            # random shift
            random_state.shuffle(rands)
            # 采样
            self.sample_topics(rands)
            
        # 计算phi:主题 k 中各特征词的 multinomial 分布
        self.phi = (self.nkv + self.beta).astype(float)
        self.phi /= np.sum(self.phi, axis=1)[:, np.newaxis]
        
        # 计算theta:文档 m 各隐含主题的 multinomial 分布
        self.topic_word_ = self.phi
        self.theta = (self.nmk + self.alpha).astype(float)
        self.theta /= np.sum(self.theta, axis=1)[:, np.newaxis]

        # 删除变量，节约内存
        del self.WS
        del self.DS
        del self.ZS
        return self

    def parameter_init(self, X):
        """初始化相关参数"""
        D, W = X.shape
        N = int(X.sum())
        n_topics = self.n_topics
        
        # 主题k特征词v的个数
        self.nkv = nkv = np.zeros((n_topics, W), dtype=np.intc)
        # 文档m中分配給主题的k的特征词个数
        self.nmk = nmk = np.zeros((D, n_topics), dtype=np.intc)
        # 主题k特征词的个数
        self.nk = nk = np.zeros(n_topics, dtype=np.intc)

		# 单词和文档索引数组
        self.WS, self.DS = WS, DS = matrix_to_lists(X)
		# 主题索引数组
        self.ZS = ZS = np.empty_like(self.WS, dtype=np.intc)
        np.testing.assert_equal(N, len(WS))
        
        # 初始化计数变量
        for i in range(N):
            w, d = WS[i], DS[i]
            z_new = i % n_topics
            ZS[i] = z_new
            nmk[d, z_new] += 1
            nkv[z_new, w] += 1
            nk[z_new] += 1
    
    
    def sample_topics(self, rands):
        """Gibbs 采样"""
        n_topics, vocab_size = self.nkv.shape
        alpha = np.repeat(self.alpha, n_topics).astype(np.float64)
        beta = np.repeat(self.beta, vocab_size).astype(np.float64)
        
        sample.topics_sample(self.WS, self.DS, self.ZS, self.nkv, self.nmk, self.nk,
                                alpha, beta, rands)

