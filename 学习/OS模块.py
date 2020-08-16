# OS模块中关于文件/目录常用的函数使用方法:
import os

# getcwd():返回当前工作目录
print(os.getcwd())
# chdir()：改变工作目录
os.chdir("D:\\")
print(os.getcwd())
os.chdir("C:\\Users\付与千钟\PycharmProjects\\untitled")
print(os.getcwd())
# listdir()列举指定目录中的文件名(.表示当前目录，'..'表示上一级目录)
print(os.listdir())
