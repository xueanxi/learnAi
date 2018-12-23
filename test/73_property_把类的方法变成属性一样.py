#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-30 11:08:33
# @Author  : anxi.xue (xueanxi@163.com)

import os


class Student():

    def __init__(self, name):
        self.name = name
        self._score = 0

    @property
    def score(self):  # 加上 @property 装饰器，就把score方法，变成了一个属性
        return self._score

    @score.setter  # 加上这个标签，实例可以通过 bob.score = 60 这样给方法赋值
    def score(self, score):
        if score < 101 and score > 0:
            self._score = score
        else:
            raise 'score must be 0~100'

bob = Student('bob')
print("1: {} s score is {}".format(bob.name, bob.score))
print("2: {} s score is {}".format(bob.name, bob._score))


bob.score = 60
print("3: {} s score is {}".format(bob.name, bob.score))
# bob.score = 1000#这里会报错   'score must be 0~100'


# 作业题 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：

class Screen():

    def __init__(self):
        self._width = 0
        self._height = 0
        self._resolution = 0

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        return self._height * self._width


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
