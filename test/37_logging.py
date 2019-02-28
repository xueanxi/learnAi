#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-20 14:28:18
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

import os
import platform
import logging

# 获得当前文件的路径
currentFilePath = os.getcwd()
print('currentFilePath is ', currentFilePath)
# 获得当前文件的父路径
parentPath = os.path.abspath(os.path.dirname(currentFilePath) + os.sep + '.')
print('parentPaht = ', parentPath)
# 获得当前文件的父路径的父路径
parentPath2 = os.path.abspath(os.path.dirname(currentFilePath) + os.sep + '..')
print('parentPath2 = ', parentPath2)
# 三个点，不是三重父路径，而是和一个点一样
parentPath3 = os.path.abspath(
    os.path.dirname(currentFilePath) + os.sep + '...')
print('parentPath3 = ', parentPath3)

# 创建log路径
logfileName = 'log.txt'
logFolderNme = 'log'
logFolderPath = os.path.join(currentFilePath, logFolderNme)
print('logfolder path:', logFolderPath)
if os.path.exists(logFolderPath):
    print('log folder is exist, not should create.')
else:
    print('create log folder...')
    os.mkdir(logFolderPath)

# 指定Log文件
# os.path.join()方法可以把你输入的路径拼成当前操作系统可用的路径
logfilePath = os.path.join(currentFilePath, logFolderNme, logfileName)
print('log file: ', logfilePath)

# 配置log信息
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    filename=logfilePath,
                    filemode='a')  # a是追加模式，w是写入

logging.debug('start logging ...')
logging.warning('logging warning ...')
logging.error('logging error ...')
