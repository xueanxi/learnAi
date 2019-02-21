# -*- coding: utf-8 -*-
# @Time    : 2/21/19 11:10 AM
# @Author  : Anxi.xue
# @Email   : xueanxi@163.com

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi,2*np.pi,100)
y = np.sin(x)
yn = y+np.random.random_integers(-10,10,len(x))*0.05#随机生成噪点数据


plt.scatter(x,yn,c='blue',marker='o')#绘制噪点
plt.plot(x,y,c='red')
plt.show()