#定义函数
def greetuser():
    """打印一行消息"""
    print("hello friend")
greetuser()
# 向函数传递信息
def greetuser(username):
    print("hello friend "+username.title()+"!")
greetuser('chenlinfeng')
# 实参和形参
# 在上述代码中，username 是一个形参——函数完成工作所需的一项信息
# 在调用函数时所传入的叫实参
# 传递实参：
# 1.位置实参：按照顺序将实参与形参相关联
def describe_pets(pet_type,pet_name):
    '''显示宠物信息'''
    print("\nI have a "+pet_type +'.')
    print("Its name is "+pet_name)
describe_pets('dog','噬元兽')
# 2.关键字实参：关键字实参是传递给函数的名称-值对
describe_pets(pet_type='cat',pet_name='shiyuanshou')
# 3.默认值：若某个形参具有特定值，可直接给形参指定默认值，这样在传入实参时仅仅需要其他待指定的值
def describe_pets(pet_name,pet_type='dog'):
    '''显示宠物信息'''
    print("\nI have a "+pet_type +'.')
    print("Its name is "+pet_name)
    '''注意指定实参值的形参应放在后面'''
describe_pets(pet_name='bob')
describe_pets('bob')
describe_pets(pet_name='tom',pet_type='cat')
# 仍然可以传入给定了实参的值的形参另一个值

# 返回值
def formatted_name(first_name,last_name):
    return first_name.title()+" "+last_name.title()
need=formatted_name('chen','linfeng')
print(need)
# 返回字典
def formatter_person(first_name,last_name,age=''):
    person={'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person
people=formatter_person('chen','lineng',20)
print(people)

while True:
    print("请输入你想要使用的名字:")
    print("输入over结束！")
    first=input("姓: ")
    if first=='over':
        break;
    last=input("名: ")
    if last=='over':
        break
    name=formatted_name(first,last)
    print("\nHello friends:"+name)

# 禁止函数修改列表：将副本传给函数而非本体
# 切片表示法[:]创建列表副本
def suring_name(unsure_name,sured_name):
    while unsure_name:
        current_name=unsure_name.pop()
        print("正在确定名字:"+current_name)
        sured_name.append(current_name)


unsure_name = ['bob', 'tom', 'jike', 'lihua']
sured_name=[]
suring_name(unsure_name[:],sured_name)
print(unsure_name)
print(sured_name)
# 传递任意数量的实参
# 当函数不知道用户需要输入多少实参时，使用形参*name
def make_pizza(*toppings):
    '''打印顾客点的所有配料'''
    print(toppings)
make_pizza("pepepepe")
make_pizza('sdssd','sdfdg','meat')
'''形参名的 * 让python创建一个空元组，并将所收到的所有值封装到这个元组中'''
def make_pizza(*toppings):
    '''打印顾客点的所有配料'''
    for topping in toppings:
        print("\t"+topping)
make_pizza("pepepep")
make_pizza("meat",'drunk','peat')

# 混合使用位置实参与任意数量实参
# 函数需要接收不同类型的实参时，必须将接纳任意实参的形参放到最后
def make_pizza(size,*toppings):
    '''打印顾客点的所有配料'''
    for topping in toppings:
        print("\t"+str(size)+' size '+' '+topping)

make_pizza(15,"meat",'peat','mosd')
# 使用任意数量的关键字实参
# 当不知道传递给函数的是什么样的信息时，可将函数编写成能够接收任意数量键值对
def build_user(name,**infomation):
    '''创建一个字典用来存储用户信息'''
    peoson={}
    peoson['name']=name.title()
    for key,value in infomation.items():
        peoson[key.title()]=value
    return peoson
person=build_user('chen linfeng',location="beijin",age=20)
print(person)
# 形参的 ** 创建一个空字典

# 将函数储存在模块中
# 要让函数是可导入的，得先创建模块，模块为.py的未见，包含要导入到程序的代码
# module_name.funcation_name() 模块名称.功能名称（）
# 导入特定函数
# from module_name import funcation_name
# from module_name import funcation_0,funcation_1
# 当使用上述两种方法时，在使用时无需写出模块名称，即文件名
# 使用（*）导入所有函数 from moudle_name import *
# 使用 as 给函数指定别名
# from module_name.import funcation_name as need_name
# 使用as 给模块指定别名
# import moudle_name as need_name


# 匿名函数
# lambda 表达式
def add(number):
    return number**2
print(add(5))
x=lambda number:number**2
print(x(5))
# lambda 表达式可以将函数转换为简单形式

# filter() 过滤器
help(filter)
# filter(function,可迭代对象)
# 1.当function 为none时,返回值为真的对象
x=list(filter(None,[1,2,3,0,True]))
print(x)
# 2.当function 有定义时,需要将可迭代对象代入函数进行筛选
def choice(x):
    return x%2
temp=range(10)
show=list(filter(choice,temp))
print(show)
temp=range(20)
show=list(filter(lambda x:x%2,temp))
print(show)

# map()映射
show=list(map(lambda x:x**2,temp))
print(show)