import sys
import module13

#dir 作用是打印一个模块里面所有的 变量 和 函数

print(dir(sys))

print(dir())

a = "sssss"
print(dir())

del a

print(dir())

print(dir(module13))
