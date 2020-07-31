#魔法方法总是被__""__双下划线包围
# __init__(self,[])
# __new__(cls,[])创建类的实例时第一个执行的魔法，他的返回一个实例对象
# 当继承一个不可变类型又需要修改的时候

class Upper_(str):
    def __new__(cls,string):
        string = string.upper()
        return str.__new__(cls,string)

str_ = Upper_("chen linfeng")
print(str_)
# str类不是一个可更改的

# __del__(self) 析构==垃圾回收机制

