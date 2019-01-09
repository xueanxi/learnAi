#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-09 14:12:24
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


class MyHandler(sax.ContentHandler):

    def __init__(self):
        self.CurrentData = ""
        self.url = ""
        self.contenttitle = ""
        self.content = ""

   # 元素开始事件处理
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "doc":
            print("*****doc*****")

   # 元素结束事件处理
    def endElement(self, tag):
        if self.CurrentData == "url":
            print("end url:", self.url)
        elif self.CurrentData == "contenttitle":
            print("end titletle:", self.titletle)
        elif self.CurrentData == "content":
            print("end content:", self.content)
        elif self.CurrentData == 'doc':
            print("end doc:")
        self.CurrentData = ""

   # 内容事件处理
    def characters(self, content):
        if self.CurrentData == "url":
            self.url = content
        elif self.CurrentData == "contenttitle":
            self.titletle = content
        elif self.CurrentData == "content":
            self.content = content


root = fileutils.getDataPath() + os.sep
# filePath = root + 'news' + os.sep + 'news.sohunews.020806.txt'
filePath = root + 'news' + os.sep + 'test.txt'

myHandler = MyHandler()
sax.parse(source=filePath, handler=myHandler)
