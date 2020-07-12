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

