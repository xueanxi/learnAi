#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-21 21:11:04
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

# 递归
import os


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print('fact(1) = ', fact(1))
print('fact(5) = ', fact(5))
print('fact(200) = ', fact(500))

# 递归层数如果太多会出现堆栈溢出
# RecursionError: maximum recursion depth exceeded in comparison
#print('fact(1000) = ', fact(1000))


# 为了避免堆栈溢出，可以把递归函数改成尾递归函数。
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，
# 都只占用一个栈帧，不会出现栈溢出的情况。
# 上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，
# 所以就不是尾递归了。要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中：

def fact2(n):
    return(fact_item(n, 1))


def fact_item(n, result):
    if n == 1:
        return result
    else:
        return fact_item(n - 1, n * result)


print('fact2(1) = ', fact2(1))
print('fact2(5) = ', fact2(5))
print('fact2(200) = ', fact2(200))


# 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，
# 所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。
#print('fact2(1000) = ', fact2(1000))
