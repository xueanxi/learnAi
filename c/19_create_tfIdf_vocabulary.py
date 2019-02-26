#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-02 15:51:06
# @Author  : anxi.xue (xueanxi@163.com)
# @Link    : ${link}
# @Version : $Id$


import os
import sys

sys.path.append('..')
from datautils import fileutils
from sklearn.datasets.base import Bunch
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

# 1.improt trainRaw.dat
# train data path:/rootdata/news/seg/trainRaw.dat
# test data path:/rootdata/news/seg/testRaw.dat
rootPath = fileutils.getDataPath() + os.sep
dataFolder = rootPath + os.sep + 'news' + os.sep + 'seg' + os.sep
trainRawFile = dataFolder + 'trainRaw.dat'
testRawFile = dataFolder + 'testRaw.dat'
trainRaw = fileutils.readBatchObj(trainRawFile)
testRaw = fileutils.readBatchObj(testRawFile)

# 2.get stop words
stopWordFolderPath = rootPath + 'train_corpus_stop_word'
stopWordFileName = 'corpus_stop_word_china.txt'
stopWordFilePath = stopWordFolderPath + os.sep + stopWordFileName
stopWordList = []
with open(stopWordFilePath, 'r') as stopWordFile:
    stopWordList = stopWordFile.read().splitlines()

#========================== 开始创建训练集词向量空间 ==========================
# 3.构建词向量空间对象(训练)
tfidfSpace = Bunch(target_name=trainRaw.target_name, lable=trainRaw.lable,
                   filenames=trainRaw.filenames, tdm=[], vocabulary=[])
# 4.使用 TfidfVectorizer 初始化向量空间模型(训练)
vectorizer = TfidfVectorizer(stop_words=stopWordList, sublinear_tf=True, max_df=0.5)
transformer = TfidfTransformer()#该类会统计每个词的TF-IDF值

# 5.文本保存为词频矩阵，单独保存字典文件(训练)
tfidfSpace.tdm = vectorizer.fit_transform(trainRaw.contents)
tfidfSpace.vocabulary = vectorizer.vocabulary_

# 6.save tfidfSpace(训练)
# /rootdata/news/seg/trainVocabulary.dat
vocabularyPath = dataFolder + 'trainVocabulary.dat'
fileutils.saveBatchObj(vocabularyPath, tfidfSpace)

#========================== 开始创建测试集词向量空间 ==========================
# 7.构建词向量空间对象(测试)
tfidfSpace = Bunch(target_name=testRaw.target_name, lable=testRaw.lable,
                   filenames=testRaw.filenames, tdm=[], vocabulary=[])
# 4.使用 TfidfVectorizer 初始化向量空间模型(测试)
vectorizer = TfidfVectorizer(stop_words=stopWordList, sublinear_tf=True, max_df=0.5)
transformer = TfidfTransformer()#该类会统计每个词的TF-IDF值

# 5.文本保存为词频矩阵，单独保存字典文件(测试)
tfidfSpace.tdm = vectorizer.fit_transform(testRaw.contents)
tfidfSpace.vocabulary = vectorizer.vocabulary_

# 6.save tfidfSpace(测试)
# /rootdata/news/seg/testVocabulary.dat
vocabularyPath = dataFolder + 'testVocabulary.dat'
fileutils.saveBatchObj(vocabularyPath, tfidfSpace)
