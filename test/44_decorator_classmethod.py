#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-21 19:13:42
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

import os


# 没看懂


def arg_sayer(what):
    def what_sayer(meth):
        def new(self, *args, **kws):
            print('what = ', what)
            return meth(self, *args, **kws)
        return new
    return what_sayer


def FooMaker(word):
    class Foo(object):

        @arg_sayer(word)
        def say(self): pass
    return Foo()

foo1 = FooMaker('this')
foo2 = FooMaker('that')
print type(foo1),
foo1.say()  # prints: <class '__main__.Foo'> this
print type(foo2),
foo2.say()  # prints: <class '__main__.Foo'> that
