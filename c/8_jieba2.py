#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-29 21:46:02
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

import os
import sys
sys.path.append('..')
import jieba
import shutil
from datautils import rootdatas


def saveFile(filePath, content):
    with open(filePath, 'wb') as file:
        file.write(content.encode(encoding='utf-8'))


def readFile(filePath):
    with open(filePath, 'rb') as file:
        content = file.read()
        return content

# 把分词语料库的文件全部进行分词

rootPath = rootdatas.getDataPath() + os.sep
corpus_raw = rootPath + 'train_corpus_small'
corpus_seg = rootPath + 'train_corpus_seg'
print('corpus_raw', corpus_raw)
print('corpus_seg', corpus_seg)

for rawDir in os.listdir(corpus_raw):
    print('rawDir:', rawDir)
    rawDirPath = corpus_raw + os.sep + rawDir
    segDirPath = corpus_seg + os.sep + rawDir
    if not os.path.exists(segDirPath):
        os.makedirs(segDirPath)
    else:
        shutil.rmtree(segDirPath)
        os.makedirs(segDirPath)
    for rawFile in os.listdir(rawDirPath):
        content = readFile(rawDirPath + os.sep +
                           rawFile).strip().decode(encoding='utf-8')
        content = ''.join(content.split())
        seg = jieba.cut(content, cut_all=False)
        segFile = segDirPath + os.sep + rawFile
        saveFile(segFile, ' '.join(seg))
