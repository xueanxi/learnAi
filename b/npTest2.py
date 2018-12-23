import numpy as np
from numpy import *
import matplotlib.pyplot as plt

'''
矩阵的运算
'''

list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = [[1, 2, 3]]

matrix = np.mat(list)
matrixOne = np.ones([3, 3])

a = matrix

print('1: matrix +')
print(matrix + matrixOne)

print('\n2: matrix -')
print(matrix - matrixOne)

#矩阵相乘 结果为 矩阵1的行数和矩阵2的列数
print('\n3: matrix x')
print(mat(list) * mat(list2))


