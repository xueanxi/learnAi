#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-02 14:54:03
# @Author  : anxi.xue (xueanxi@163.com)
# @Link    : ${link}
# @Version : $Id$

import os
import sys
sys.path.append('..')
from datautils import fileutils

rootPath = fileutils.getDataPath() + os.sep
stopWordFolder = 'train_corpus_stop_word'
stopWordFolderPath = rootPath + stopWordFolder
stopWordFileName = 'corpus_stop_word_china.txt'
stopWordFilePath = stopWordFolderPath + os.sep + stopWordFileName
print('stopWordFilePath:', stopWordFilePath)

with open(stopWordFilePath, 'r') as file:
    lines = file.readlines()
    for word in lines:
        word = word.strip()
        print('stop word:', word)
