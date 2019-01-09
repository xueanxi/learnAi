#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-09 10:38:05
# @Author  : anxi.xue (xueanxi@163.com)
# @Link    : ${link}
# @Version : $Id$

import os
import sys
sys.path.append('..')
from datautils import fileutils
import pandas as pd
import numpy as np

data = ['one', 'two', 'three']
index = [100, 200, 300]
my = pd.Series(data, index)

root = fileutils.getDataPath() + os.sep
# print('root', root)
newsFolder = root + 'news'
newsFile1 = newsFolder + os.sep + 'test.txt'
# newsFile1 = newsFolder + os.sep + 'news.sohunews.020806.txt'


df_news = pd.read_table(
    newsFile1, names=['url', 'docno', 'contenttitle', 'content'], encoding='utf-8', sep='\n\t')

print(df_news)
# df_news = df_news.dropna()
# df_news.head()
# df_news.shape
# content = df_news.content.values.tolist()
# print('content:', content)
