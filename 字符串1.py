#字符串替换
# 字段名：索引或标识符，指出要设置哪个值的格式并使用结果来替换该字段。除指定值
# 外，还可指定值的特定部分，如列表的元素。

# 转换标志：跟在叹号后面的单个字符。当前支持的字符包括r（表示repr）、s（表示str）
# 和a（表示ascii）。如果你指定了转换标志，将不使用对象本身的格式设置机制，而是使
# 用指定的函数将对象转换为字符串，再做进一步的格式设置。

# 格式说明符：跟在冒号后面的表达式（这种表达式是使用微型格式指定语言表示的）。格
# 式说明符让我们能够详细地指定最终的格式，包括格式类型（如字符串、浮点数或十六
# 进制数），字段宽度和数的精度，如何显示符号和千位分隔符，以及各种对齐和填充方式。
# 下面详细介绍其中的一些要素。
import math


x = "{fool}{}{bar}{}".format(1,2,fool=3,bar=5)
print(x)
# 注意未命名参数要按顺序

x = "{pi!s}{pi!r}{pi!a}".format(pi="Π")
print(x)
# 函数str通常创建外观普通的字符串版本（这里没有对输入字符串做任何处理）。函数repr尝试创建给定值的Python表
# 示（这里是一个字符串字面量）。函数ascii创建只包含ASCII字符的表示

x = "{num:f}".format(num=23) #f表示定点数
print(x)
x = "{num:b}".format(num=23) #b表示二进制数
print(x)
# f 将小数表示为定点数
# F 与f相同，但对于特殊值（nan和inf），使用大写表示
# g 自动在定点表示法和科学表示法之间做出选择。这是默认用于小数的说明符，但在默认情况下至少有1位小数
# G 与g相同，但使用大写来表示指数和特殊值
# n 与g相同，但插入随区域而异的数字分隔符
# o 将整数表示为八进制数
# s 保持字符串的格式不变，这是默认用于字符串的说明符
# x 将整数表示为十六进制数并使用小写字母
# X 与x相同，但使用大写字母
# % 将数表示为百分比值（乘以100，按说明符f设置格式，再在后面加上%）

# 在格式说明中指定宽度和精度
print("{:10}".format(10))   # 宽度使用整数指定,左对齐
print("{name:10}".format(name = "chen"))#字符串为右对齐

# 精度也是使用整数指定的，但需要在它前面加上一个表示小数点的句点。
print("{:10.2f}".format(20))

# 可使用逗号来指出你要添加千位分隔符。
print("{:,}".format(10**20))


#在指定宽度和精度的数前面，可添加一个标志。这个标志可以是零、加号、减号或空格，其中零表示使用 0来填充数字。
print("{:010.2f}".format(math.pi))
# 要指定左对齐、右对齐和居中，可分别使用<、>和^
print("{:<10.2f}".format(math.pi))
print("{:^10.2f}".format(math.pi))
print("{:<+10.2f}".format(math.pi))

# 可以使用填充字符来扩充对齐说明符，这样将使用指定的字符而不是默认的空格来填充。
print("{:@^10.2f}".format(math.pi))

# 说明符=，它指定将填充字符放在符号和数字之间。
print("{:=10.2f}\n{:#=10.2f}".format(math.pi,-math.pi))


width =10# int(input('Please enter width: '))
price_width = 10
item_width = width - price_width
header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width)
fmt = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)

print(header_fmt)
print(fmt)

