
str="i tell you that 'python' is very good"
print(str)
#修改字符串大小写
#title():无参数，其作用是将每个单词的首字母改为大写
print(str.title())
#upper()将字符串全部改为大写
#lower(),casefold()将字符串全部改为小写//在储存数据时很有用
print(str.upper())
print(str.lower())
#拼接字符串
s_1="happy and pleased"
print(s_1+str)
print("1123456"+" "+"iky")
#使用制表符或换行符添加空白
print("python")
print("\tpython")
print("languages:\npython\nc++\njava")
print("languages:\n\tpython\n\tc++\n\tjava")
#删除空白区域
#rstrip()清除末尾空格
#lstrip()清除开头空格
# strip()清除末尾与开头的空格
lang=" python "
print(lang)
lang=lang.rstrip()
print(lang)
lang=lang.lstrip()
print(lang+"\n")
# import this
# capitalize(),titile()将字符串第一个字符变成大写
str_1="chen linfeng linfeng"
str_1=str_1.capitalize()
print(str_1)
str_1="chen linfeng"
str_1=str_1.title()
print(str_1)

str_1="ABCDEF"
str_1=str_1.casefold()
print(str_1)
# center(wideth)将字符串居中
print(str_1.center(20))
# find(元素,start,end)
# isalpha()检查字符串是否全是字母
# isdecimal()检查是否只含十进制数
# isdigit()检查是否全是数字
# islower()当字符串包含一个区分大小写字符时，检查是否全是小写
# isupper()检查是否全是大写
# rfind(),rindex()同find,index，从右边开始检查

# 字符串格式化
str_1="{0} love {1} {2}".format("I","fish",'!')
print(str_1)
# 位置参数
# 关键字参数
str_1="{a} {b} {c}".format(a="chenlinfeng",b="is",c="student")
print(str_1)

str_2 = "{}".format("hello")
print(str_2)

# 混合使用位置参数与关键字参数时需要将位置参数在前
num="{0:.2f} {1}".format(23.2332,"not")
print(type(num),num)
# 字符串格式化意义
# %c 格式化字符
# %s 格式化字符串
# %d 格式化整数 %o 格式化八进制数
print('%s %s %s' %(934,956,9))
print('%s %s %s'%("sdsd","sdsdf","fgfg"))
print('%c'%97)

e = 2.7344234234
print(f"test is {e}") #与"test is {e}.".format(e=e)等效


# enumerate()
num=[1,3,45,8,56,234,5]
num=dict(enumerate(num))
print(num)
# zip

# eval(),将字符串转化为表达式
expr = "2**5"
print((eval(expr)))

# center在两边添加字符让字符串居中
print("chen linfeng".center(16,'*'))

# 方法translate与replace一样替换字符串的特定部分，但不同的是它只能进行单字符替换。
# 这个方法的优势在于能够同时替换多个字符，因此效率比replace高。

# 使用translate前必须创建一个转换表。这个转换表指出了不同Unicode码点之间的转换关系
# 方法maketrans，这个方法接受两个参数：两个长度相同的字符串，它们指定要将第一个字符串中的每个字符都替换为第二个字符串中的相应字符

table = str.maketrans("cs","kz"," ")#第三个参数将指定字母删除
print(table)
x = "this is my creaze son".translate(table)
print(x)

