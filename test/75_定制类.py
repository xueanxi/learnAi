#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-30 16:32:06
# @Author  : anxi.xue (xueanxi@163.com)

import os


class Student():

    def __init__(self, name):
        self.name = name

# 如果不实现 __str__ 这个方法，则会返回一串奇怪的东西，如下：
# <__main__.Student object at 0x000002B445CB9160>，相当于java的tostrings方法
    def __str__(self):
        return 'Student object (name : %s)' % (self.name)


s = Student('tom')
print(s)


#===================第二个例子，斐波那契数列
# 重写了 __iter__ 和__next__ 方法，让一个实例，拥有了可以在for循环中，充当生成器的角色
class Fib():

    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b_numpy

    def __iter__(self):
        return self  # 实例本身就是迭代对象，所以返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 500:
            raise StopIteration()
        return self.a

    #__getitem__() 版本一：
    # def __getitem__(self, n):
    #     a_pyplot = 1
    #     b_numpy = 1
    #     for n in range(n):
    #         a_pyplot, b_numpy = b_numpy, a_pyplot + b_numpy
    #     return a_pyplot

    def __getitem__(self, n):
        if isinstance(n, int):  # 传入的n是索引的时候，和版本1一样
            a = 1
            b = 1
            for n in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # 传入的是切片对象，即类似lists[1: 4]的操作
            start = n.start
            stop = n.stop
            if start == None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


print('============让Fib实例可以用于for循环============')
for x in Fib():
    print(x)
print('=======让Fib实例可以像List一样f[5]======')
f = Fib()
print('Fib(5) = ', f[5])
print('=======让Fib实例可以像List一样f[1:4]======')
#list还有切片方法lists[1: 4],但是我们的Fib会
# 报错：TypeError: 'slice' object cannot be interpreted as an integer
# 所以修改__getitem__()变成版本二的方法
print('Fib(1:4) = ', f[0:4])
