#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-27 20:59:47
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

import sys


def test():
        # argv是读取命令行的参数，它至少会有一个元素，
        # 比如用户什么都不输入的时候，它就是文件名
    args = sys.argv
    if len(args) == 1:
        print('Hello, world! {}'.format(args[0]))
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

# 在命令行输入的时候，会自动为__name__ 赋值为__main
if __name__ == '__main__':
    test()
