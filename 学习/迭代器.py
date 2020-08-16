#iter()
# next()

# 魔法方法：__iter__(),__next__()
# 一个容器如果是迭代器，则需要包含上述魔法方法


str = "chen linfeng"
it = iter(str)
print(it)
print(next(it))
print(next(it))


class Fibs:
    '''自定义迭代器'''
    def __init__(self,n =10):
        self.a = 0
        self.b = 1
        self.n =n
    def __iter__(self):
        return self
    def __next__(self):
        self.a ,self.b =self.b,self.a+self.b
        if self.a >self.n:
            raise StopIteration
        return self.a

temp  = Fibs(20)
print(temp)
for i in temp:
    if i<100:
        print(i)
    else:
        break