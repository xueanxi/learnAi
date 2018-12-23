#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-03 20:56:16
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

import os
# 元类 type 可以动态创建一个类，而不是使用代码class...来创建


def f(self, name='world'):  # 定义一个函数用于下面创建类
    print('Hello %s' % name)

# 参数1，是类名
# 参数2，是集成的父类，是一个Tupe类型的，允许多继承
# 参数3，绑定类的方法
Hello = type('Hello', (object,), dict(hello=f))

h = Hello()
h.hello()

# 下面使用class创建一个类，和上面是用type创建时完全一样的


class Hello2(object):

    def hello(self, name='world'):
        print('Hello %s' % name)

h2 = Hello2()
h2.hello()


print('====================')
# 类的type()是type
# 对象的type()是类
print('Hello2类的type ', type(Hello2))
print('h2对象的type ', type(h2))
print('Hello类的type ', type(Hello))
print('h对象的type ', type(h))
