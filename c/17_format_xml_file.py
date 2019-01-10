#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-10 11:48:03
# @Author  : anxi.xue (xueanxi@163.com)
# @Link    : ${link}
# @Version : $Id$


import os
import sys
sys.path.append('..')
from datautils import fileutils

root = fileutils.getDataPath() + os.sep
folderPath = root + 'news' + os.sep + "train"
for file in os.listdir(folderPath):
    filePath = folderPath + os.sep + file
    with open(filePath, 'r+') as fp:
        content = fp.read()
        fp.seek(0, 0)
        fp.write('<start>\n' + content + '\n</start>')
