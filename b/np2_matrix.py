import numpy as np
from numpy import *
import matplotlib.pyplot as plt

'''
矩阵的运算
'''

list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = [[1], [2], [3]]
list3 = [[1,2,3], [2,4,6]]

matrix = np.mat(list)
matrixOne = np.ones([3, 3])

a = matrix

print('1: 矩阵加')
print(matrix + matrixOne)

print('\n2: 矩阵 减')
print(matrix - matrixOne)

print('\n3: 矩阵 点乘')
print(matrixOne * 8)

# 矩阵相乘 结果为 矩阵1的行数和矩阵2的列数
print('\n4: 矩阵相乘 ：结果为 矩阵1的行数和矩阵2的列数')
print(mat(list) * mat(list2))

print('\n5: 矩阵转置')
print(mat(list).T)

print('\n6: 矩阵转置2')
print(mat(list).transpose())

print('\n7: 获得矩阵的行列数')
print(mat(list3).shape)

print('\n8: 矩阵切片,按行切片')
print(matrix[0])

print('\n9: 矩阵切片,按列切片')
print(matrix.T[0])

print('\n10: 矩阵复制')
print(matrix.copy())

print('\n11: 矩阵比较')
print(matrix == matrix.T)