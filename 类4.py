class Username():
    def __init__(self,first,last):
        self.first = first
        self.last = last
        self.__age = 20

    def format_name(self):
        print("The name is "+"{} {}".format(self.first.title(),self.last.title()))
        print('The name is '+'%s %s' %(self.first,self.last))

one_people = Username('chen','linfeng')
one_people.format_name()

# ?如何访问私有成员:_类名__变量名
print(one_people._Username__age)
