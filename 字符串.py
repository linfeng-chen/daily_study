
str="i tell you that 'python' is very good"
print(str)
#修改字符串大小写
#title():无参数，其作用是将每个单词的首字母改为大写
print(str.title())
#upper()将字符串全部改为大写
#lower()将字符串全部改为小写//在储存数据时很有用
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
import this