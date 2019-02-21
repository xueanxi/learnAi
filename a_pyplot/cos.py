# -*- coding: utf-8 -*-
# Filename: cos.py

import numpy as np
from a_pyplot import drawUtils
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi)
Y = np.cos(x)

plt.plot(x,Y)

xrange = [-2*np.pi, 2*np.pi]
yrange = [-2,2]
drawUtils.drawCoordiates(plt,xrange,yrange)

plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],['-π','-π/2','0','π/2','π'])

plt.show()

