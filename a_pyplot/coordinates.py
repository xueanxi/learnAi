import numpy as np
import matplotlib.pyplot as plt

# 确定范围
xrange = [-2 * np.pi, 2 * np.pi]
yrange = [-2, 2]
zero = [0, 0]
# 设置坐标轴范围
plt.xlim(xrange)
plt.ylim(yrange)
# 设置坐标轴名称
plt.xlabel('x')
plt.ylabel('y')
# 设置坐标轴刻度
my_x_ticks = np.arange(-2 * np.pi, 2 * np.pi, 0.5*np.pi)
my_y_ticks = np.arange(-2, 2, 1)
plt.xticks(my_x_ticks)
plt.yticks(my_y_ticks)

# 绘制坐标轴的线
plt.plot(xrange, zero, c='blue')
plt.plot(zero, yrange, c='blue')

# 创建数据
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()
