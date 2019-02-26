#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-09 15:28:00
# @Author  : anxi.xue (xueanxi@163.com)
# @Link    : ${link}
# @Version : $Id$

import time
timeStart=time.clock()
import os
import sys
sys.path.append('..')
from datautils import fileutils
import re
# improve speed use c lib
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


#rootdata/test/xml/file1.xml
root = fileutils.getDataPath() + os.sep
filePath = root + 'test' + os.sep +'xml'+os.sep+ 'file1.xml'

# # 方法1：直接解析，但是有非法字符串的时候会解析错误
# tree = ET.parse(filePath)
# root = tree.getroot()

# 方法2:先读出来，然后处理非法字符串，再解析
file = open(filePath, 'r')
text = file.read()
file.close()
text = re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f|&]+", u"", text)
#text = re.sub(u"&", u"", text)
root = ET.fromstring(text)


timeEnd=time.clock()
print("ElementTree spend time:",(timeEnd - timeStart))

# 遍历xml文档的第二层
# for child in root:
#     # 第二层节点的标签名称和属性
#     # 遍历xml文档的第三层
#     for children in child:
#         # 第三层节点的标签名称和属性
#         if children.tag == 'url':
#             print(children.tag, children.text)
#         elif children.tag == 'content':
#             print(children.tag, children.text)
