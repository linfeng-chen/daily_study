x=3
print(x)
幸运数 = 4
print(幸运数)#可以使用中文当作变量
print("you are pig")
print("let's go!")
x=5
y=8
x, y=y, x
print(x,y)
print(x*y,x+y)
print("let\n go")
print("\"let")#使用转义字符

print("D:\three\two\one\now")
#改进版
print(r"D:\three\two\one")#加入r可以使后面按原始字符串输出
#反斜杠\在末尾代表语句未结束
print(" such a pig\nyou are beautiful")
print("sdsd"
      "dfgh"
      "sdsfdgf")
print("abcd        \n"
      "sdsdsad")
#长字符串
poetry="""
都将万事，付与千钟
大鹏一日同风起，扶摇而上九千里
"""
print(poetry)#自动换行
trim="只问朝夕"
print(poetry+trim)#字符串加法即使串接
print(poetry*9)
def mult_two(a,b):
      return a*b
x=input()
y=input()
x=int(x)
y=int(y)
print(mult_two(x,y))