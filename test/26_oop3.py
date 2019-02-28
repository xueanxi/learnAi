#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-19 23:22:45
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

import os


class person:
    """
    I am a people
    """

    # 类变量,使用双下滑线，定义一个私有变量，外部不能访问
    __number = 0

    def __init__(self, name):
        self.name = name
        person.__number += 1
        print("my name is ", self.name)

    def die(self):
        person.__number -= 1

    def sayHi(self):
        """
        i am a method
        """
        print("Hi I am ", self.name)

        # 类方法
    @classmethod
    def showAll(cls):
        print("now there are {} perpon".format(person.__number))

print(person.__doc__)
p1 = person('p1')
p1.sayHi()
#print("current has {} person".format(p1.__number))
#print("current has {} person".format(person.__number))

p2 = person('p2')
p2.sayHi()
p1.die()
p1.showAll()  # 对象也可以调用静态方法
p2.die()
person.showAll()  # 类本身也可以调用静态方法
print(person.sayHi.__doc__)
