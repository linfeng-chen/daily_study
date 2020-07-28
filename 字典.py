alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
#字典是一系列键-值对，每个键与一个值相关联，可将任何对象用作字典的值
# 添加键值对
alien_0['x_position']=0
alien_0["y_position"]=25
print(alien_0)
# 修改字典中的值
alien_0['color']='yellow'
print(alien_0)
# 删除键值对
del alien_0['points']
print(alien_0)
# 遍历字典
# 声明两个变量用于储存键值对中的键和值
user_0={'username':'chenlinfeng',
        'first':'chen',
        'last':'linfeng',
        }
for key,value in user_0.items():
    print("\nkey: "+key)
    print("value: "+value)
# 若只需要遍历字典的键时，可用keys()
for key in user_0.keys():
    print("the key is "+key)
for key in user_0:
    print("the key is ".title() + key)
# 上面两种方法均可以遍历键，但用key()更显而易见
# key()返回一个列表，其中包含字典的所有键
key =user_0.keys()
print(key)
print("first" in key)
# 在获取字典的元素时，获取顺序是不可预测的，要以特定的顺序返回元素，一种方法是在for循环中对返回的键排序
favorite={'jen':'python',
          'sarch':'c',
          'ewad':'ruby',
          'bob':'python',
          }
for name in sorted(favorite.keys()):
    print(name.title()+" join")

# 遍历字典的值，可用value()
for language in favorite.values():
    print(language.title())
# 当字典中含有大量重复值时，可用集合set()进行操作，其返回值是一个字典
for language in set(favorite.values()):
    print(language.title())
language=set(favorite.values())
print(language)

# 创建字典
dict1=dict(((1,'wd'),(2,"sf"),(3,"dfdf")))
print(dict1)
# fromkeys(s,[v])
dict2={}
dict2=dict2.fromkeys((1,2,3),'num')
print(dict2)
# 所有键对应后面的同一个值

# setdefault 检查字典是否含有这个键值对,若没有,则添加进去
dict2.setdefault(4,"sdsd")
print(dict2)
# updata也可添加键值对

# 集合：元素具有唯一性，但数值具有随机性，不支持索引
# 创建集合
set1 = set([1,2,3,4,2,1,])
print(set1)
# 不可变集合:frozenset()
set1.add(0)
set1= frozenset([1,2,3,4])
set1.add(22)
print(set1)
