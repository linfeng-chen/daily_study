x = [1,2,3,4,5]
print(x)
x=[1,2,3,4,5,"hello"]
print(x)
#列表：列表可添加任意类型的数据
print(x[5][0])
for i in x:
    print(i)
print(x[-1])
# 下表索引时，可用-1直接找到最后一个，以此类推，倒数第二就是-2
# 列表切片
print(x[0:6])
print(x[0:3])
print(x[2:9])#只输出列表内的数据
print(x[-1:6])
# 🐂🐂
print(x[:3])#输出前三个
print(x[3:])#输出后三个
print(x[:])#输出全部
# 列表也可以像range()一样拥有第三个参数步长
print(x[0:6:2])
print(x[::2])
# 可以倒序输出列表中的元素
print(x[::-1])