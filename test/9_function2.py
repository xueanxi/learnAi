#函数可以设置默认参数
def func(number1,number2 = 2):
    print("number1 = {}, number2 = {} ".format(number1,number2))

func(4,4)
func(1)

#这是无效的，只有位于参数末尾的的参数，才可以省略
def func2(number1 = 1,number2):
        print("number1 = {}, number2 = {} ".format(number1,number2))

func2(4,4)
func2(1)
