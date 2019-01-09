#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-09 15:28:00
# @Author  : anxi.xue (xueanxi@163.com)
# @Link    : ${link}
# @Version : $Id$

import os
import sys
sys.path.append('..')
from datautils import fileutils
import pandas as pd
import numpy as np
import re
# improve speed use c lib
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

root = fileutils.getDataPath() + os.sep
# filePath = root + 'news' + os.sep + 'news.sohunews.020806.txt'
filePath = root + 'news' + os.sep + 'test.txt'

# 1
# tree = ET.parse(filePath)  # <class 'xml.etree.ElementTree.ElementTree'>
# root = tree.getroot()           # 获取根节点 <Element 'data' at 0x02BF6A80>

# 2
file = open(filePath, 'r')
text = file.read()
file.close()
text = re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f]+", u"", text)
root = ET.fromstring(text)

# 遍历xml文档的第二层
for child in root:
    # 第二层节点的标签名称和属性
    # 遍历xml文档的第三层
    for children in child:
        # 第三层节点的标签名称和属性
        if children.tag == 'url':
            print(children.tag, children.text)
        elif children.tag == 'content':
            print(children.tag, children.text)
