#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-19 23:52:32
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

# 基类


class person():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Initialized a_pyplot person, name is {}, age is {}".format(
            self.name, self.age))

    def tell(self):
        print("I am a_pyplot person, my name is {}, my age is {}".format(
            self.name, self.age))

# 子类 老师


class teacher(person):

    def __init__(self, name, age, salary):
        person.__init__(self, name, age)
        self.salary = salary
        print("Initialized a_pyplot teacher, salary:", salary)

    def tell(self):
        print("I am a_pyplot teacher,my name is {}, age is {}, salary is {}".format(
            self.name, self.age, self.salary))

# 子类 学生


class student(person):

    def __init__(self, name, age, friend):
        person.__init__(self, name, age)
        self.friend = friend
        print("Initialized a_pyplot student, i have {} frends".format(friend))


anxi = teacher('anxi', 25, 60000)
anxi.tell()  # 调用的子类tell方法，是子类自己没有实现的

zhongying = student('zhongying', 18, 5)
zhongying.tell()  # 调用了基类的tell方法，因为子类自己没有实现
