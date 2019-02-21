# -*- coding: utf-8 -*-
# @Time    : 2/21/19 11:10 AM
# @Author  : Anxi.xue
# @Email   : xueanxi@163.com

import numpy as np
import matplotlib.pyplot as plt
import a_pyplot.treePlotter as tp

'''
这个程序没有跑通 treePlotter 这个类有问题，
'''

# mytree = {'Root':{'A1':'*','A2':{'B1':{'C4':'*'},'B2':{'C1':'*','C2':'*','C3':{'D1':'*'}}}}}
#mytree = {'Root': {'A1': {'B1':'*','B2':'*','B3':{'C1':'*'}}, 'A2': '*', 'A3': '*'}}
mytree = {'Root': {'A1': {'B1':'*','B2':'*','B3':'*'}, 'A2': '*', 'A3': '*'}}
print(mytree)
tp.createPlot(mytree)
