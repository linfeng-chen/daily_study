# __get__():
#     触发时机：在访问对象成员属性（该成员已经交给描述符管理的时候）的时候触发
#     作用：设置当前属性获取的值
#     参数：self 描述符的对象  / 第二个 被管理成员的类的对象  / 第三个  被管理成员的类
#     返回值：可有可无，有的话就是获取的值
#     注意事项:无
#
# __set__():
#     触发时机：在设置对象成员属性（该成员已经交给描述符管理的时候）的时候触发
#     作用:对成员的值进行设置管理
#     参数：self 描述符的对象  / 第二个 被管理成员的类的对象  / 第三个  要设置的值
#     返回值：无
#     注意事项:设置值的时候一定要设置当前描述符对象的临时变量
#
# __delete__():
#     触发时机：在删除对象成员属性（该成员已经交给描述符管理的时候）的时候触发
#     作用:对成员的值进行删除管理
#     参数：self 描述符的对象  / 第二个 被管理成员的类的对象
#     返回值：无
#     注意事项:删除值的时候一定要删除当前描述符对象的临时变量

# 描述符的作用：
# 描述符的作用就是对类/对象中某个成员进行详细的管理操作

class Descriptor:
    #初始化一个临时的成员属性（代替原有username的操作）
    def __init__(self):
        self.tmpvar = '匿名用户'#属性随便给，这个就是控制的入口
    #定义描述符的三个成员
    def __get__(self,obj,cls):#self 描述符的对象  obj Email对象mail  cls Email类
        #希望获取用户名的时候仅仅返回第一个和最后一个字符 其余的都隐藏
        result = self.tmpvar[0] + '*' + self.tmpvar[-1]
        return result
    def __set__(self,obj,val):#self 描述符的对象   / obj Email对象mail  /val 要设置的值
        #设置值的时候一定要设置当前描述符对象的临时变量
        #限制用户名不能超过8个字符
        #检测字符个数
        if len(val) > 8:
            self.tmpvar = val[0:8]
        else:
            self.tmpvar = val
    def __delete__(self,obj):#self 描述符的对象/ obj Email对象mail
        #删除临时变量即可
        if obj.isallowdel_username == True:
            del self.tmpvar
    #声明一个类（邮箱）


class Email:
    #成员属性
    username = Descriptor()#用户名 交给描述符管理 [交接行为]
    #设置一个是否允许删除username的标志
    isallowdel_username = True
# 实例化对象
mail = Email()
# 访问用户名
print(mail.username)
# 设置用户名
mail.username = 'lovemybaby'
print(mail.username)
# 删除用户名的操作

del mail.username
#print(mail.username)