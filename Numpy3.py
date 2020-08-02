import numpy as np
# ndarray数组的统计方法
# mean：计算算术平均数，零长度数组的mean为NaN。
# std和var：计算标准差和方差，自由度可调（默认为n）。
# sum ：对数组中全部或某轴向的元素求和，零长度数组的sum为0。
# max和min：计算最大值和最小值。
# argmin和argmax：分别为最大和最小元素的索引。
# cumsum：计算所有元素的累加。
# cumprod：计算所有元素的累积。

arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(arr.shape)
print(arr.mean(),np.mean(arr))
print(arr.sum(),np.sum(arr))
print(arr.max(),arr.min())

# # 指定计算的维度
# # 沿着第1维求平均，也就是将[1, 2, 3]取平均等于2，[4, 5, 6]取平均等于5，[7, 8, 9]取平均等于8
# arr.mean(axis = 1)

print(arr.mean(axis=1),arr.mean(axis=0))

# 沿着第0维求和，也就是将[1, 4, 7]求和等于12，[2, 5, 8]求和等于15，[3, 6, 9]求和等于18
print(arr.sum(axis=0),arr.min(axis=0),arr.max(axis=0))
print(arr.std(),arr.var())
# 找出最大元素的索引
print(arr.argmax(),arr.argmax(axis=0),arr.argmax(axis=1))


# 随机数np.random
# 设置随机数种子
np.random.seed(10)
a = np.random.rand(3, 3)
print(a)   # 如果不设置随机数种子，观察多次运行输出结果不一致


# 均匀分布
# 生成均匀分布随机数，随机数取值范围在0~1之间
a = np.random.rand(3,3)
print(a)
# 生成均匀分布随机数，指定随机数取值范围和数组形状
a = np.random.uniform(low=-8.0,high=1.0,size=(2,2))
print(a)

# 生成标准正态分布随机数
a = np.random.randn(3,3)
print(a)
# 生成正态分布随机数，指定均值loc和方差scale
a = np.random.normal(loc=1.0,scale=1.0,size=(3,3))
print(a)

# 随机打乱ndarray数组顺序
a = np.arange(0,30)
print('before:',a)
np.random.shuffle(a)
print("after:",a)

a = np.arange(0,30)
a=a.reshape(10,3)
print(a)
np.random.shuffle(a)
print(a)
# 随机打乱2维ndarray数组顺序，发现只有行的顺序被打乱了，列顺序不变

a = np.arange(30)
b = np.random.choice(a,size=5)
print(b)