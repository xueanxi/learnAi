import numpy as np
import matplotlib.pyplot as plt

def drawCoordiates(p,xrange,yrange):
    zero = [0,0]
    #设置坐标轴名称
    p.xlabel('x')
    p.ylabel('y')
    p.plot(xrange,zero,c='b',linewidth=0.5,)
    p.plot(zero,yrange,c='b',linewidth=0.5,)