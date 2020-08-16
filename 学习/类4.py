class Username():
    def __init__(self,first,last):
        self.first = first
        self.last = last
        self.__age = 20

    def format_name(self):
        print("The name is "+"{} {}".format(self.first.title(),self.last.title()))
        print('The name is '+'%s %s' %(self.first,self.last))

one_people = Username('chen','linfeng')
one_people.format_name()

# ?如何访问私有成员:_类名__变量名
print(one_people._Username__age)

# 类的组合(不同类之间的组合）
class Turtle:
    def __init__(self,x):
        self.num = x


class Fish:
    def __init__(self,x):
        self.num = x

class Pool:
    def __init__(self,x,y):
        self.turtle =Turtle(x)
        self.fish = Fish(y)

    def print_name(self):
        print("turtle:%d,fish:%d"%(self.turtle.num,self.fish.num))

pool = Pool(1,10)
pool.print_name()

# 类定义，类对象，实例对象
class Num():
    count =10

num = Num()
num1= Num()
num2= Num()
print(num.count,num1.count,num2.count)

num.count  = 100
print(num.count,num1.count,num2.count)
Num.count = 10000
print(num.count,num1.count,num2.count)

#绑定
class Cc:
    def set_xy(self,x,y):
        self.x = x
        self.y = y
    def print_xy(self):
        print(self.x,self.y)

one_example = Cc()
print(one_example.__dict__)#获取实例的属性和方法
print(Cc.__dict__)
one_example.set_xy(2,3)
print(one_example.__dict__)
print(Cc.__dict__)

# 内置函数
# issubclass(class,classinfo)判断class是否是classinfo子类，classinfo可以是类对象组成的元组
print(issubclass(Cc,object))
# isinstance(object,classinfo)检查实例对象object是否属于classinfo,classinfo可以为类组成的元组
print(isinstance(one_example,Cc))
# hasattr(object,name)检测实例对象是否有属性name
print(hasattr(one_example,'x'))
# getattr(object,name,[default])返回实例对象属性的值，default抛出异常
print(getattr(one_example,'f','no attribute'))
# setattr(object,name,value)设置实例对象属性的值，没有则新建
setattr(one_example,'r',23)
print(one_example.r)
# delattr(object,name)删除指定的属性

# property(fget,fset,fdel,doc)通过属性设置属性

class C:
    def __init__(self,x=10):
        self._x = x

    def get_x(self):
        return self._x

    def set_x(self,number):
        self._x = number

    def del_x(self):
        del self._x
    x=property(get_x,set_x,del_x,"已删除")

one_ex = C()
print(one_ex.get_x())
print(one_ex.x)
one_ex.x = 99
print(one_ex.get_x())
del one_ex.x
print(one_ex._x)