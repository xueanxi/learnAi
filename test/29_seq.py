#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-20 09:21:21
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os

sss = 'abcdefg123'
string2 = sss[1:4]
print("string2 = ", string2)

string3 = sss[1:4:2]
print("string3 = ", string3)

string4 = sss[::-1]
print("string 4 =", string4)

newlist = [1,2,3,4,5,6,7,88]
print('string 5:',newlist[0:-1])
