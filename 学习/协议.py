#容器类型的协议:
# 如果需要定制的容器是不可变的，则只需定义__len()__,和__getitem__()方法
# 如果需要定制的容器是可变的，则需定义__len()__,__getitem__(),__setitem__(),__delitem__()方法

class List_count:
    def __init__(self,*args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)),0)
    def __len__(self):
        return len(self.values)
    def __getitem__(self, keys):
        self.count[keys] +=1
        return self.values[keys]

c1 = List_count(1,2,3,5,6,7)
c2 = List_count(3,5,7,2,2,1)

print(c1[1])
print(c2[1])

print(c1[1]+c2[1])
print(c1.count,c2.count)

# help(list)