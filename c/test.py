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
