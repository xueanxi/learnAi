#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-20 19:37:41
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

import os

list1 = ['aaa']
assert len(list1) > 0
print('list1 len >0')
list1.pop()


assert len(list1) > 0
print('list1 len <= 0')
