#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-30 14:05:24
# @Author  : anxi.xue (xueanxi@163.com)

import os


class A():

    def say(self):
        print('I am A')


class B():

    def say(self):
        print('I am B')


class C(B, A):
    pass

c = C()
c.say()  # 结果打印 I am B，先继承谁，就调用谁


#==================================

class D():

    def say(self):
        print('I am D')


class E(D):

    def say(self):
        print('I am E')


class F(D):

    def say(self):
        print('I am F')


class G(F, E):  # 结果打印 I am F，先继承谁，就调用谁
    pass

g = G()
g.say()
