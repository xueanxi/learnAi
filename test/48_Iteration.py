#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-21 22:32:27
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

import os


def getMaxAndMin(list1):
    max = list1[0]
    min = list1[0]
    for item in list1:
        if item >= max:
            max = item
    for item in list1:
        if item <= min:
            min = item
    return max, min

list1 = [-32, 4234, 232, 3213, 545, 67, 1, 13, -3213]
print('max and min:', getMaxAndMin(list1))


L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [item.lower() for item in L1 if isinstance(item, str)]
print('L2', L2)
