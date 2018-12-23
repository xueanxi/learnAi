#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-22 21:42:55
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

import os

# python 内置的排序算法 sorted()

a = [3, 2, -5, 6,  -75, 2, 7, -89, 234]
print('normal:', sorted(a))

# 通过key 关键字 可以实现自己的排序函数
print('abs:', sorted(a, key=abs))


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# 按名字排序：


def sort_by_name(L):
    return L[0]

# 再按成绩从高到低排序：


def sort_by_score(L):
    return -L[1]

L2 = sorted(L, key=sort_by_name)
print(L2)

L3 = sorted(L, key=sort_by_score)
print(L3)
