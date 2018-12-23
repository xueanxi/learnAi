#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-30 10:35:50
# @Author  : anxi.xue (xueanxi@163.com)

import os

#__slots__ 可以锁定一些属性不让实例访问,连初始化__init__里面都不允许初始化


class Student():

    def __init__(self):
        pass
    __slots__ = ['name', 'year']


class Student2():

    def __init__(self):
        self.name = 'no name'
        self.year = 0
        self.socre = 0
    __slots__ = ['name', 'year', 'score']


bob = Student()
bob.name = 'bob'
bob.year = 18
# bob.score = 100  # 这里会报错，不让绑定score，因为score没有写入__slots__
#print('instance bob: {}, {}, {}'.format(bob.name, bob.year, bob.score))
