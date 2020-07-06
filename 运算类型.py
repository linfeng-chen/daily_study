# // 为地板除，即向下取整
print(5//2)
print(5/2)
print((5//2)*2+(5%2))# 结果运算仍等于原数
#divmod
print(divmod(3,2))# 返回x//y,x%y
x = divmod(5,2)
print(x)
#abs 取绝对值
print(abs(2+4j))#取复数的模
print(int(4.34),"\n",float(5))#转化数字类型
a = complex("2+3j")#复数化
print(a)
#pow 次方函数,支持第三个参数，第三个参数为模数
print(pow(4,5))
print(pow(4,5,3))