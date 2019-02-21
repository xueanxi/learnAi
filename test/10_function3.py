def func(a,b =2,c = 3):
    print("a_pyplot = {} , b_numpy = {} , c = {}".format(a,b,c))

#一般情况
func(7,8,9)

#4给a,9给b,c默认3
func(4,9)

#还可以分别赋值
func(c=7,a=5,b=4)
