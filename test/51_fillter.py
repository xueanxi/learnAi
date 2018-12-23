#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-22 19:46:44
# @Author  : anxi.xue (xueanxi@163.com)

import os
# filter的作用和map一样，也作用于数列中的每一个数，然后通过传入函数判断，是否保留这个数。

# 用filter求素
# 计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
# 首先，列出从2开始的所有自然数，构造一个序列：
# 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
# 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
# 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
# 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 不断筛下去，就可以得到所有的素数。

# prime 就是 素数，概念，自能被一和自身整除的数


def getOdd():
    n = 1
    while True:
        n = n + 2
        yield n


def not_divisible(n):
    return lambda x: x % n > 0

# 不能被 3 整除的数列
# a = list(filter(not_divisible(3), [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]))
# print(a)


def getPrime():
    yield 2
    it = getOdd()
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible(n), it)

# lists = getPrime()
# for x in range(300):
#     n = next(lists)
#     print(n)

# 惰性数列可以通过for 循环达到next()的效果
for i in getPrime():
    if i < 1000:
        print(i)
    else:
        break

print('len', len(str(100)))


def is_palindrome(n):
    L = str(n)
    calculaTime = len(L) // 2  # calculaTime为进行循环的次数
    for i in range(calculaTime):
        if L[i] != L[-1 - i]:
            return False
    return True

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
