#Sequence 序列 字符串，元组，列表 都是属于序列
# 特点1  是 都有 in 和 not in的操作
# 特点2  都有切片功能，即可以通过下标访问

sequence = ['a_pyplot','b_numpy','c','d','e','f','g','h']
print("item 0 :",sequence[0])
print("item 1 :",sequence[1])
print("item 2 :",sequence[2])
print("item -1 :",sequence[-1]) # 倒数第一个

print("item 1-3 :",sequence[1:3]) #1:3 其实是下标 1和2
print("item 1-结束 :",sequence[1:]) #1: 其实是下标 1到最后一个
print("item 开始-3 :",sequence[:3]) # :3 其实是前三个
print("item -1 :",sequence[:3]) # :3 其实是前三个
print("item 开始到-1 :",sequence[:-1]) # :-1 除了倒数最后个
print("item 所有 :",sequence[:]) # : 其是所有

print("step = 2 : ",sequence[::2])#步长为2，第三个参数为步长





