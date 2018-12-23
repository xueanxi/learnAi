#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-27 21:26:28
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

import os


class Student():

    def __init__(self, name, score, grade):
        self.name = name
        self.__score = score  # 两个下滑线，定义成了私有变量，外部不能访问
        self._grade = grade  # 一个下滑线，其实也是定义成了私有变量，但是外部是可以访问的，它定义只是告诉使用者，这个是一个私有变量最好不要直接访问

    def print_student(self):
        print("student name is {}, score is {}, grade is".format(
            self.name, self.__score, self._grade))


aaa = Student('aaa', 69, 1)

aaa.print_student()

print("aaa name is {}".format(aaa.name))
# print("aaa score is {}".format(aaa.__score))# __score定义成了私有变量，外部不能访问
print("aaa grade is {}".format(aaa._grade))  # _ 可以访问，但是不建议访问
# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
# 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
# 所以，仍然可以通过_Student__name来访问__name变量：
print("aaa grade is {}".format(aaa._Student__score))
