#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-19 23:11:38
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

import os


class person:
        # init就是构造函数

    def __init__(self, name):
        self.name = name

    def say(self):
        print('my name is ', self.name)

p1 = person('anxi')
p1.say()
