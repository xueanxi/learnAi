#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-20 15:02:39
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

import os
import platform

# 判断当前的操作系统
isWindowsPlatform = platform.platform().startswith('Windows')
if isWindowsPlatform:
    print('current is Windows')
else:
    print('current is not Windows')


print('current platform is ', platform.platform())
