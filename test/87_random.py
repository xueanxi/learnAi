# -*- coding: utf-8 -*-
# @Time    : 2/28/19 10:41 AM
# @Author  : Anxi.xue
# @Email   : xueanxi@163.com

import random

group = ['a','b','c','d','f']
print('select1:',random.choice(group))
print('select2:',random.choice(group))
print('select3:',random.choice(group))

print('list1',random.sample(range(100),10))
print('list2',random.sample(range(100),10))
print('list3',random.sample(range(100),10))

print('random float1:',random.random())
print('random float2:',random.random())
print('random float3:',random.random())

print('random int1:',random.randrange(5))
print('random int2:',random.randrange(5))
print('random int3:',random.randrange(5))