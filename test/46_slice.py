#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-21 21:33:12
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

import os

a = ['a', 'b', 'c', 'd', 'e', 'f']

print(a[0:3])
print(a[:])
print(a[-1:])
print(a[-1:2])

l = list(range(100))
print(l[:10])  # 前10个数
print(l[-10:])  # 后10个数
print(l[:10:2])  # 前10个数，步长2


# 实例化元组 tuple
t1 = tuple([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
t2 = tuple([1, 2, 3])
# t = tuple(1, 2, 3, 4, 5, 6, 7, 8, 9) # tuple的参数只能有一个，所以不能这样实例化
print('\nt1:', t1)
print('t2:', t2)

list = range(8)
for i in list:
    print('range:', i)


def removeblank(strings):
    firstBlankIndex = 0  # 从前往后看，第一个非空格的索引
    lastBlankIndex = 0  # 从后往前看，第一个非空格的索引
    lenght = len(strings)

    i = 0
    while(i < lenght - 1):
        if strings[i] != ' ':
            firstBlankIndex = i
            break
        i += 1

    j = lenght - 1
    while(j > -1):
        if strings[j] != ' ':
            lastBlankIndex = j
            break
        j -= 1

    if firstBlankIndex == lenght - 1:
        return ''
    elif lastBlankIndex == 0:
        return ''
    else:
        return strings[firstBlankIndex:lastBlankIndex + 1]

s1 = ('    afadsf    asfwef    ')
s2 = ('        ')
s3 = ('   sdfas')
print('result1:====' + removeblank(s1) + '=======')
print('result2:====' + removeblank(s2) + '=======')
print('result3:====' + removeblank(s3) + '=======')
