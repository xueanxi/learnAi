#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-29 18:15:07
# @Author  : anxi.xue (xueanxi@163.com)
# @Link    : ${link}
# @Version : $Id$

import os
from os.path import dirname, abspath


def getDataPath():
    path = dirname(abspath(__file__))
    parentpath = dirname(abspath(path))
    return parentpath + os.sep + 'rootdata'
