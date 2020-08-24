class Gun():
    '''这是一个枪类'''
    def __init__(self,model):
        self.model = model
        self.buttle_count = 0

    def add_bullet(self,count):
        self.buttle_count +=count

    def shoot(self):
        print("biubiubiu")
        self.buttle_count -=1

class Solider():
    '''这是一个描述士兵的类'''

    def __init__(self, name):
        self.name = name
        self.gun = None
    def fire(self):
        if self.gun is None:
            print("%s没有枪......"%self.name)
            return
        self.gun.shoot()

xusanduo = Solider("许三多")
xusanduo.fire()
AK47 = Gun("AK47")
xusanduo.gun = AK47
xusanduo.gun.add_bullet(10)
xusanduo.fire()

print(xusanduo.gun.buttle_count)