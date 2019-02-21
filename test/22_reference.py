# reference 引用

list1 = ['a_pyplot','b_numpy','c','d']
list2 = list1

del list1[0]
#这里因为是指向同一个对象，所以删除了list1，list2也会跟着删除
print("list1 : ",list1)
print("list2 : ",list2)


#下面这种就是通过切片的方式，完整复制
list3 = ['a_pyplot','b_numpy','c','d','e','f']
list4 = list3[:]
del list3[0]

print("list3 : ",list3)
print("list4 : ",list4)




