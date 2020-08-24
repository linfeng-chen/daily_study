import numpy as np
# 线性代数
# diag：以一维数组的形式返回方阵的对角线（或非对角线）元素，或将一维数组转换为方阵（非对角线元素为0）。
# dot：矩阵乘法。
# trace：计算对角线元素的和。
# det：计算矩阵行列式。
# eig：计算方阵的特征值和特征向量。
# inv：计算方阵的逆

# 矩阵相乘
a = np.arange(12)
b = a.reshape(3,4)
c = a.reshape(4,3)
# 矩阵b的第二维大小必须等于矩阵c的第一维大小
d = b.dot(c)#等价于np.dot(b,c)
print('a: \n{}'.format(a))
print('b: \n{}'.format(b))
print('c: \n{}'.format(c))
print('d: \n{}'.format(d))

# numpy.linalg  中有一组标准的矩阵分解运算以及诸如求逆和行列式之类的东西
# np.linalg.diag 以一维数组的形式返回方阵的对角线（或非对角线）元素，
# 或将一维数组转换为方阵（非对角线元素为0）

e = np.diag(d)
f = np.diag(e)
print('e: \n{}'.format(e))
print('f: \n{}'.format(f))

g = np.trace(d)#对角线之和
print(g)

h = np.linalg.det(d)#计算行列式
print(h)

# eig计算特征向量和特征值
i = np.linalg.eig(d)
print(i)
# inv计算矩阵的逆
temp = np.random.rand(3,3)
j = np.linalg.inv(temp)
print(j)

# Numpy文件保存
# 使用np.fromfile从文本文件'housing.data'读入数据
# 这里要设置参数sep = ' '，表示使用空白字符来分隔数据
# 空格或者回车都属于空白字符，读入的数据被转化成1维数组
# d = np.fromfile('./work/housing.data', sep = ' ')

# Numpy提供了save和load接口，直接将数组保存成文件(保存为.npy格式)，或者从.npy文件中读取数组。
# 产生随机数组a
a = np.random.rand(3,3)
np.save('../txt/a.npy', a)

# 从磁盘文件'a.npy'读入数组
b = np.load('../txt/a.npy')

# 检查a和b的数值是否一样
check = (a == b).all()
print(check)