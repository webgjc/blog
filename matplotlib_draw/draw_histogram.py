import numpy as np
import matplotlib.pyplot as plt
#得到测试点
x=np.linspace(0,5,10)
y=np.sin(x)
z=2*x
#画柱状图
plt.bar(x,z,width=0.1,bottom=None,align='center')
#画柱状大小的描述
for i,j in zip(x,z):
    plt.text(i,j,"%.2f"%j,ha='center',va='bottom')
plt.show()