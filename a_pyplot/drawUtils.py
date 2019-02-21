import numpy as np
import matplotlib.pyplot as plt

def drawCoordiates(p,xrange,yrange):
    zero = [0,0]
    #设置坐标轴名称
    p.xlabel('x')
    p.ylabel('y')
    p.plot(xrange,zero,c='blue',linewidth=0.5,)
    p.plot(zero,yrange,c='blue',linewidth=0.5,)