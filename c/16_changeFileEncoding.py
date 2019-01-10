#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-10 10:59:01
# @Author  : anxi.xue (xueanxi@163.com)
# @Link    : ${link}
# @Version : $Id$

import os
import sys
sys.path.append('..')
from datautils import fileutils

root = fileutils.getDataPath() + os.sep
folderPath = root + 'news' + os.sep + "train"
fileutils.encodeUtf8(folderPath)
