# bool 用于分支和循环语句
print(bool(250),bool("sdasd"))
# 空字符串为False, 0值为false
x =bool("")
print(x)
#bool 为false的类型或数据
#定义为false的对象：none,false
#值为0的数字类型：0，0.0,oj,Decimal(0),Fraction(0,1)
#空序列和集合："",(),[],{},set(),range(0)
print(1==True) #1和true相等，0与false相等，true与false是特殊的整数类型
print(True+False,True*False)
#逻辑运算符：and , or ,not ->并，或，非
print(3<4 and 4>1)
print("345"<"5")#Asic码
print(3 and 5)#似乎 and 取后一个数
print(not 0)
print("fish" and "love")
print("fish" and 9)
print(5 or 6) #or 取前一个数


