#描述符就是 将某种特殊类型的类的实例指派给另一个类的属性
# 特殊类型至少实现以下方法的一个
# __get__(self,instance,owner) 用于访问属性，他返回属性的值
# __set__(self,instance,value)将在属性分配操作中调用，不返回如何值
# __delete__(self,instance)控制删除操作，不返回值

class Try():        #这个称为描述符类
    def __get__(self, instance, owner):
        print("getting....",self,instance,owner)
    def __set__(self, instance, value):
        print("settinf....",self,instance,value)
    def __delete__(self, instance):
        print("deleting....",self,instance)

class Test:
    x = Try()

test = Test()
test.x
print(test)
print(Test)
## 可以看到，self即是描述符类本身的一个实例 ，instance即是拥有这个属性的实例--Test,ower即是拥有者这个类
test.x = 'x-man'
del test.x



