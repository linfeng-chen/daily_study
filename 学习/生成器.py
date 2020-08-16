'''协同程序指的是可以运行的独立函数调用，函数可以暂停或者挂起，并在需要的时候从程序离开的地方继续或重写开始'''
# 生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。

def Mygen():
    '''生成器例子'''
    print("生成器被执行！")
    yield 1  #返回一个数字并暂停
    yield 2

temp = Mygen()
print(temp)
next(temp)
print(next(temp))
# print(next(temp))

temp = {i:i%2 ==0 for i in range(10)}
print(temp)


e = (i for i in range(10))   #生成器
print(next(e))
print(sum(i for i in range(10)))