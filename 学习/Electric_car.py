from 学习.car import Car

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