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
from datautils import rootdatas, fileutils
from sklearn.datasets.base import Bunch
import pickle

rootPath = rootdatas.getDataPath() + os.sep
bagPath = rootPath + 'train_word_bag'
bagFileName = 'train_set.dat'
bagFile = bagPath + os.sep + bagFileName
corpusSegPath = rootPath + 'train_corpus_seg'

if not os.path.exists(bagPath):
    os.mkdir(bagPath)

if os.path.exists(bagFile):
    os.remove(bagFile)
    print(bagFile, ' exist, so delete it.')

print(Bunch)
bunch = Bunch(target_name=[], lable=[], filenames=[], contents=[])
bunch.target_name = corpusSegPath

for segDir in os.listdir(corpusSegPath):
    segDirPath = corpusSegPath + os.sep + segDir

    for segFile in os.listdir(segDirPath):
        fullName = segDirPath + os.sep + segFile
        content = fileutils.readFile(fullName).strip()
        content = ''.join(content.split())

        bunch.filenames.append(fullName)
        bunch.lable.append(segDir)
        bunch.contents.append(content)

# bunch is a_pyplot object, so it need to be saved in byte format.
fileToSave = open(bagFile, 'wb')
pickle.dump(bunch, fileToSave)
fileToSave.close()

# load in byte format too.
fileToOpen = open(bagFile, 'rb')
bunch2 = pickle.load(fileToOpen)
fileToOpen.close()
print(bunch2)
