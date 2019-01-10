#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-10 17:31:07
# @Author  : anxi.xue (xueanxi@163.com)
# @Link    : ${link}
# @Version : $Id$

import os
import sys
sys.path.append('..')
from datautils import fileutils
from sklearn.datasets.base import Bunch
from xml import sax
import re


class MyHandler(sax.ContentHandler):

    def __init__(self):
        self.lables = []
        self.lable = ''
        self.content = ''
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
                self.lable = list[0]
                if list[0] not in self.lables:
                    self.lables.append(list[0])
                    folderPath = newsTestFolder + os.sep + list[0]
                    if not os.path.exists(folderPath):
                        os.mkdir(folderPath)

        elif self.CurrentData == "contenttitle":
            self.content = content

        elif self.CurrentData == "content":
            self.content = self.content + ' ' + content
            self.datas.append(self.lable + 'xueANxi' + self.content)

    def setDatas(self, datas):
        self.datas = datas

root = fileutils.getDataPath() + os.sep
newsTestFolder = root + 'news' + os.sep + "test"
newsTrainFolder = root + 'news' + os.sep + "train"
newsSegFolder = root + 'news' + os.sep + "seg"
newsTestSegFile = newsSegFolder + os.sep + 'testSpace.dat'

myHandler = MyHandler()
datas = []
myHandler.setDatas(datas)

# delete all folder
for file in os.listdir(newsTestFolder):
    filePath = newsTestFolder + os.sep + file
    if os.path.isdir(filePath):
        fileutils.removeFolder(filePath)

# parser all test news
for file in os.listdir(newsTestFolder):
    filePath = newsTestFolder + os.sep + file
    if os.path.isdir(filePath):
        print(file, ' is dir. continue')
        continue
    with open(filePath, 'r') as file:
        text = file.read()
        text = re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f|&]+", u"", text)
        root = sax.parseString(string=text, handler=myHandler)

# split test file to folder separately
for data in datas:
    lable = data.split('xueANxi')[0]
    content = data.split('xueANxi')[1]
    segFolder = newsTestFolder + os.sep + lable
    num = len(os.listdir(segFolder))
    filePath = segFolder + os.sep + str(num) + '.txt'
    fileutils.saveFile(filePath, content)

bunch = Bunch(target_name=[], lable=[], filenames=[], contents=[])
bunch.target_name = newsSegFolder

# save test data to file
for data in datas:
    lable = data.split('xueANxi')[0]
    content = data.split('xueANxi')[1]
    segFolder = newsTestFolder + os.sep + lable
    filePath = segFolder + os.sep + str(num) + '.txt'
    bunch.filenames.append(filePath)
    bunch.lable.append(lable)
    bunch.contents.append(content)

fileutils.saveBatchObj(newsTestSegFile, bunch)
