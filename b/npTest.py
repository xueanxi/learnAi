import numpy as np
import matplotlib.pyplot as plt

list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = [[1, 2, 3]]
matrix = np.mat(list)

# plt.plot(matrix)
# plt.show()

matrix2 = np.mat(list2)

print(matrix)
print(matrix2.T)
