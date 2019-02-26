#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-10 09:38:22
# @Author  : anxi.xue (xueanxi@163.com)
# @Link    : ${link}
# @Version : $Id$

import os
import sys
sys.path.append('..')
from datautils import fileutils
import pandas as pd
import numpy as np
from xml import sax
import re
from sklearn.datasets.base import Bunch
import jieba

#把训练集和测试集的数据保存到Bunch对象中

class MyHandler(sax.ContentHandler):

    def __init__(self):
        self.lable = []
        pass

    def startElement(self, tag, attributes):
        self.CurrentData = tag

    def endElement(self, tag):
        self.CurrentData = ""

    def startDocument(self):
        print('startDocument')
        pass

    def characters(self, content):
        if self.CurrentData == "url":
            content = content.replace(' ', '')
            list = content.split('http://')
            if(len(list) == 2):
                list = list[1].split('.sohu')
                self.bunch.lable.append(list[0])
                if list[0] not in self.lable:
                    self.lable.append(list[0])

        elif self.CurrentData == "contenttitle":
            self.bunch.filenames.append(filePath)

        elif self.CurrentData == "content":
            if(len(content) > 0):
                seg = jieba.cut(content, cut_all=False)
                self.bunch.contents.append(' '.join(seg))

    def getBanch(self):
        return self.bunch

    def setBanch(self, bunch):
        self.bunch = bunch

    def printlable(self):
        print(self.lable)


root = fileutils.getDataPath() + os.sep
trainDataPath = root + 'news' + os.sep + "train"
testDataPath = root + 'news' + os.sep + "test"
segPath = root + 'news' + os.sep + "seg"
trainRawPath = segPath +os.sep+"trainRaw.dat"
testRawPath = segPath +os.sep+"testRaw.dat"
bunch = Bunch(target_name=[], lable=[], filenames=[], contents=[])
bunch.target_name = segPath

myHandler = MyHandler()
myHandler.setBanch(bunch)

# parser all train data and save it to bunch
for file in os.listdir(trainDataPath):
    filePath = trainDataPath + os.sep + file
    if os.path.isdir(filePath):
        print(file, ' is dir. continue')
        continue
    with open(filePath, 'r') as file:
        text = file.read()
        text = re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f|&]+", u"", text)
        root = sax.parseString(string=text, handler=myHandler)
        print('finish train file:',filePath)
fileutils.saveBatchObj(trainRawPath, bunch)

# parser all test data and save it to bunch
bunch.lable=[]
bunch.filenames=[]
bunch.contents=[]

for file in os.listdir(testDataPath):
    filePath = testDataPath + os.sep + file
    if os.path.isdir(filePath):
        print(file, ' is dir. continue')
        continue
    with open(filePath, 'r') as file:
        text = file.read()
        text = re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f|&]+", u"", text)
        root = sax.parseString(string=text, handler=myHandler)
        print('finish test file:',filePath)
fileutils.saveBatchObj(testRawPath, bunch)
