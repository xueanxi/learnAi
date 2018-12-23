#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-20 10:16:51
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import io

f = io.open("abc.txt", 'wt', encoding='utf-8')
# io写文件必须在字符串前面跟上一个u,转换为unicode
# f.write("问一下，出现这个问题smartmanager的版本号是多少呢？我们现在的版本应该已经修复这个问题了")
f.write(u"问一下，出现这个问题smartmanager的版本号是多少呢？我们现在的版本应该已经修复这个问题了")
f.close()

text = io.open("abc.txt", encoding='utf-8').read()
print(text)
