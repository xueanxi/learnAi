#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-28 20:08:20
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

from numpy import *

featuremat = mat(
    [[1, 2, 3], [1, 2, 3], [1, 5, 3]])
evals, evecs = linalg.eig(featuremat)
print("特征值:", evals)
print("特征向量:", evecs)

# 使用特征值和特征向量可以还原矩阵
print("使用特征值和特征向量可以还原矩阵:")
sigma = evals * eye(shape(featuremat)[0])
print(evecs * sigma * linalg.inv(evecs))
