#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-29 23:09:28
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

# 把jieba2.py 中保存的分词文件持久化保存到Bunch中

import os
import sys
sys.path.append('..')
import jieba
import shutil
from datautils import rootdatas
from sklearn.datasets.base import Bunch
import pickle


def saveFile(filePath, content):
    with open(filePath, 'wb') as file:
        file.write(content.encode(encoding='utf-8'))


def readFile(filePath):
    with open(filePath, 'rb') as file:
        content = file.read()
        return content


bag_file = 'train_set.dat'
rootPath = rootdatas.getDataPath() + os.sep
corpus_seg = rootPath + 'train_corpus_small'
train_word_bag_path = rootPath + os.sep + 'train_word_bag'
if not os.path.exists(train_word_bag_path):
    os.mkdir(train_word_bag_path)

if os.path.exists(train_word_bag_path + os.sep + bag_file):
    os.remove(train_word_bag_path + os.sep + bag_file)

print(Bunch)
bunch = Bunch(target_name=[], lable=[], filenames=[], contents=[])
bunch.target_name = corpus_seg

for segDir in os.listdir(corpus_seg):
    segDirPath = corpus_seg + os.sep + segDir

    for segFile in os.listdir(segDirPath):
        fullName = segDirPath + os.sep + segFile
        content = readFile(fullName).decode(encoding='utf-8').strip()
        content = ''.join(content.split())

        bunch.filenames.append(fullName)
        bunch.lable.append(segDirPath)
        bunch.contents.append(content)

print(bunch)
fileToSave = open(train_word_bag_path + os.sep + bag_file, 'wb')
pickle.dump(bunch, fileToSave)
fileToSave.close()

print('================================')


fileToOpen = open(train_word_bag_path + os.sep + bag_file, 'rb')
bunch2 = pickle.load(fileToOpen)
print(bunch2)
