class HouseItem:
    '''这是一个家具类'''
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        return "[%s]占地%.2f"%(self.name,self.area)


class House:
    '''这是一个房子类'''
    def __init__(self,model,area):
        self.furniture_list = []
        self.model = model
        self.area = area
        self.free_area = area

    def add_item(self,furniture):
        print("添加家具%s"%furniture)
        if furniture.area>self.free_area:
            print("%s的占地面积太大了"%furniture.name)
            return
        self.free_area -= furniture.area
        self.furniture_list.append(furniture.name)


    def __str__(self):
        return ("户型：%s\n总面积：%d[剩余面积：%.2f]\n家具名称：%s"
                %(self.model,self.area,self.free_area,self.furniture_list))


# 创建家具
bed = HouseItem("席梦思",4)
chest = HouseItem("衣柜",2)
table = HouseItem("餐桌",1.5)
print(bed,chest,table)
# 创建房子
my_home = House("别墅",200)
print(my_home)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)
