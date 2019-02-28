# -*- coding: utf-8 -*-
# @Time    : 2/28/19 9:32 AM
# @Author  : Anxi.xue
# @Email   : xueanxi@163.com

from timeit import Timer

# 有些用户对了解解决同一问题的不同方法之间的性能差异很感兴趣。
# Python 提供了一个度量工具，为这些问题提供了直接答案。
# 例如，使用元组封装和拆封来交换元素看起来要比使用传统的方法要诱人的多,
# timeit 证明了现代的方法更快一些。

#=========细粒度的方法=======

timer1 = Timer('t=a; a=b; b=t', 'a=1; b=2')
print('timer1',timer1.timeit())

timer2 = Timer('a=1; b=2')
print('timer2',timer2.timeit())

timer3 = Timer('s = \'sdfafljljflajf\';s.startswith(\'sdf\')')
print('timer3',timer3.timeit())

#=========粗粒度的方法=======
def funcs():
    for i in range(1000):
        print('funcs:',i)
        a = i
        b = i+1
        c = a+b

import profile
import pstats

profile.run('funcs()','result')#执行完之后会在当前目录生成一个result文件
p=pstats.Stats('result')#使用pstats来查看这个result文件
p.sort_stats('time').print_stats(5)   #运行时间前5行
p.sort_stats('cumulative').print_stats(0.1)   #总共时间前10%。