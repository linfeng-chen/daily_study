# #将字符串转换为列表：
# # 1.list:会将每个字符都划归为一个列表元素
# str="chen linfeng"
# str=list(str)
# print(str)
# # 2.split()
# str="chen linfeng"
# str=str.split()
# print(str)
# s='1234567'
# s=s.split(' ')
# print(s)
# # 对于数字想要转换成列表，用list合适
#
# # 将列表转化为字符串
# # 1.join()
# # str=['1','2','3','4']
# # str=''.join(str)
# # print(str)
# # 注意,当列表元素并不是str类型时
a=[1,2,3,4,5]
b=[str(i) for i in a]
print(b)
# 将列表转换为字典
a=['name','age','height']
b=['chenlinfeng',20,168]
person=dict(zip(a,b))
print(person)

# 方法replace()将字符串中特定单词替换为另一个单词
# 在局部使用全局变量使用global关键字
# 在局部使用外部变量使用nonlocal关键字
# s.disjoint(s1)判断s,s1是否没有交集
# s.issubest(s1),判断s是否是s1的子集
# s.union(s1)返回两者的并集
# s.intersection(s1)返回交集
# s.difference(s1)返回差集

