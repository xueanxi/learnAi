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
trainDataPath = root + 'news' + os.sep + "train"
testDataPath = root + 'news' + os.sep + "test"

def addStartEndTagForData(folderPath):
    for file in os.listdir(folderPath):
        filePath = folderPath + os.sep + file
        if os.path.isdir(filePath):
            continue
        with open(filePath, 'r+') as fp:
            content = fp.read()
            fp.seek(0, 0)
            if not content.startswith('<start>'):
                if not content.startswith('</start>'):
                    fp.write('<start>\n' + content + '\n</start>')

#将原素材进行转码
fileutils.encodeUtf8ForFolder(trainDataPath)
fileutils.encodeUtf8ForFolder(testDataPath)
#原素材没有开始和结束标签，不能使用xml解析，添加上标签
addStartEndTagForData(trainDataPath)
addStartEndTagForData(testDataPath)