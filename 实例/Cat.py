class Cat:
    def __str__(self):
        print("使用这个函数")
        return "hello world"
    def eat(self):
        print("小猫爱吃鱼")
    def drink(self):
        print("小猫要喝水")



if __name__=="__main__":
    tom = Cat()
    tom.eat()
    tom.drink()
    print(tom)
    print(id(tom))
    tom.age = 13
    print(tom.__dict__)
    # print(tom.__str__())
    print(tom)