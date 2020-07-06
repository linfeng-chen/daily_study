#增
#append:每次增加一个对象
heros=["钢铁侠","绿巨人"]
print(heros)
heros.append("雷神")
print(heros)
# extend,可增加一个可迭代对象,其参数就必须是一个可迭代对象
#新的内容加到源列表最后一个元素后面
heros.extend(["队长","黑寡妇"])
print(heros)
# 可直接进行列表增加
x=[1,2,3,4,5]
print(x)
x[len(x):]=[6,7,8,9]#从末端开始添加元素len():
print(x)
x[len(x):]=[2]
print(x)
#insert 函数
#第一个参数为待插入位置，第二个参数为待插入元素
x=[1,3,4,5]
x.insert(1,2)
print(x)
x.insert(0,heros)
print(x)
print(x[0][0])
x.insert(0,"her")
print(x)
#删
# remove:如果列表中有多个匹配元素，那么其只会删除第一个
# 如果指定的元素不存在，那么会报错
x.remove("her")
print(x)
# pop 函数：根据下表删除对象
x.pop(0)
print(x)
# clean 函数：可直接清空列表
x.clear()
print(x)

# 改
# 直接更改
print(heros)
heros[1]="girl"
print(heros)
# 利用切片改变一段
heros[3:]=["超人","蜘蛛侠","惊奇队长"]
print(heros)

# 对数据进行排序，sort函数从小到大，reverse()将数据反转，从而达到从大到小的作用

number=[3,6,4,1,8,9,34]
print(number)
number.sort()
number.reverse()
print(number)
number=[3,6,4,1,8,9,34]
print(number)
number.sort(reverse=True)
print(number)
# 查
# count :查询元素出现的次数
print(number.count(3))
# index :查询元素的索引,返回第一个元素的位置
# index(x,start,end)第二个和第三个参数指定查找范围
print(heros.index("超人"))

#当不知道元素所在位置时，可用index进行便捷操作
heros[heros.index("超人")]="神明"
print(heros)
# print(number.index(34,1,4))
# copy 拷贝列表

number1=number.copy()
print(number1)
number1.clear()
print(number1)
number1=number[:4]
print(number1)
###此上为均为浅拷贝
##演示效果
