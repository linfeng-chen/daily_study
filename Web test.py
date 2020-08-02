import numpy as np
import  matplotlib.pyplot as plt

x = np.arange(-10,10,0.1)
y = ((np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x)))

plt.figure(figsize=(8,3))
plt.plot(x,y,color='r')

# 添加文字说明
plt.text(-5.,0.9,r'$y =\tanh(x)$',fontsize =13)
# 设置坐标轴
currentAxis = plt.gca()
currentAxis.xaxis.set_label_text('x',fontsize =15)
currentAxis.yaxis.set_label_text('y',fontsize =15)
# plt.show()

p = np.random.rand(10,10)
print(p)
q = (p>0)
print(q)