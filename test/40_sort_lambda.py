#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-20 18:35:25
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$


point1 = [{'x': 1, 'y': 4},
          {'x': 4, 'y': 2},
          {'x': 3, 'y': 7}]
print('point1 type',type(point1))
# 会报错
#point1.sort(key=lambda i: i['y'])
print('point1 after sort by y', point1)

point1.sort(key=lambda i: i['x'])
print('point1 after sort by x', point1)


point2 = [1, 5, 3, 4]
point2.sort()
print('point2 :', point2)
