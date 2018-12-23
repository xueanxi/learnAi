#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-03 20:35:10
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

import os
from enum import Enum, unique

# 默认的枚举类是从1为索引开始的
Month = Enum('month', ('Jan', 'Feb', 'Mar', 'Apr', 'May'))
# 有多种访问枚举类的方法
print(Month(1))
print(Month['Jan'])
print(Month.Jan)

# 如果想从所以0开始，可以自己派生一个枚举类


@unique  # 加上这个之后，枚举类的值就不能相等
class Week(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
    #FFF = 6

print(Week(0))
print(Week['Sun'])
print(Week.Sun)

# 获得枚举的值，可以使用value
print(Week.Wed.value)

# 遍历枚举类
for name, member in Week.__members__.items():
    print(name, '==>', member, "=", member.value)

# 练习题：把Student的gender属性改造为枚举类型，可以避免使用字符串：


class Gender(Enum):
    Male = 0
    Female = 1


class Student():

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
