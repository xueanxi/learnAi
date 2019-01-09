#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-29 18:09:10
# @Author  : anxi.xue (xueanxi@163.com)
# @Link    : ${link}
# @Version : $Id$

import os
import sys
sys.path.append('..')
from datautils import fileutils
from lxml import etree, html

# path = rootdatas.getDataPath() + os.sep + "a.html"
# file = open(path, 'rb')
# content = file.read()
# file.close()

# page = html.document_fromstring(content)
# text = page.text_content()
# print(text)


path = fileutils.getDataPath() + os.sep + "news" + os.sep + \
    'test.txt'
file = open(path, 'r')
content = file.read()
file.close()
print(content)
