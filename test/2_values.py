age = 20
name = 'anxi'

print('1: {0} was {1} year old'.format(name,age) )
print('2: {} was {} year old'.format(name,age) )
print('3: '+name+' was '+str(age)+" year old.")#不建议这么写，容易出错

print("4: {0:.6f}".format(1/3))#这样可以限定小数点后面的位数
print("5: {0:_^20}".format("abcdef"))#^20 符号可以用来打印20位长度的字符串

#打印多行文字 1
print("""6:第一行
第二行
第三行""")

#打印多行文字 2
print("7:第一行\n第二行\n第三行")

print('a_pyplot',end="   ")#end 的使用
print('b_numpy',end= "  \n")

print(r"8: abcdefg \n hijk") # 字符串签名加上 r  可以去掉转义

a = 5#给变量赋值
print("9:"+str(a))

c = 3+3; d = 4+4  #不建议使用分号，一行最好只有一个语句

print("10: the values is",22)








