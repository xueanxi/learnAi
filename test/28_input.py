#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-20 00:11:06
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

import os


def reverse(text):
        # 倒转字符串的函数
    return text[::-1]


def ispalindrome(text):
        # 判断是否回文的函数
    return (text == reverse(text))

something = input('input a_pyplot text:')

if ispalindrome(something):
    print("your input is palindrome!")
else:
    print("your input is not palindrome!")
