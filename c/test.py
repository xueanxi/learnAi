#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append('..')
import jieba
import shutil
from datautils import fileutils
from chardet import detect


# def saveFile(filePath, content):
#     with open(filePath, 'wb') as file:
#         file.write(content.encode(encoding='utf-8'))


# def readFile(filePath):
#     with open(filePath, 'rb') as file:
#         content = file.read()
#         return content

# targetFolder = 'testFolder'
# targetFile = 'test.dat'
# rootPath = rootdatas.getDataPath() + os.sep
# folderPath = rootPath + targetFolder
# if not os.path.exists(folderPath):
#     os.mkdir(folderPath)
# filePath = folderPath + os.sep + targetFile

# saveFile(filePath, 'testtstserslfjsajfajfdas')
# content = readFile(filePath)
# print('read content:', content)

# s = 'http://house.sohu.com/ bjesf/  sale/84294750.html'
# print('0:', s.replace(' ', ''))
# list = s.split('http://')
# if(len(list) == 2):
#     list = list[1].split('.sohu')
#     print('4:', list[0])

# str = '期市研究 ＜＜上一页\u3000下一页＞＞\ue40c＜＜上一页\u3000下一页＞＞\ue40c本网站提供之资料或信息，仅供投资者参考，不构成投资建议。\ue40c搜狐财经频道联系方式：热线电话\u3000（０１０）６２７２６１１３或６２７２６１１２2008 组图：奥运圣火在大同传递\u3000市民热情迎接圣火 跳转至：\ue40c页２６／３２\ue40c我来说两句\ue40c作者：摄影／王玉玺\ue40c奥运官网６月２７日讯\u3000今天上午８点，奥运圣火在山西最后一站——大同传递。大同段火炬传递全程约４公里，时间为２小时左右。大同有２０８名火炬手、５３名护跑手进行传递。（奥运官网ｗｗｗ．ｂｅｉｊｉｎｇ２００８．ｃｏｍ\u3000摄影记者\u3000王玉玺）\ue40c（责任编辑：ｗｅｎｘｕ）'
# seg = jieba.cut(str, cut_all=False)
# print('\\'.join(seg))

d = dict()
d['a'] = 'dog'
del(d['a'])
print(d)
