import numpy as np

import matplotlib.pyplot as plt

'''
矩阵性质
'''

list = [[1, 2], [9, 5]]
matrix1 = np.mat(list);
matrix2 = np.mat([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 19, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
matrix3 = np.mat([[1, 2, 3, 4], [6, 7, 8, 9], [11, 12, 13, 19], [16, 17, 18, 19]])
A = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]


print('0:矩阵的特征向量和特征值')
evals, evecs = np.linalg.eig(A)
print('特征值:', evals, "\n特征向量:", evecs)

print('\n1:使用特征向量和特征值还原矩阵(没有算对，不知道那里出错了)')
sigma = evals * np.eye(3)
print('还原结果为:', evecs * sigma * np.linalg.inv(evecs))

print('\n2: 矩阵的行列式 矩阵不一定都有行列式')
print(np.linalg.det(matrix1))

# 如果将矩阵和它的逆矩阵相乘，结果就应该是单位矩阵。pass:不是所有矩阵都有逆
print('\n3: 矩阵的逆')
print(np.linalg.inv(matrix1))

print('\n4: 对称矩阵')
print(matrix1.T)

print('\n5: 矩阵的秩')
print(np.linalg.matrix_rank(matrix1))

print('\n6: 可逆矩阵求解')
# print(np.linalg.solve(matrix1))
