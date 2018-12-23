#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-22 22:20:32
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

import os


def createCounter2():
    fn = [0]

    def counter():
        fn[0] = fn[0] + 1
        return fn[0]
    return counter

# 闭包引用的外部变量如果是不可变的，且需要在返回的函数中修改，
# 则要在函数中用nonlocal声明。


def createCounter():
    x = 0

    def counter():
        nonlocal x
        x = x + 1
        return x
    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
