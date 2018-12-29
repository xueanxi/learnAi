#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-29 18:41:32
# @Author  : anxi.xue (xueanxi@163.com)
# @Link    : ${link}
# @Version : $Id$

import os
import jieba
import sys


seg_list = jieba.cut("小明1995年毕业于北京清华大学", cut_all=False)
print('type:', type(seg_list))

# seg_list 是一个迭代器
# 访问的方法1
# for seg in seg_list:
#     print('defult mode1:', seg)

# 访问的方法2
print('defult mode2:', " ".join(seg_list))

seg_list = jieba.cut("小明1995年毕业于北京清华大学", cut_all=True)
print('Full mode:', "/ ".join(seg_list))
