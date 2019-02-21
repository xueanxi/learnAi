myList = ["b_numpy" , "a_pyplot" , "d" ,"c","e"]

print("the length of myList = {}".format(len(myList)))

i = 0
for item in myList:
    print("the {} item in myList is:{}".format(i,item))
    i+=1

myList.append("f")
print("after append f, the list is ",myList)

myList.sort()
print("after sort list is",myList)

print("the first item is",myList[0])

del myList[1]
print("after del list:",myList)




