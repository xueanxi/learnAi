#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-30 10:12:53
# @Author  : anxi.xue (xueanxi@163.com)

import os


class MyObject():

    def __init__(self):
        self.__name = 'default name'
        self.yearold = 18

    def getName(self):
        return self.__name

    def getYearold(self):
        return self.yearold

    def setName(self, name):
        self.name = name

    def setYearold(self, yearold):
        self.yearold = yearold

obj = MyObject()

print(dir(obj))  # 打印对象的所有方法

# print(obj.__name)#不能直接访问私有方法
print(obj.yearold)

print(getattr(obj, 'yearold'))
# print(getattr(obj, '__name'))#也不能使用反射获得私有方法

setattr(obj, 'yearold', 20)
print(obj.getYearold())
setattr(obj, '__name', 'tom')
print(obj.getName())  # 反射也不能设置私有变量的名字
