import numpy as np
from numpy import *
import matplotlib.pyplot as plt

'''
随机数
'''

randomMatrix = np.random.rand(3, 3)
print('1: 生成3*3的随机矩阵')
print(randomMatrix)

print('\n2: 生成1个随机数的数组')
print(np.random.random())

print('\n3: 生成5个随机数的数组')
print(np.random.random(5))

print('\n4: 生成5~10之间的随机数')
print(np.random.randint(5, 10))

print('\n5: 生成20个1~10之间的随机数数组')
print(np.random.random_integers(1, 10, 20))

