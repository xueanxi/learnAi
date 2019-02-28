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
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

#把训练集和测试集的数据保存到Bunch对象中

root = fileutils.getDataPath() + os.sep
trainDataPath = root + 'news' + os.sep + "train"
testDataPath = root + 'news' + os.sep + "test"
segPath = root + 'news' + os.sep + "seg"
trainRawPath = segPath +os.sep+"trainRaw.dat"
testRawPath = segPath +os.sep+"testRaw.dat"
bunch = Bunch(target_name=[], lable=[], filenames=[], contents=[])
bunch.target_name = segPath

contenttitle =''
# parser all train data and save it to bunch
for file in os.listdir(trainDataPath):
    filePath = trainDataPath + os.sep + file
    if os.path.isdir(filePath):
        print(file, ' is dir. continue')
        continue
    with open(filePath, 'r') as file:
        text = file.read()
        text = re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f|&]+", u"", text)
        root = ET.fromstring(text)
        for child in root:
            # 第二层节点的标签名称和属性,遍历xml文档的第三层
            for children in child:
                bunch.filenames.append(filePath)
                # 第三层节点的标签名称和属性
                if children.tag == 'url':
                    content = children.text
                    list = content.split('http://')
                    if (len(list) == 2):
                        list = list[1].split('.sohu')
                        bunch.lable.append(list[0])
                        if list[0] not in bunch.lable:
                            bunch.lable.append(list[0])
                elif children.tag == 'contenttitle':
                    contenttitle = children.text
                elif children.tag == 'content':
                    content = str(contenttitle)+' '+str(children.text)
                    if (len(content) > 0):
                        seg = jieba.cut(content, cut_all=False)
                        bunch.contents.append(' '.join(seg))
                    else:
                        bunch.contents.append('null')
        print('finish train file:',filePath)
fileutils.saveBatchObj(trainRawPath, bunch)

# parser all test data and save it to bunch
bunch.lable=[]
bunch.filenames=[]
bunch.contents=[]
contenttitle =''
for file in os.listdir(testDataPath):
    filePath = testDataPath + os.sep + file
    if os.path.isdir(filePath):
        print(file, ' is dir. continue')
        continue
    with open(filePath, 'r') as file:
        text = file.read()
        text = re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f|&]+", u"", text)
        root = ET.fromstring(text)
        for child in root:
            # 第二层节点的标签名称和属性,遍历xml文档的第三层
            for children in child:
                # 第三层节点的标签名称和属性
                bunch.filenames.append(filePath)
                if children.tag == 'url':
                    content = children.text.replace(' ', '')
                    list = content.split('http://')
                    if (len(list) == 2):
                        list = list[1].split('.sohu')
                        bunch.lable.append(list[0])
                        if list[0] not in bunch.lable:
                            bunch.lable.append(list[0])
                elif children.tag == 'contenttitle':
                    contenttitle = children.text
                elif children.tag == 'content':
                    content = str(contenttitle)+' '+str(children.text)
                    if (len(content) > 0):
                        seg = jieba.cut(content, cut_all=False)
                        bunch.contents.append(' '.join(seg))
                    else:
                        bunch.contents.append('null')
        print('finish test file:',filePath)


fileutils.saveBatchObj(testRawPath, bunch)
