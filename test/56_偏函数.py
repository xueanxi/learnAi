#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-24 22:59:05
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

import functools

# 偏函数的作用，当参数多的时候，用偏函数可以固定住其中几个参数，让函数变得简单
a = int('256')
print('a = ', a)

b = int('101011', base=2)  # 加上base，就是二进制
print('b = ', b)

# 上面使用偏函数可以写成，定义一个偏函数 int2()自动执行二进制
int2 = functools.partial(int, base=2)
c = int2('101011')
print('c = ', c)
# 当然偏函数也是可以传入参数的，继续当成以前的int()函数来使用
d = int2('101011', base=10)
print('d = ', d)

#=============下面测试 max()函数 =================
print('=============下面测试 max()函数 =================')
t = [1, 2, 3, 4, 5, 6, 7, 8]
e = max(*t)
print('e = ', e)

max10 = functools.partial(max, 10)
f = max10(*t)
print('f = ', f)

# 其实传入max()函数的是一个元组*t,
# 像max()偏函数这种参数不带名字的，偏函数中传进去一个10，其实是在元组中加了一个数字而已。
