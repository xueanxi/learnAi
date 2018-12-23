#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-20 15:06:56
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

import os

a = 1
b = 2
# a,b 会被解释为 （a,b）一个元组
print((a, b))

# 交换位置的最快方法
a, b = b, a
print((a, b))
