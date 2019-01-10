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


class MyHandler(sax.ContentHandler):

    def __init__(self):
        self.url = ''
        self.titletle = ''
        self.content = ''
        self.line = ''
        self.alldata = []

       # 元素开始事件处理
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "doc":
            self.line = ''

           # 元素结束事件处理
    def endElement(self, tag):
        self.CurrentData = ""

    def startDocument(self):
        self.alldata = []
        print('clear alldata')

   # 内容事件处理
    def characters(self, content):
        if self.CurrentData == "url":
            content = content.replace(' ', '')
            list = content.split('http://')
            if(len(list) == 2):
                list = list[1].split('.sohu')
                self.line = (list[0])
        elif self.CurrentData == "contenttitle":
            self.line = self.line + ' ' + content
        elif self.CurrentData == "content":
            self.line = self.line + ' ' + content
            self.alldata.append(self.line)

    def getData(self):
        return self.alldata


root = fileutils.getDataPath() + os.sep
folderPath = root + 'news' + os.sep + "train"
bunch = Bunch(target_name=[], lable=[], filenames=[], contents=[])
bunch.target_name = folderPath + os.sep + 'seg'

myHandler = MyHandler()
for file in os.listdir(folderPath):
    filePath = folderPath + os.sep + file
    with open(filePath, 'r') as file:
        text = file.read()
        text = re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f|&]+", u"", text)
        root = sax.parseString(string=text, handler=myHandler)
        bunch.
        list = myHandler.getData()
        print('finish file:', file)
