class Person():
    '''小明跑步'''
    def __init__(self,name,height):
        self.name = name
        self.height = height
    def __str__(self):
        return "我的名字是%s,体重是%.2f公斤"%(self.name,self.height)
    def run(self):
        self.height -=0.5
    def eat(self):
        self.height +=1

xiaoming = Person("小明",75)
print(xiaoming)
print(xiaoming.height)
xiaoming.eat()
xiaoming.run()
print(xiaoming.height)