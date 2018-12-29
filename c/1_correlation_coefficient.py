#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-28 19:48:48
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

# 相关系数 和 相关距离
import numpy as np
from numpy import *

featuremat = np.mat(
    [[1, 2, 3, 4, 5, 6], [3, 2, 3, 4, 5, 6]])
print("矩阵每一行的相关系数:")
print("1 python 方法计算:")
print(np.corrcoef(featuremat))

print("2 普通方法计算:")
# 计算均值
mv1 = np.mean(featuremat[0])
mv2 = np.mean(featuremat[1])
# 计算两列的标准差
dv1 = np.std(featuremat[0])
dv2 = np.std(featuremat[1])
corref = mean(multiply(featuremat[0] - mv1, featuremat[1] - mv2)) / (dv1 * dv2)
print(corref)

# 马氏距离
featuremat2 = np.mat(
    [[1, 2, 3, 4, 5, 6], [9, 2, 9, 4, 5, 6]])
covinv = linalg.inv(cov(featuremat2))
tp = featuremat2.T[0] - featuremat2.T[1]
distMa = sqrt(dot(dot(tp, covinv), tp.T))
print("\n\n\n马氏距离")
print(distMa)
