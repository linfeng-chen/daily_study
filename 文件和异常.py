#读取文件

with open('D:\新建文件夹\python\\no.txt') as file_object:
    contents= file_object.read()
    print(contents)

# 逐行读取
filename = 'pi_digist.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())