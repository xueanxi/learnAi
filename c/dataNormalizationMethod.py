#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-28 20:21:08
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

import os
from numpy import *
# 数据归一化
# 1.数据标准化，属于归一化的一种
# 2.标准化欧式距离


# 标准化欧式距离： 标准化后的值 = （标准化前的值 - 分量的均值）/分量的标准差
vectormat = mat([[1, 2, 3], [4, 5, 6]])
v12 = vectormat[0] - vectormat[1]
print('标准化前的值', sqrt(v12 * v12.T))
# normal
varmat = std(vectormat.T, axis=0)
normvmat = (vectormat - mean(vectormat)) / varmat.T
normv12 = normvmat[0] - normvmat[1]
print('标准化后的值', sqrt(normv12 * normv12.T))
