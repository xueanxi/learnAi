import numpy as np

import matplotlib.pyplot as plt

'''
随机数
'''

list = [[1, 2], [9, 5]]
matrix1 = np.mat(list);
matrix2 = np.mat([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 19, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
matrix3 = np.mat([[1, 2, 3, 4], [6, 7, 8, 9], [11, 12, 13, 19], [16, 17, 18, 19]])
print('1: 矩阵的行列式 矩阵不一定都有行列式')
print(np.linalg.det(matrix1))

#如果将矩阵和它的逆矩阵相乘，结果就应该是单位矩阵。pass:不是所有矩阵都有逆
print('2: 矩阵的逆')
print(np.linalg.inv(matrix1))

print('3: 对称矩阵')
print(matrix1.T)

print('4: 矩阵的秩')
print(np.linalg.matrix_rank(matrix1))

print('5: 可逆矩阵求解')
np.linalg.solve()
print(np.linalg.matrix_rank(matrix1))