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

