#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-30 18:04:35
# @Author  : anxi.xue (xueanxi@163.com)

import os


class Student():

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student Object name is %s' % self.name

tom = Student('tom')
print(tom)

# tom()  #实例是不可以加括号直接调用的，如果要实现，需要加上__call__


class Student2():

    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('call : Student2 name %s' % self.name)

    def __str__(self):
        return 'Student2 Object name is %s' % self.name
tim = Student2('tim')
tim()  # 这样就可以像调用函数一样调用实例了

# 下面看看callable 判断传入的东西能否被调用
print(callable(int))
print(callable(tom))  # 因为没有实现 __call__方法，所以没法调用
print(callable(tim))
print(callable([1, 2, 3, 4, 5, 6]))
print(callable(max))
