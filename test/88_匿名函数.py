# -*- coding: utf-8 -*-
# @Time    : 2/28/19 10:49 AM
# @Author  : Anxi.xue
# @Email   : xueanxi@163.com

#匿名函数使用关键字 lambda

def add1(num):
    return num+1

#1.普通写法
list1 = [1,2,3,4,5,6]
for num in list1:
    print('1.reuslt',add1(num))


#2.使用map
list1 = [1,2,3,4,5,6]
newlist = map(add1,list1)
print('2.reuslt',list(newlist))

#3.使用匿名函数lambda
list1 = [1,2,3,4,5,6]      
newlist2 = map(lambda x:x+1,list1)
print('3.reuslt',list(newlist2))   
