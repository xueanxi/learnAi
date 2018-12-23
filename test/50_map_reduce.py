#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-22 12:06:01
# @Author  : anxi.xue (xueanxi@163.com)


from functools import reduce

# 函数式的使用 map 和 reduce 函数


def multip2(number):
    return 2 * number


def add(number1, number2):
    return number1 + number2

# map 可以对第二个参数传入的东西，进行第一个函数的操作，比如下面的例子，所有都乘以2
# map 返回的是一个Iterator，是一个惰性的数列，需要用list(),转化一下。
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = list(map(multip2, list1))
print('map result = ', list2)

# reduce（f,[x,y,z]） 传入两个参数，参数形式和map一致。
# f(f(f(1,2),3),4)...
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('reduce result = ', reduce(add, list3))


# 作业
list5 = [1, 2, 3]


def muti(number1, number2):
    return number1 * number2


def prod(L):
    return reduce(muti, L)
print('prod:', prod(list5))

# 作业
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
DIGITS = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
          '6': 6, '7': 7, '8': 8, '9': 9, '0': 0, '.': '.'}

# 貌似没算对


def str2float(strings):
    def str2int(strs):
        if strs in DIGITS.keys():
            return DIGITS[strs]

    def sum2(number1, number2):
        return number1 * 10 + number2

    stringLength = len(strings)
    pointIndex = strings.find('.')

    list6 = list(map(str2int, strings))
    list6.pop(pointIndex)
    result = reduce(sum2, list6) * (10 ^ -(stringLength - pointIndex - 1))
    return result

print('str2float = ', str2float('123.456'))
