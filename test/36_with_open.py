#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-20 14:07:18
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

# with open 打开文件会自动关闭，不用finally，但是没有finally那么有可操作性
import time
import sys

with open('file/poem.txt') as f:
    for line in f:
        print(line)
        print('dont press ctrl c when reading the file')
        time.sleep(2)
