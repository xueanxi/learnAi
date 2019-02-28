#字典 类似于 java 的 map , 内容使用单引号和双引号都可以
dict = {'a':"apple",
        'b':"book",
        'c':"cell"}
print("print the values of a: ",dict["a"])
print("len of dict = ",dict)

print('key:',dict.keys())

#删除
del dict['b']
print("len of dict = ",dict)

# 插入
dict['d'] = "dog"
print("len of dict = ",dict)

if 'd' in dict:
    print("dict[d] = ",dict['d'])
