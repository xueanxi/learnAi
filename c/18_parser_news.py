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


class MyHandler(sax.ContentHandler):

    def __init__(self):
        self.lable = []
        pass

       # 元素开始事件处理
    def startElement(self, tag, attributes):
        self.CurrentData = tag

        # 元素结束事件处理
    def endElement(self, tag):
        self.CurrentData = ""

    def startDocument(self):
        print('startDocument')
        pass

   # 内容事件处理
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
# newsTrainPath = root + 'news' + os.sep + "train"
newsTrainPath = root + 'news' + os.sep + "test"
newsSegPath = root + 'news' + os.sep + "seg"
bunch = Bunch(target_name=[], lable=[], filenames=[], contents=[])
bunch.target_name = newsSegPath

myHandler = MyHandler()
myHandler.setBanch(bunch)

# parser all test news
for file in os.listdir(newsTrainPath):
    filePath = newsTrainPath + os.sep + file
    if os.path.isdir(filePath):
        print(file, ' is dir. continue')
        continue
    with open(filePath, 'r') as file:
        text = file.read()
        text = re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f|&]+", u"", text)
        root = sax.parseString(string=text, handler=myHandler)

myHandler.printlable()
save bunch obj to file
newsSegBagFile = newsSegPath + os.sep + 'news.dat'
fileutils.saveBatchObj(newsSegBagFile, bunch)
