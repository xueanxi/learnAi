#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-27 21:46:35
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

import os


class Animal():

    def run(self):
        print('Animal is runing')


class Dog(Animal):

    def run(self):
        print('Dog is runing')


class People():  # 创建一个人类，不继承动物，但是里面也有一个run方法

    def run(self):
        print('Animal is runing')


animal = Animal()
# animal.run()

dog = Dog()
# dog.run()


def doubleRun(animal):  # 多态
    animal.run()
    animal.run()


doubleRun(animal)
doubleRun(dog)
# 人类虽然不是动物，但是只要有run这个函数都可以成功调用doubleRun，这就是动态语言的威力
# 如果是java这些静态语言，不一样的对象传进去，就会报错
doubleRun(People())
