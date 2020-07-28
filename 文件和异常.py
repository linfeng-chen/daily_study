#读取文件

# with open('D:\新建文件夹\python\\no.txt') as file_object:
#     contents= file_object.read()
#     print(contents)

# 逐行读取
filename = 'txt/pi_digist.txt'
with open(filename) as file_object:
    for i in file_object:
        print(i.rstrip())

with open(filename) as file_object:
    x = file_object.readline()
    print(x)
    num =file_object.tell()
    print(num)
    file_object.seek(23,0)
    num = file_object.tell()
    print(num)

# 使用关键字with时，文件对象只在with代码块中可用
# 可将文件各行存储再列表中
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
print(lines,type(lines))
# 使用文件内容

pi_string=''
for line in lines:
    pi_string += line.strip()

print(pi_string,len(pi_string),end='')
# 写入文件
# 要将文本写入文件，你在调用open()时需要提供另一个实参，告诉Python你要写入打开的文件
# 'w'表示写入模式，'r'表示只读模式，'a'附加模式，'r+'表示可读可写
# writelines()

filename = 'program.txt'
with open(filename,'w') as file_object:
    file_object.write("I love python\n")
    file_object.writelines(["2323","4523"])


print("\n")
with open(filename,'a') as file_object:
    file_object.write('\nI love python because i want to do something i like')
    while True :
        name = input("请输入名字/输入over结束：")
        if name=='over':
            break
        else:
            file_object.write('\n'+name)

# 异常处理
# 处理ZeroDivisionError错误
# print(5/0)
# 使用try-except代码块

try:
    print(5/0)
except ZeroDivisionError:
    print("0不能做除数")

# else 代码块
while True:
    first_number = input("输入第一个数/输入q退出：")
    if first_number =='q':
        break
    second_number = input("请输入第二个数：")
    if second_number =='q':
        break
    try:
        print(int(first_number)/int(second_number))
    except ZeroDivisionError:
        print("0不能做除数")
    else:
        print(int(first_number)/int(second_number))

# 处理FileNotFoundError错误
#
# with open("ailen.txt") as f_obj:
#      contents = f_obj.read()

try:
    with open("ailen.txt") as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg="Sorry,there is no this file"
    print(msg)

# 分析文本
title = 'chen linfengisastudenthelikecomputer'
(first,second) = title.split(" ")
print(first)
# 在执行遇到错误时不执行任何语句
# pass 语句，其还可充当占位符
# f.seek(offest,from),from(0表示起始位置，1代表当前位置，2代表文件末尾，偏移offset个字节
# f.tell()




