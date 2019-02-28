# -*- coding: utf-8 -*-
# @Time    : 2/28/19 9:49 AM
# @Author  : Anxi.xue
# @Email   : xueanxi@163.com

"""
开发高质量软件的方法之一是为每一个函数开发测试代码，并且在开发过程中经常进行测试
doctest模块提供了一个工具，扫描模块并根据程序中内嵌的文档字符串执行测试。
测试构造如同简单的将它的输出结果剪切并粘贴到文档字符串中。
通过用户提供的例子，它强化了文档，允许 doctest 模块确认代码的结果是否与文档一致:
"""

def funcAdd(a,b):
    """Computes the arithmetic mean of a list of numbers.
        >>> print(funcAdd(20, 30))
        40
    """
    return a+b

def funcReduce(a,b):
    """Computes the arithmetic mean of a list of numbers.
        >>> print(funcReduce(30, 20))
        15
    """
    return a-b

import doctest
doctest.testmod()