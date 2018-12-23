#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-30 17:38:43
# @Author  : anxi.xue (xueanxi@163.com)

import os


class Student():

    def __init__(self, name):
        self.name = name

tom = Student('tom')
print('Student name is %s' % tom.name)
# print('Student socre is %s' % tom.socre)#由于没有score，这样执行就会报错
# 为了避免这样调用不存在的变量，可以shiyong __getattr__这个定制


class Student2():

    def __init__(self, name):
        self.name = name

    # 在没有找到变量的情况下，才会调用__getattr__，如果类中已经有了，则不会
    def __getattr__(self, attr):
        if attr == 'score':  # 变量
            return 99
        elif attr == 'age':  # 函数也可以，但是要用lambada
            return lambda: 25
        else:
            raise AttributeError('Student2 has not attr %s' % attr)

tim = Student2('tim')
print('Student name is %s' % tim.name)
print('Student socre is %s' % tim.score)
print('Student year is %s' % tim.age())
# print('Student year is %s' % tim.ssss)如果 __getattr__ 也找不到，可以在else里面处理
