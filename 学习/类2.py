#继承
# 当要编写的类是一个类的特殊版本时,可使用继承,其会获得原有类(父类)的所有属性和方法,还可以添加自己的属性和方法
# 子类的方法__init__()
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
    def fill_gas_tank(self):
        '''电动车没有邮箱'''
        print("This car need a gas tank!")


class Battery():
    '''将Electriccar 部分功能迁移到Battery中'''
    def __init__(self,battery_size=70):
        '''初始化电瓶属性'''
        self.battery_size=battery_size

    def describe_battery(self):
        '''打印电瓶容量'''
        print("This car has a "+ str(self.battery_size)+"-kwh battery")

    def get_range(self):
        '''指出电瓶的续航里程'''
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go " + str(range) + " miles"
        print(message)

class Electriccar(Car):
    '''电动车的特殊面'''
    def __init__(self,make,modul,year):
        '''初始化父类的属性
        初始化字类特有属性'''
        super().__init__(make,modul,year)
        self.battery=Battery()
    #     Battery()为一个类，此处将其实例化作为一个属性

    def fill_gas_tank(self):
        print('This car doesn\'t need a gas tank!')




new_car = Electriccar('tesla','model s',2019)


# 定义子类时，必须在括号内指定父类的名称。方法__init__() 接受创建Car实例所需的信息
# super()是一个特殊函数，帮助Python将父类和子类关联起来。
# 这行代码让Python调用ElectricCar的父类的方法__init__()，让ElectricCar实例包含父类的所有属性
# 给子类定义属性和方法
# 在子类中定义的属性和方法只在字类创建的实例中可用，父类不包含，

new_car1=Car("outo","XX",2019)
print(new_car1.get_describe_name())

# 重写父类的方法
# 当父类的方法不符合字类时，可对其进行重写
# 在子类定义同名方法，在调用时python会只考虑子类的方法
new_car1.fill_gas_tank()
new_car.fill_gas_tank()

# 将实例用作属性
# 当类中所含的属性方法越来愈多，需要将一部分作为一个独立的类提取出来，可将大型类拆分成多个小类
# 不断给ElectricCar类添加细节时，我们可能会发现其中包含很多专门针对汽车电瓶的属性和方法。
# 在这种情况下，我们可将这些属性和方法提取出来，放到另一个名为Battery的类中，并将一个Battery实例用作ElectricCar类的一个属性：

new_car.battery.describe_battery()
# 实例new_car中查找属性battery，并对存储在该属性中的Battery实例调用方法describe_battery()。
new_car.battery.get_range()


