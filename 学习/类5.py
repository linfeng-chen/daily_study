# if __name__ =='__main__'
def demo():
    '''测试函数'''
    print("chen linfeng")

print(dir(demo))
print(demo.__doc__)

class Person():
    ''''''
    def __init__(self,name):
        self.name = name
        self.__age = 18
    def __secret(self):
        print("%s的年龄是%d岁"%(self.name,self.__age))


xiaofang = Person("小芳")
print(xiaofang._Person__age)
xiaofang._Person__secret()