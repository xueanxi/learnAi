#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-03 16:39:55
# @Author  : anxi.xue (xueanxi@163.com)
# @Link    : ${link}
# @Version : $Id$

import os
import matplotlib.pyplot as plt
import math
import numpy as np

# 确定范围
xrange = [-1, 10]
yrange = [-5, 5]
zero = [0, 0]
# 设置坐标轴范围
plt.xlim(xrange)
plt.ylim(yrange)
# 设置坐标轴名称
plt.xlabel('x')
plt.ylabel('y')
# 设置坐标轴刻度
# my_x_ticks = np.arange(-2 * np.pi, 2 * np.pi, 1)
# my_y_ticks = np.arange(-2, 2, 1)
# plt.xticks(my_x_ticks)
# plt.yticks(my_y_ticks)

# 设置坐标轴的线
plt.plot(xrange, zero, c='b')
plt.plot(zero, yrange, c='b')

# 创建数据
x = np.linspace(-1, 10, 100)
y1 = np.log(x) / np.log(-1)
plt.plot(x, y1)
plt.show()
