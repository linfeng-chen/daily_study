# -*- coding = utf-8 -*-
# @time:2020/9/29 19:19
# Author:chen linfeng
# @File:高级类.py
from time import time, localtime, sleep
class person():
    def __init__(self,name,age):
        self._name = name
        self._age = age
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        self._age = age

    def play(self):
        if self._age <=16:
            print("%s正在玩游戏"%self._name)
        else :
            print(("%s正在吃饭"%self._name))

# 静态方法，定义在类中，但是在调用前实例对象并未被创建

class Triangle():
    def __init__(self,a,b,c):
        self.a = a
        self.b= b
        self.c = c
    @staticmethod
    def is_vaild(a,b,c):
        return a+b>c and a+c>b and b+c>a
    def permeter(self):
        return self.a +self.b+self.c
    def area(self):
        return  "it is ok!"

def main():
    a,b,c =3,4,5
    if Triangle.is_vaild(a,b,c):
        t=Triangle(a,b,c)
        print(t.permeter())
        print(t.area())
    else:
        print("it isnot ok")

def main1():
    people = person("chenlinfeng", 20)
    people.play()
    people.age = 13
    people.play()
    print(people.age, people.__dict__)



class Clock(object):
    """数字时钟"""
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second
    # 类方法，它代表的是当前类相关的信息的对象（类本身也是一个对象，有的地方也称之为类的元数据对象）
    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)
def main2():
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(3)
        clock.run()

if __name__ =='__main__':
    main1()
    main()
    main2()
