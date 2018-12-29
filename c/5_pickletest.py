#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-29 15:44:49
# @Author  : anxi.xue (xueanxi@163.com)
# @Link    : ${link}
# @Version : $Id$

import pickle
import os
from os.path import dirname, abspath
from numpy import *

A = mat([[1, 2, 3, 4, 5, 6], [4, 3, 5, 78, 9, 52], [3, 4, 6, 2, 21, 8]])
print(A)

path = dirname(abspath(__file__))
parentpath = dirname(abspath(path))
rootdata = parentpath + os.sep + 'rootdata'

savePath = rootdata + os.sep + 'save.dat'
file = open(savePath, 'wb')
pickle.dump(A, file)

file = open(savePath, 'rb')
B = pickle.load(file)
print('read:\n', B)
