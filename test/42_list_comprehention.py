#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-20 18:47:02
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

import os
# 列表推导，用于创建另外一张符合指定条件的表
list1 = [1, 5, 2, 5, 7, 2, 8, 3]
list2 = [2 * i for i in list1 if i >= 3]
print('lsit2 = ', list2)
