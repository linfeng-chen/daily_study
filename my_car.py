from car import Car
from Electric_car import Electriccar


my_new_car = Car('audi','a4',2016)
print(my_new_car.get_describe_name())
my_new_car.odometer_reading=20
my_new_car.read_odometer()

print("\n")
my_tesla = Electriccar("tesla","model s",2019)
print(my_tesla.get_describe_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()