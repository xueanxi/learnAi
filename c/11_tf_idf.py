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
import pickle

# 1.improt train_set.dat
rootPath = fileutils.getDataPath() + os.sep
trainSetFolderPath = rootPath + 'train_word_bag'
trainSetFilePath = trainSetFolderPath + os.sep + 'train_set.dat'
trainSet = fileutils.readBatchObj(trainSetFilePath)

# 2.get stop words
stopWordFolderPath = rootPath + 'train_corpus_stop_word'
stopWordFileName = 'corpus_stop_word_china.txt'
stopWordFilePath = stopWordFolderPath + os.sep + stopWordFileName
stopWordFile = open(stopWordFilePath, 'r')
stopWordList = stopWordFile.read().splitlines()
# print('stopWordList,', stopWordList)
stopWordFile.close()

# 2.build TF-IDF vector space
tfidfSpace = Bunch(target_name=trainSet.target_name, lable=trainSet.lable,
                   filenames=trainSet.filenames, tdm=[], vocabulary=[])
vectorizer = TfidfVectorizer(
    stop_words=stopWordList, sublinear_tf=True, max_df=0.5)
transformer = TfidfTransformer()

tfidfSpace.tdm = vectorizer.fit_transform(trainSet.contents)
# print('tdm:', tfidfSpace.tdm)
tfidfSpace.vocabulary = vectorizer.vocabulary_
# print('tfidfSpace:', tfidfSpace)

# 3.save tfidfSpace
vocabularyFolderPath = rootPath + 'train_word_bag'
vocabularyFileName = 'tfidfSpace.dat'
vocabularyPath = vocabularyFolderPath + os.sep + vocabularyFileName
if os.path.exists(vocabularyPath):
    os.remove(vocabularyPath)
fileutils.saveBatchObj(vocabularyPath, tfidfSpace)
