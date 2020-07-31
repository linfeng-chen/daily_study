import numpy as np
# 多维ndarray数组的索引和切片
# 在多维数组中，各索引位置上的元素不再是标量而是多维数组。
# 以逗号隔开的索引列表来选取单个元素。
# 在多维数组中，如果省略了后面的索引，则返回对象会是一个维度低一点的ndarray

a = np.arange(30)
arr3d = a.reshape(5,3,2)
print(arr3d)

# 只有一个索引指标时，会在第0维上索引，后面的维度保持不变
print(arr3d[0])
print(arr3d[1])
# 两个索引指标
print(arr3d[0][1])
# 三个索引
print(arr3d[0][1][1])
print(arr3d.shape)

# 多维ndarray数组的切片

a = np.arange(30)
print(a)
a = a.reshape(6,5)
print(a)
print(a[0:2])
print(a[0:2,1:])


print('\n')
x = [ i for i in range(0,6,2)]
print(x)


# 使用for语句对数组进行切片
# 下面的代码会生成多个切片构成的list
# k in range(0, 6, 2) 决定了k的取值可以是0, 2, 4
# 产生的list的包含三个切片
# 第一个元素是a[0 : 0+2]，
# 第二个元素是a[2 : 2+2]，
# 第三个元素是a[4 : 4+2]
slices = [a[k:k+2] for k in range(0, 6, 2)]
print(slices)
print(slices[0])


