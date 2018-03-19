#coding:utf-8
#引入相关库
import matplotlib.pyplot as plt
import numpy as np
#读取文件中的点坐标及分类
f=open("testSet.txt")
#两类点坐标
gdatax=[]
gdatay=[]
rdatax=[]
rdatay=[]
#类别
label=[]
#点坐标
data=[]
#代表有5个θ
N=5
#θ的矩阵
A=np.array([1]*N)
#步长，这里设的比较大因为小了到不了最低点
alpha=0.1
#不同类的点画不同颜色的点
for i in f.readlines():
    linearr=i.strip().split()
    data.append([float(linearr[0]),float(linearr[1])])
    label.append(int(linearr[2]))
    if int(linearr[2])==1:
        gdatax.append(linearr[0])
        gdatay.append(linearr[1])
    else:
        rdatax.append(linearr[0])
        rdatay.append(linearr[1])
l=len(label)
#迭代2000次，过程和上面一样
for _ in range(2000):
    z=np.zeros(N)
    for i in range(l):
        sh=1/(1+np.exp(-A[0]-data[i][0]*A[1]-data[i][1]*A[2]-A[3]*data[i][0]**2-A[4]*data[i][1]**2))
        z[0]+=sh-label[i]
        z[1]+=(sh-label[i])*data[i][0]
        z[2]+=(sh-label[i])*data[i][1]
        z[3]+=(sh-label[i])*data[i][0]**2
        z[4]+=(sh-label[i])*data[i][1]**2
    A=A-alpha*z/l
#下面为画图过程
tmpx=[i/10.0 for i in range(-30,30)]
tmpy=[]
tmpz=[]
for i in tmpx:
    su=A[2]**2-4*A[4]*(A[0]+A[1]*i+A[3]*i**2)
    if su<0:
        tmpy.append(0)
        tmpz.append(0)
    else:
        tmpy.append((-A[2]-np.sqrt(su))/(2*A[4]))
        tmpz.append((-A[2]+np.sqrt(su))/(2*A[4]))
plt.plot(tmpx,tmpy)
plt.plot(tmpx,tmpz)
plt.plot(gdatax,gdatay,'ro',c='g')
plt.plot(rdatax,rdatay,'ro',c='r')
plt.show()