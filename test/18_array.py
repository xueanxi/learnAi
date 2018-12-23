array1 = ("a",)  # 声明一个元组 ，如果里面只有一个对象，需要加一个逗号

print("len of array1 : ", len(array1))

array2 = ("a", "b", "c", "d")  # 声明元组的方法1
print("len of array2 : ", len(array2))

array3 = "e", "f"  # 声明元组的方法2
print("len of array3 : ", len(array3))

array4 = ("g", "h", array2)
print("len of array4 : ", len(array4))
print("array4 ", array4)
print("array4[2][1] ：", array4[2][1])
