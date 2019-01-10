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
from chardet import detect


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


def encodeUtf8(folderPath, encode="utf8"):
    for file in os.listdir(folderPath):
        filePath = folderPath + os.sep + file
        with open(filePath, 'rb+') as file:
            print('start read file:', file)
            text = file.read()
            encoding = detect(text)['encoding']  # check encoding style
            try:
                print('ready decode:', encoding)
                text = text.decode(encoding)
            except Exception as e:
                # 解决方法：处理的字符的确是gb2312，但是其中夹杂的部分特殊字符，是gb2312编码中所没有的。
                # 如果有些特殊字符是GB18030中有的，但是是gb2312中没有的，则用gb2312去解码，也比较会出错。
                # 所以，此种情况，可以尝试用和当前编码（gb2312）兼容的但所包含字符更多的编码（gb18030）去解码，或许就可以了。
                # GB2312，GBK，GB18030，是兼容的，包含的字符个数：GB2312 < GBK < GB18030
                # text = text.decode(encoding)
                print('ready decode:GB18030')
                text = text.decode('GB18030')
            print('ready encode:', encode)
            text = text.encode(encode)
            file.seek(0)
            file.write(text)
            print('finish :', file)

    print('finish all!!!')
