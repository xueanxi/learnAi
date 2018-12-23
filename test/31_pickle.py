#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-20 09:46:30
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import pickle

saveDataName = 'python.data'
data = ['apple', 'boy', 'time', ['hello', 'world']]

f = open(saveDataName, 'wb')
pickle.dump(data, f)
f.close()

del data
f = open(saveDataName, 'rb')
saveobj = pickle.load(f)
print('the save obj is:', saveobj)
