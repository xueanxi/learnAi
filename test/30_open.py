#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-20 09:22:01
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
poem = """\
Programming is fun
when the work is done
if you wanna make your work also fun:
	use python!
"""

filename = 'file/poem.txt'
f = open(filename, 'w')
f.write(poem)
f.close()

s = open(filename, 'r')
while True:
    line = s.readline()
    if len(line) == 0:
        break
    else:
        print(line)
s.close()

print("======help(open)=========")
print('4')
