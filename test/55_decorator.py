#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-24 18:20:32
# @Author  : anxi.xue (xueanxi@163.com)
import functools
import os
import time

# decorator 装饰器。函数的功能在代码写好之后就是固定的，
# 但是可以使用装饰器，来修饰一个函数，动态增加函数的功能。


# 例子1 decorator 不带参数的例子
def addTime(func):
    def wrapper(*args, **kw):
        print('time is 18:33 by', func.__name__)
        return func(*args, **kw)
    return wrapper


@addTime
def sayHello():
    print("Hello world!!!")


# 例子2 decorator 带参数的例子,带参数需要写三重

def addTime2(text):
    def decorator(func):
        #@functools.wraps(func)
        def wrapper(*args, **kw):
            print('wrapper say : args is {} : {}'.format(text, func.__name__))
            return func
        return wrapper
    return decorator


@addTime2('fuck')
def sayHello2():
    print("Hello world222")

func = sayHello2
print('sayHello2 name is ', func.__name__)


# 作业1
def metric(fn):
    def wrapper(*args, **kw):
        timeBegin = time.time()
        result = fn(*args)
        timeEnd = time.time()
        print('%s executed in %s ms' % (fn.__name__, timeEnd - timeBegin))
        return result
    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)

if f != 33:
    print('测试失败1')
elif s != 7986:
    print('测试失败2')
# 作业2

print('============作业2========\n')


def log3(*arg):
    def decorator(func):
        def wrapper(*args, **kw):
            print('begin call')
            print('传入的参数是:', *arg)
            func()
            print('end call')
            return func
        return wrapper
    return decorator


@log3()
def test1():
    print('i am test1')


@log3('execute')
def test2():
    print('i am test2')

test1()
print('=========== 分界线 ========')
test2()
