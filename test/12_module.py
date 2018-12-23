import sys
import os
from sys import argv

print("1: The command line arguments are :")
for i in sys.argv:
    print(i+"\n")

print("2: \n\n the python path is ",sys.path,"\n")#类似于环境变量，这一行里面打印出来的目录里面的模块都可以导入，可以理解成工作目录

print("3: current path:" + os.getcwd())#打印当前目录

print("4: "+argv[0])#使用了 from sys import argv 之后，可以直接调用，而不用sys.argv
