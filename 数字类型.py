x = 0.3
y = 0.5
print(x+y)
i = 0
while i<1:
    i=i+0.1
    print(i)
import decimal  #十进制模块，可以实现浮点数精确计算，比较
a = decimal.Decimal("0.91")#实例化
b = decimal.Decimal("0.02")
print( a + b )
c = decimal.Decimal("0.5")
d= 0.5
print(c>a+b)
print(d<a+b)
e = 1+2j
f = 1-2j
print(e.real,e.imag)#虚数是以浮点数存放
print((e*f).real)
