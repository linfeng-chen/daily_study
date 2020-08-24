words=["apple","bat","bar","atom","book"]
by_letter = {}
for word in words:
    letter= word[0]
    if letter not in by_letter:
        by_letter[letter]=[word]
    else:
        by_letter[letter].append(word)
print(by_letter)
# setdefault方法
# Python 字典 setdefault() 函数和 get()方法 类似, 如果键不存在于字典中，将会添加键并将值设为默认值。
# dict.setdefault(key, default=None)
# key -- 查找的键值。
# default -- 键不存在时，设置的默认键值。

by_letter1={}
for word in words:
    letter=word[0]
    by_letter1.setdefault(letter,[]).append(word)

print(by_letter1)

# collections 模块有一个很有用的类， defaultdict ，它可以进一步简化上
# 面。传递类型或函数以生成每个位置的默认值
from collections import  defaultdict

by_letter2 = defaultdict(list)
for word in words:
    by_letter2[word[0]].append(word)

print(by_letter2)

# 可以用 hash 函数检测一个对象是否是可哈希的（可被用作字典的键）
print(hash("shishi"))
# print(hash([1,2,3])) 列表不可哈希

# 柯里化:部分参数应用
def add_numbers(x,y):
    return x+y
# 通过这个函数，我们可以派生出一个新的只有一个参数的函数——add_five，它用
# 于对其参数加5：

add_five = lambda y:add_numbers(5,y)
print(add_five(4))
# 内置的functools模块可以用partial函数将此过程简化：
from functools import partial
add_five = partial(add_numbers,5)

# itertools模块：
# 标准库itertools模块中有一组用于许多常见数据算法的生成器。例如，groupby可以
# 接受任何序列和一个函数。它根据函数的返回值对序列中的连续元素进行分组。
import  itertools
import itertools
first_letter = lambda x:x[0]
names = ['Alan','Adam','Wes','Will','Albert','Steven']
for letter,names in itertools.groupby(names,first_letter):
    print(letter,list(names))
