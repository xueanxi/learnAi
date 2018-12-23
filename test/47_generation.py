#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-21 23:06:01
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

import os

# generation 生成器，每调用一次 next(),会从上次 yield 关键字中断的地方，继续执行。
# 而不会一次性把整个函数执行完，这个使用于数据十分庞大的时候。

# generation 可以看做容量无线的数据，而list的容量是有限的


def getGeneration():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3
    return 'done'

g = getGeneration()
print('next = ', next(g))
print('next = ', next(g))
print('next = ', next(g))
# print('next = ', next(g))
# print('next = ', next(g))

# 这里执行next(g)次数超过了函数的 yield的时候，会报错
# 如果想要获得最后的返回值，可以通过捕获异常来的到

g2 = getGeneration()
try:
    print('next = ', next(g2))
    print('next = ', next(g2))
    print('next = ', next(g2))
    print('next = ', next(g2))
    print('next = ', next(g2))
except StopIteration as e:
    print('return values is:', e.value)


# 一直使用next() 来获取generation是很笨的，
# 可以通过for循环来获得，for循环会自动调用next函数
g3 = getGeneration()
for item in getGeneration():
    print('for :', item)

# L = [1]
# print('L : ', L)
# L.append(0)
# print('L2 :', L)

# 杨辉三角


def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[x - 1] + L[x] for x in range(len(L))]


n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
