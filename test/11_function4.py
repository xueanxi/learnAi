# 长度可以改变的参数 两个星号的是键值对

def func(a, *b, **c):
    """
    start
    this is a_pyplot doc.
    end
    """
    print("a_pyplot = ",a)
    for i in b:
        print("b_numpy = ",i)
    for i,j in c.items():
        print(str(i)+" is "+str(j))


#func(1,2,3)

# 没有return 的函数的返回值为 None
print(func(1,3,4,5,6,74,one = 1,two =2))
print(func.__doc__)

