#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-30 10:47:08
# @Author  : anxi.xue (xueanxi@163.com)

from types import MethodType


class Student():

    def __init__(self, name):
        self.name = name
        self.score = 0


tom = Student('tom')
print("1: {} is {}".format(tom.name, tom.score))


def setScore(self, score):
    self.score = score

# 把setScore这个方法绑定给tom这个实例
tom.set_score = MethodType(setScore, tom)
tom.set_score(100)
print("2: {} is {}".format(tom.name, tom.score))

jerry = Student('jerry')
# jerry调用 set_score 会报错，因为set_score方法只绑定给了tom这个实例，
# jerry.set_score(100)
#print("3: {} is {}".format(jerry.name, jerry.score))

# 如果给一个类设绑定了一个方法，那么它产生的实例都可以调用这个方法了
# 给类绑定新方法，只有动态语言才有这种能力
Student.set_score = MethodType(setScore, Student)
lala = Student('lala')
lala.set_score(99)
print("4: {} is {}".format(lala.name, lala.score))
