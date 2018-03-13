import numpy as np
import matplotlib.pyplot as plt

num=1000
vectors=[]
xx=0;xy=0;ex=0;ey=0

#沿线随机产生点
for i in range(num):
	x1=np.random.normal(0.0,0.55)
	y1=x1*0.1+0.3+np.random.normal(0.0,0.03)
	xx+=x1*x1
	xy+=x1*y1
	ex+=x1
	ey+=y1
	vectors.append([x1,y1])
x_data=[v[0] for v in vectors]
y_data=[v[1] for v in vectors]
plt.plot(x_data,y_data,'r.',label='data')

#求参数a,b  y=bx+a
b=(xy-ex*ey/num)/(xx-ex*ex/num)
a=ey/num-b*ex/num

#画图
tmpx=[-2,0,2]
tmpy=[]
for i in tmpx:
	tmpy.append(b*i+a)
plt.plot(tmpx,tmpy)
plt.legend()
plt.show()