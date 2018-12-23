import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2
plt.figure()
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle = '--')
plt.xlim((-3,5))
plt.ylim((-3,5))
plt.xlabel('x')
plt.ylabel('y')

new_ticks1 = np.linspace(-1,0,1)

plt.yticks(new_ticks1)
plt.xticks([-np.pi,0,np.pi],[r'-Pi',r'0',r'Pi'])
ax = plt.gca()#axc = 'get current axis' 获取现在的轴
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.xaxis.set_ticks_position('bottom')   #用bottom代替x轴
ax.yaxis.set_ticks_position('left')     #用left代替y轴
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))#axes 百分比
plt.show()