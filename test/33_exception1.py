#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-20 10:51:08
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

# 因为快捷键的问题这个，需要在命令行运行这个文件才可以触发异常
try:
    text = input("Enter somethings:")
except EOFError as e:
    # 输入过程中按 ctrl + d 会触发
    print("EOFError happend")
except InterruptedError as e:
    # 输入过程中按 ctrl + c 会触发
    print('IndentationError happend')
else:
    print("what your input is:", text)
finally:
    print("finally")
