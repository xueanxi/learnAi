#!/usr/bin/env python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-29 18:15:07
# @Author  : anxi.xue (xueanxi@163.com)
# @Link    : ${link}
# @Version : $Id$


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