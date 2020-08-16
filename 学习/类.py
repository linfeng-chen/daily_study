#类是一类具有相同行为的集合体,可以根据类创建对象,这个称为实例化
class Dog():
    '''一次模拟小狗的简单测试'''
    def __init__(self,name,age):
        '''初始化属性name,age'''
        self.name= name
        self.age = age
    def sit(self):
        '''模拟小狗被命令时蹲下'''
        print(self.name.title()+" is now sitting")
    def roll_over(self):
        '''模拟小狗打滚'''
        print(self.name.title()+" rolled over")


# 方法__init__():
# 类中的函数称为方法,当创建实例时,都会运行__init__方法,
# 形参中的self 必不可少,必须位于其他形参前面
# 每个与类相关联的方法调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法
# 以self为前缀的变量都可供类中的所有方法使用，我们还可以通过类的任何实例来访问这些变量
# 可通过实例访问的变量称为属性
# 创建实例
my_dog=Dog("shiyuanshou",3)
print("My dog is "+ my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old")
# 方法 __init__()并未显式地包含return语句，但Python自动返回一个表示这条小狗的实例
# 调用方法
my_dog.sit()
my_dog.roll_over()

class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def get_describe_name(self):
        '''返回完整的描述信息'''
        long_name=str(self.year)+" "+self.make+" "+self.model
        return long_name
my_car=Car("audi",'a4',2019)
print(my_car.get_describe_name())
# 给属性指定默认值
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    #属性odometer_reading 为自己添加的,需要指定初始值
    def get_describe_name(self):
        '''返回完整的描述信息'''
        long_name=str(self.year)+" "+self.make+" "+self.model
        return long_name

    def update_odometer(self,mileage):
        '''这里将里程表设置为指定值,但不能小于原有里程值'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll back an odometer!!")
    def increasse_odometer(self,miles):
        '''将里程数增加特定的值'''
        self.odometer_reading += miles
    def read_odometer(self):
        '''打印车的里程数'''
        print("This car has "+str(self.odometer_reading)+" miles on it")
my_car=Car("audi",'a4',2019)
print(my_car.get_describe_name())
my_car.read_odometer()
# 修改属性的值
# 1.直接通过实例修改
my_car.odometer_reading=100
my_car.read_odometer()
# 2.通过方法修改属性的值
# 在类中添加了方法update_odometer
my_car.update_odometer(90)
my_car.read_odometer()
# 3.通过方法对属性的值进行递增
my_used_car=Car("subar","outback",2010)
print(my_used_car.get_describe_name())

my_used_car.update_odometer(1000)
my_used_car.read_odometer()

my_used_car.increasse_odometer(20000)
my_used_car.read_odometer()



