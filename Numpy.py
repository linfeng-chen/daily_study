import numpy as np

a = np.array([1,2,3,4])
b = np.array([10,202,23,311])
print(a)
print(b)
print(a+b) #对应相加
# ndarray 数组
# ndarray数组支持广播机制，矩阵运算时不需要写for循环。
# Numpy底层使用C语言编写，内置并行计算功能，运行速度高于Python代码

# 实现整体加减运算
a = a+1
print(a)
a = a*2
print(a)

# 自动广播机制
# ndarray数组还提供了广播机制，它会按一定规则自动对数组的维度进行扩展以完成计算。
d = np.array([[1,2,3,4,5],[6,7,8,9,10]])# 二维数组
c = np.array([[4,5,6,7,8],[1,2,3,4,5]])#一维数组
print(d+c)


# array:：创建嵌套序列（比如由一组等长列表组成的列表），并转换为一个多维数组。
a = [1,2,3,4,5]
b = [2,3,4,5,6]
c = np.array([a,b])
print(c)

# arange:创建元素从0到10依次递增2的数组。
a = np.arange(0,10,1)
print(a)
# zeros:创建指定长度或者形状的全0数组。
a = np.zeros([3,3])
print(a)
# ones:创建指定长度或者形状的全1数组

# ndarray的属性包括shape、dtype、size和ndim等，通过如下代码可以查看ndarray数组的属性。
# shape：数组的形状 ndarray.shape，1维数组（N, ），二维数组（M, N），三维数组（M, N, K）。
# dtype：数组的数据类型。
# size：数组中包含的元素个数 ndarray.size，其大小等于各个维度的长度的乘积。
# ndim：数组的维度大小，ndarray.ndim, 其大小等于ndarray.shape所包含元素的个数。

a = np.ones([3,3,3])
print(a+a)
print('a,dtype:{},shape:{},size:{},ndim:{}'.format(a.dtype,a.shape,a.size,a.ndim))


# numpy.random.rand()
# 官方文档中给出的用法是：numpy.random.rand(d0,d1,…dn)
# 以给定的形状创建一个数组，并在数组中加入在[0,1]之间均匀分布的随机样本。
b = np.random.rand(10,10)
print(b)

# 改变ndarray数组的数据类型和形状
a  =  a.astype(np.int64)
print('a,dtype:{},shape:{},size:{},ndim:{}'.format(a.dtype,a.shape,a.size,a.ndim))

a = a.reshape([1,27])#保证数据大小一致（size)
print('a,dtype:{},shape:{},size:{},ndim:{}'.format(a.dtype,a.shape,a.size,a.ndim))

d = np.array([[1,2,3,4,5],[6,7,8,9,10]])# 二维数组
c = np.array([[4,5,6,7,8],[1,2,3,4,5]])#一维数组
print(d+c)
print(c.shape)
print(d*c)
print(d/c)
print(d**0.5)

# ndarray数组的索引和切片的使用方式与Python中的list类似。
# 通过[ -n , n-1 ]的下标进行索引，通过内置的slice函数，
# 设置其start,stop和step参数进行切片，从原数组中切割出一个新数组

a = np.arange(30)
b = a[10]
print(b)
b = a[4:7]
print(b)
#将一个标量值赋值给一个切片时，该值会自动传播到整个选区。
a = np.arange(30)
a[4:7] = 10
print(a)

# 数组切片产生的新数组，还是指向原来的内存区域，数据不会被复制。
# 视图上的任何修改都会直接反映到源数组上。
a = np.arange(30)
arr_slice = a[4:7]
arr_slice[0] = 100
print(a, arr_slice)#可以看到原数组中a[4]已经被更改

# 通过copy给新数组创建不同的内存空间
a = np.arange(30)
arr_slice = a[4:7]
arr_slice = np.copy(arr_slice)
arr_slice[0] = 100
print(a, arr_slice)#此时原数组没有被改变


