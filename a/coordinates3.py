import matplotlib.pyplot as plt
import numpy as np

plt.figure()
x = np.linspace(-np.pi, np.pi)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x,y1,color='b')
plt.plot(x,y2,color='red',linewidth=1.0,linestyle = '--')

y_ticks = np.linspace(-1,1,5)
plt.yticks(y_ticks)

plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],['-π','-π/2','0','π/2','π'])
ax = plt.gca()#axc = 'get current axis' 获取现在的轴
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.xaxis.set_ticks_position('bottom')   #用bottom代替x轴
ax.yaxis.set_ticks_position('left')     #用left代替y轴
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))#axes 百分比


l1, = plt.plot(x,y1,label='up') #label线的名字
l2, = plt.plot(x,y2,color='red',linewidth=1.0,linestyle = '--',label='down')
plt.legend(handles=[l1,l2,],labels=['sin','cos'],loc='best')

plt.show()