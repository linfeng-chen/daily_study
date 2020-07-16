#导入类
# 将类储存在模块中
# 1.导入单个类
# car.py 与my_car.py 演示
# 2.可在一个模块中储存多个类
# 3.在一个模块中导入多个类
from collections import OrderedDict
'''这个类可以记录字典添加顺序'''
favorite_language = OrderedDict()
favorite_language['jen']='python'
favorite_language['mike']='C'
favorite_language['bob']='ruby'
favorite_language['cell']='c++'

for name,language in favorite_language.items():
    print(name.title()+' likes the '+ language.title())

# help(OrderedDict)
# 类名应采用驼峰命名法，即将类名中的每个单词的首字母都大写，而不使用下划线。实例名 和模块名都采用小写格式，并在单词之间加上下划线。
# 对于每个类，都应紧跟在类定义后面包含一个文档字符串。这种文档字符串简要地描述类的功能，并遵循编写函数的文档字符串时采用的格式约定。每个模块也都应包含一个文档字符串，
# 对其中的类可用于做什么进行描述。
# 可使用空行来组织代码，但不要滥用。在类中，可使用一个空行来分隔方法；而在模块中，可使用两个空行来分隔类。
# 需要同时导入标准库中的模块和你编写的模块时，先编写导入标准库模块的import语句，再 添加一个空行，然后编写导入你自己编写的模块的import语句。在包含多条import语句的程序中，
