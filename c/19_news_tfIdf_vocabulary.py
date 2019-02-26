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
# train folder path:/rootdata/news/seg/news_train.dat
rootPath = fileutils.getDataPath() + os.sep
trainDataFile = rootPath + os.sep +'news'+os.sep+'seg'+os.sep+'news_train.dat'
trainBunch = fileutils.readBatchObj(trainDataFile)

# 2.get stop words
stopWordFolderPath = rootPath + 'train_corpus_stop_word'
stopWordFileName = 'corpus_stop_word_china.txt'
stopWordFilePath = stopWordFolderPath + os.sep + stopWordFileName
stopWordList = []
with open(stopWordFilePath, 'r') as stopWordFile:
    stopWordList = stopWordFile.read().splitlines()

# 3.build TF-IDF vector space
tfidfSpace = Bunch(target_name=trainBunch.target_name, lable=trainBunch.lable,
                   filenames=trainBunch.filenames, tdm=[], vocabulary=[])
vectorizer = TfidfVectorizer(
    stop_words=stopWordList, sublinear_tf=True, max_df=0.5)
transformer = TfidfTransformer()

tfidfSpace.tdm = vectorizer.fit_transform(trainBunch.contents)
# print('tdm:', tfidfSpace.tdm)
tfidfSpace.vocabulary = vectorizer.vocabulary_
# print('tfidfSpace:', tfidfSpace)

# 3.save tfidfSpace
vocabularyFolderPath = rootPath + 'news' + os.sep + 'seg'
vocabularyFileName = 'tfidfSpace.dat'
vocabularyPath = vocabularyFolderPath + os.sep + vocabularyFileName
fileutils.saveBatchObj(vocabularyPath, tfidfSpace)


