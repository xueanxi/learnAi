#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append('..')
import jieba
import shutil
from datautils import fileutils


# def saveFile(filePath, content):
#     with open(filePath, 'wb') as file:
#         file.write(content.encode(encoding='utf-8'))


# def readFile(filePath):
#     with open(filePath, 'rb') as file:
#         content = file.read()
#         return content

# targetFolder = 'testFolder'
# targetFile = 'test.dat'
# rootPath = rootdatas.getDataPath() + os.sep
# folderPath = rootPath + targetFolder
# if not os.path.exists(folderPath):
#     os.mkdir(folderPath)
# filePath = folderPath + os.sep + targetFile

# saveFile(filePath, 'testtstserslfjsajfajfdas')
# content = readFile(filePath)
# print('read content:', content)

s = 'http://house.sohu.com/ bjesf/  sale/84294750.html'
print('0:', s.replace(' ', ''))
list = s.split('http://')
if(len(list) == 2):
    list = list[1].split('.sohu')
    print('4:', list[0])
