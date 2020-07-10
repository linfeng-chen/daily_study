# and 与 or 满足短路逻辑，即从左往右，只有当第一个操作数
#的值无法确定逻辑运算的结果时，才对第二个操作数进行求值
print(3 and 4) # 只有第一个数 and 不能发挥作用，但如果第一个是0即可判断
print(3 or 4) # or对第一个数即可判断，但第一个数不能为0

# 运算符优先级
# or < and < not
print(not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9)
#python 输入时会在两端加上引号，默认为string 类型
# eval 可以去除输入中的引号，还可以同时输入多个数并赋值
# x , y = eval(input("请输入两个数："))
# print(x,y,type(x))

#def con( c ):
    # f = c*5-1
    # return f
#
# a = int(input("请输入一个数字:"))
# print(type(a))
# num = con(a)
# print((num))
# print(1111)

print(not 1 or 5 and 1)
print(not 1)
print(not 1 or 0 and 3 or 6 and 9 )
# 检查特定的值是否包含在列表中，in
num=[1,2,3,4,5]
print(8 in num)
# 检查特定值不在列表中 ，not in
print(8 not in num)
