#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-20 13:55:47
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

# 此文件要在命令行打开

import time
import sys

f = None
fimeName = 'file/poem.txt'
try:
    f = open(fimeName, 'r')
    while True:
        line = f.readline()
        if(len(line) == 0):
            break
        print(line)
        sys.stdout.flush()
        print('press ctrl c to crash this progress.')
        time.sleep(2)
        pass
except KeyboardInterrupt as e:
    print('you can not cancered reading file!!!')
finally:
    if f:
        f.close()
        print('finally close the file.')
