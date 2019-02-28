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
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

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
bugDataPath = root + 'news' + os.sep + "bug"
segPath = root + 'news' + os.sep + "seg"
bugRawPath = segPath +os.sep+"bugRaw.dat"
bunch = Bunch(target_name=[], lable=[], filenames=[], contents=[])
bunch.target_name = segPath
myHandler = MyHandler()
myHandler.setBanch(bunch)

for file in os.listdir(bugDataPath):
    filePath = bugDataPath + os.sep + file
    if os.path.isdir(filePath):
        print(file, ' is dir. continue')
        continue
    with open(filePath, 'r') as file:
        text = file.read()
        text = re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f|&]+", u"", text)
        root = sax.parseString(string=text, handler=myHandler)
        print('finish bug file:',filePath)
fileutils.saveBatchObj(bugRawPath, bunch)


# 1.improt bugRaw.dat
# train data path:/rootdata/news/seg/bugRaw.dat
rootPath = fileutils.getDataPath() + os.sep
dataFolder = rootPath + os.sep + 'news' + os.sep + 'seg' + os.sep
bugRawFile = dataFolder + 'bugRaw.dat'
bugRaw = fileutils.readBatchObj(bugRawFile)

# 2.get stop words
stopWordFolderPath = rootPath + 'train_corpus_stop_word'
stopWordFileName = 'corpus_stop_word_china.txt'
stopWordFilePath = stopWordFolderPath + os.sep + stopWordFileName
stopWordList = []
with open(stopWordFilePath, 'r') as stopWordFile:
    stopWordList = stopWordFile.read().splitlines()

#========================== 开始创建训练集词向量空间 ==========================
corpus = [
     'This is the first document.',
     'This document is the second document.',
     'And this is the third one.',
     'Is this the first document?',
]

# 3.构建词向量空间对象(训练)
tfidfSpace = Bunch(target_name=bugRaw.target_name, lable=bugRaw.lable,
                   filenames=bugRaw.filenames, tdm=[], vocabulary=[])
# 4.使用 TfidfVectorizer 初始化向量空间模型(训练)
vectorizer = TfidfVectorizer(stop_words=['and'], sublinear_tf=True, max_df=0.5)
sparse_result = vectorizer.fit_transform(corpus)
print('vocabulary',vectorizer.vocabulary_)
print('result',sparse_result)
print(sparse_result.todense())




