#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-21 23:36:45
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

import os

# Iterator 迭代器
from collections import Iterator
from collections import Iterable


def getGeneration():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3
    return 'done'


# Iterable对象，可以通过for循环迭代，但是不能使用next方法，获取下一个值
l1 = [1, 2, 3]  # list
l2 = {'1': 3, '2': 5, '3': 77}  # dict
l3 = 1, 2, 3  # tuple
l4 = 'strings'  # string
l5 = {'1', '4', '6', '4'}  # set
l6 = getGeneration()  # Iterator对象
print('l1 :', isinstance(l1, Iterable))
print('l2 :', isinstance(l2, Iterable))
print('l3 :', isinstance(l3, Iterable))
print('l4 :', isinstance(l4, Iterable))
print('l5 :', isinstance(l5, Iterable))
print('l6 :', isinstance(l6, Iterable))


print('=============================')
# next(l1)
# generation是 Iterator对象，可以通过for循环迭代，也可以通过next方法获取下一个值，
print('l1 :', isinstance(l1, Iterator))
print('l2 :', isinstance(l2, Iterator))
print('l3 :', isinstance(l3, Iterator))
print('l4 :', isinstance(l4, Iterator))
print('l5 :', isinstance(l5, Iterator))
print('l6 :', isinstance(l6, Iterator))

print('=============================')
# Iterable 对象也可以转化为 Iterator对象,调用next函数
print('l1 :', isinstance(iter(l1), Iterator))
print('l2 :', isinstance(iter(l2), Iterator))
print('l3 :', isinstance(iter(l3), Iterator))
print('l4 :', isinstance(iter(l4), Iterator))
print('l5 :', isinstance(iter(l5), Iterator))
