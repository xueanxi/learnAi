#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-10 17:39:29
# @Author  : anxi.xue (xueanxi@163.com)
# @Link    : ${link}
# @Version : $Id$

import os
import sys

sys.path.append('..')
from datautils import fileutils
from sklearn.naive_bayes import MultinomialNB

# 导入测试集的数据
# /rootdata/news/test
root = fileutils.getDataPath() + os.sep
dataFolder = root + 'news' +os.sep + 'seg' + os.sep
testVocabularyPath = dataFolder + "testVocabulary.dat"
trainVocabularyPath = dataFolder + "trainVocabulary.dat"
stopWordFilePath = root+'train_corpus_stop_word'+os.sep+'corpus_stop_word_china.txt'
testSet = fileutils.readBatchObj(testVocabularyPath)
trainSet = fileutils.readBatchObj(trainVocabularyPath)



# 8.使用贝叶斯分类
clf = MultinomialNB(alpha=0.001)
clf.fit(trainSet.tdm,trainSet.lable)

# 9.预测分类结果
predicted = clf.predict(testSet.tdm)
print('testSet.lable:',len(testSet.lable))
print('testSet.filenames:',len(testSet.filenames))
print('predicted:',len(predicted))


total = len(predicted)
rate = 0
#print('predicted',predicted)
# for index in range(0,len(predicted)):
#     if testSet.lable[index] != predicted[index]:
#         # print('实际类别:', testSet.lable[index], ' 预测类别:', predicted[index])
#         rate += 1
for (flable,filename,except_cate) in zip(testSet.lable,testSet.filenames,predicted):
    if flable != except_cate:
        rate+=1
        print('实际类别:',flable,' 预测类别:',except_cate)

# 10. 精度
print('error_rate:',(float(rate)*100/float(total)),'%', 'error num:',rate,' right num:',(total-rate))

