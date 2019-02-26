#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-09 14:12:24
# @Author  : anxi.xue (xueanxi@163.com)
# @Link    : ${link}
# @Version : $Id$

import time
timeStart=time.clock()
import os
import sys
sys.path.append('..')
from datautils import fileutils
import pandas as pd
import numpy as np
from xml import sax
import re


class MyHandler(sax.ContentHandler):

    def __init__(self):
        self.CurrentData = ""
        self.url = ""
        self.contenttitle = ""
        self.content = ""

   # 元素开始事件处理
    def startElement(self, tag, attributes):
        self.CurrentData = tag

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

#rootdata/test/xml/file1.xml
root = fileutils.getDataPath() + os.sep
filePath = root + 'test' + os.sep +'xml'+os.sep+ 'file1.xml'

myHandler = MyHandler()
# 方法1:直接解析.不过有非法字符的时候会出问题，
#sax.parse(source=filePath, handler=myHandler)

# 方法2:先读出来,处理非法字符串，然后再解析。但是这样耗内存
file = open(filePath, 'r')
text = file.read()
file.close()
text = re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f|&]+", u"", text)
root = sax.parseString(string=text, handler=myHandler)

timeEnd=time.clock()
print("Sax xml spend time:",(timeEnd - timeStart))

