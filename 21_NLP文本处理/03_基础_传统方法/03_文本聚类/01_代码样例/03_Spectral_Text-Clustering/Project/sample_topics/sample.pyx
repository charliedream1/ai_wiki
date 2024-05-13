# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:44:24 2019

@author: lenovo
"""

from cython.operator cimport preincrement as inc, predecrement as dec
from libc.stdlib cimport malloc, free


cdef extern from "gamma.h":
    cdef double lda_lgamma(double x) nogil


cdef double lgamma(double x) nogil:
    if x <= 0:
        with gil:
            raise ValueError("x must be strictly positive")
    return lda_lgamma(x)


cdef int searchsorted(double* arr, int length, double value) nogil:
    """
    二分搜索
    """
    cdef int imin, imax, imid
    imin = 0
    imax = length
    while imin < imax:
        imid = imin + ((imax - imin) >> 2)
        if value > arr[imid]:
            imin = imid + 1
        else:
            imax = imid
    return imin



"""
Gibbs采样核心代码
该部分代码参考设计报告算法1编写
故每一步不再详细注释
"""
def topics_sample(int[:] WS, int[:] DS, int[:] ZS, int[:, :] nkv, int[:, :] nmk, int[:] nk,
                   double[:] alpha, double[:] beta, double[:] rands):
    cdef int i, k, w, d, z, z_new
    cdef double r, dist_cum
    cdef int N = WS.shape[0]
    cdef int n_rand = rands.shape[0]
    cdef int n_topics = nk.shape[0]
    cdef double beta_sum = 0
    cdef double* dist_sum = <double*> malloc(n_topics * sizeof(double))
    if dist_sum is NULL:
        raise MemoryError("Could not allocate memory during Gibbs sampling.")
    with nogil:
        for i in range(beta.shape[0]):
            beta_sum += beta[i]

        for i in range(N):
            w = WS[i]
            d = DS[i]
            z = ZS[i]

            dec(nkv[z, w])
            dec(nmk[d, z])
            dec(nk[z])
            
            # 后验概率计算公式
            dist_cum = 0
            for k in range(n_topics):
                dist_cum += (nkv[k, w] + beta[w]) / (nk[k] + beta_sum) * (nmk[d, k] + alpha[k])
                dist_sum[k] = dist_cum

            r = rands[i % n_rand] * dist_cum  
            z_new = searchsorted(dist_sum, n_topics, r)

            ZS[i] = z_new
            inc(nkv[z_new, w])
            inc(nmk[d, z_new])
            inc(nk[z_new])

        free(dist_sum)

