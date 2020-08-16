from time import localtime


time = localtime()
print(time)

class A():
    def __repr__(self):
        return "chen linfeng"


class B():
    pass
a = A()
print(a)
b = B()
print(b)#当我们输出某个实例化对象时，其调用的就是该对象的 __repr__() 方法，输出的是该方法的返回值,包含类名以及地址。

# 再python中调用print()打印实例化对象时会调用__str__()如果__str__()中有返回值，就会打印其中的返回值。
class B():
    def __str__(self):
        return "CHEN LINFENG"

b =B()
print(b)

class My_timer():
    def __init__(self):
        self.unit =["年","月","日","时","分","秒"]
        self.prompt = "计时未开始"
        self.last=[]
        self.begin = 0
        self.end =0
    # 开始计时
    def start(self):
        self.begin = localtime()
        print("计时开始...")
    # 停止计时
    def stop(self):
        self.end = localtime()
        self._calc()
        print(self.prompt)
        print("计时结束！")
    # 计算时间插值(内部方法)
    def _calc(self):
        self.last = []
        self.prompt ="总共运行了"
        for index in range(6):
            self.last.append(self.end[index]-self.begin[index])
            if self.last[index]:

                self.prompt +=str(self.last[index])+self.unit[index]

    def __str__(self):
        return self.prompt
    def __repr__(self):
        return self.prompt

while True:
    time = My_timer()
    print(time)
    x = input("按Y开始计时:")
    if x=='Y':
        time.start()
    y=input("按X结束计时:")
    if y =='X':
        time.stop()