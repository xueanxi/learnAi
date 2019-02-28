myList = ["b" , "a" , "d" ,"c","e"]

print("1 the length of myList = {}".format(len(myList)))

i = 0
for item in myList:
    print("the {} item in myList is:{}".format(i,item))
    i+=1

myList.append("f")
print("2 after append f, the list is ",myList)

myList.sort()
print("3 after sort list is",myList)

print("4 the first item is",myList[0])

del myList[1]
print("5 after del list:",myList)

str1 = '<Start> jhfjajfd </Start>'
if not str1.startswith('<Start>'):
    print('6 str1 is not start with tag.')
if not str1.endswith('</Start>'):
    print('7 str1 is not end with tag.')




