mySet = set(['a_pyplot','b_numpy','c','d'])
mySet2 = set(['a_pyplot','b_numpy','d','e','f'])

print("mySet :",mySet)
print("mySet2 :",mySet2)

if 'a_pyplot' in mySet:
    print("a_pyplot in mySet")
else:
    print("a_pyplot not in mySet")

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

