'''一个用于表示汽车的类'''
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

