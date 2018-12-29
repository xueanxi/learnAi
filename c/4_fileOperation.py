#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-28 20:33:32
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

import os
from os.path import dirname, abspath
import sys
import numpy as np
from numpy import *

# 文件操作 文件数据转化为矩阵


def file2matrix(path, delimater):
    fp = open(path, 'rb')
    content = fp.read()
    fp.close()
    rowList = content.splitlines()  # 按行转换为一维表
    # 逐行遍历，结果按照分隔符分成行向量
    l = []
    for row in rowList:
        line = row.decode(encoding='utf-8')
        newdata = line.split('.')
        l.append(newdata)
    recordlist = np.mat(l)
    return recordlist

path = dirname(abspath(__file__))
parentpath = dirname(abspath(path))
rootdata = parentpath + os.sep + 'rootdata'
pathlist = os.listdir(rootdata)
for path in pathlist:
    if isinstance(path, str):
        if path.endswith('.txt'):
            filePath = rootdata + os.sep + path
            # print('file:', filePath)
            recordmat = file2matrix2(filePath, ".")
            print(path, ':\n', recordmat)
