mySet = set(['a','b','c','d'])
mySet2 = set(['a','b','d','e','f'])

print("mySet :",mySet)
print("mySet2 :",mySet2)

if 'a' in mySet:
    print("a in mySet")
else:
    print("a not in mySet")

mySet.add('z')
print("after add z ,mySet : ",mySet)

mySet3 = mySet.copy()
print("mySet3 :",mySet3)

# 交集
mySet4 = mySet & mySet2
print("mySet & mySet2 = ",mySet4)

#并集
mySet5 = mySet | mySet2
print("mySet | mySet2 = ",mySet5)

# 这样初始化会去掉列表中的重复值，但是顺序会发生改变
list1 = [2,1,2,3,4,5,4,5,5,5]
mySet6 = set(list1)
print('mySet6',mySet6)
