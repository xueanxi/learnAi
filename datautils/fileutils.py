#!/usr/bin/env python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-29 18:15:07
# @Author  : anxi.xue (xueanxi@163.com)
# @Link    : ${link}
# @Version : $Id$

import os
from os.path import dirname, abspath
import pickle


def getDataPath():
    path = dirname(abspath(__file__))
    parentpath = dirname(abspath(path))
    return parentpath + os.sep + 'rootdata'


def saveFile(filePath, content):
    """
    doc:save file with normal style.
    """
    with open(filePath, 'w') as file:
        file.write(content)


def readFile(filePath):
    """
    doc:read file with normal style.
    """
    with open(filePath, 'r') as file:
        content = file.read()
        return content


def saveFileB(filePath, content):
    """
    doc:save file with byte.
    """
    with open(filePath, 'wb') as file:
        file.write(content.encode(encoding='utf-8'))


def readFileB(filePath):
    """
    doc:save file with byte.
    """
    with open(filePath, 'rb') as file:
        content = file.read()
        return content


def saveBatchObj(filePath, obj):
    """
    doc:save batch obj.
    """
    with open(filePath, 'wb') as file:
        pickle.dump(obj, file)


def readBatchObj(filePath):
    """
    doc:save batch obj.
    """
    with open(filePath, 'rb') as file:
        return pickle.load(file)
