# -*- coding: utf-8 -*-
# @Time    : 2/27/19 2:20 PM
# @Author  : Anxi.xue
# @Email   : xueanxi@163.com

# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，
# 然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
# 我们可以使用 list() 转换来输出列表。
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同,
# 利用 * 号操作符，可以将元组解压为列表。

a = ['1','2','3','4','5']
zip1 = zip(a)
print('zip1',list(zip1))

b = ['6','7','8','9','10']
zip2 = zip(a,b)
print('zip2',list(zip2))

# c最短，以c为长度
c= ['1','2','3']
zip3 = zip(a,b,c)
print('zip3',list(zip3))

# for 循环遍历
for (a,b,c) in zip(a,b,c):
    print('for:',a,' ',b)
