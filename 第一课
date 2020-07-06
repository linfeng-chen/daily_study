import random
x=random.getstate#获取随机数内部生成状态
a=5
while a>0 :
    y = random.randint(1, 100)
    print(y)
    a=a-1
random.setstate(x)#设置内部生成状态，可以让其回到初始状态
a=5
while a>0:
    y = random.randint(1, 100)
    print(y)
    a = a - 1