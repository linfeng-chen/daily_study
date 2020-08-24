import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# ReLU和Sigmoid激活函数示意图
plt.figure(figsize=(8,3))
# x是一维数组，数组大小从-10到10的实数，每隔0.1去一个点
x = np.arange(-10,10,0.1)
# 计算sigmoid函数
s = 1.0/(1+np.exp(-x))
# 计算ReLu函数
y = np.clip(x,a_min=0,a_max=None)

# #画图
f = plt.subplot(121)
plt.plot(x,s,color = 'r')
# 添加文字说明
plt.text(-5.,0.9,r'$y =\sigma(x)$',fontsize =13)
# 设置坐标轴
currentAxis = plt.gca()
currentAxis.xaxis.set_label_text('x',fontsize =15)
currentAxis.yaxis.set_label_text('y',fontsize =15)

# 将ReLU的函数图像画在右边
f = plt.subplot(122)
# 画出函数曲线
plt.plot(x, y, color='g')
# 添加文字说明
plt.text(-3.0, 9, r'$y=ReLU(x)$', fontsize=13)
# 设置坐标轴格式
currentAxis=plt.gca()
currentAxis.xaxis.set_label_text('x', fontsize=15)
currentAxis.yaxis.set_label_text('y', fontsize=15)

# plt.show()

