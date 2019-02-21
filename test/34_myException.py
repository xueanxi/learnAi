#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-20 12:15:52
# @Author  : anxi.xue (xueanxi@163.com)

import os

# 自定义一个异常类


class myException(Exception):

    def __init__(self, lenght, atlast):
        Exception.__init__(self)
        self.lenght = lenght
        self.atlast = atlast


try:
    text = input("please input a_pyplot text")
    if(len(text) <= 3):
        raise myException(len(text), 5)
except myException as e:
    print("myException happen. your input len is {},at last {}".format(
        e.lenght, e.atlast))
else:
    print("No exception happen. your input string is ", text)
finally:
    pass
