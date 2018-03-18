#python2.7
#引入必要文件
import matplotlib.pyplot as plt
import numpy as np
#打开文件
f=open("testSet.txt")
gdatax=[]
gdatay=[]
rdatax=[]
rdatay=[]
label=[]
data=[]
#读取文件
for i in f.readlines():
    #strip()是除去开头空格，split()是以空格为间断，变成数组。
    linearr=i.strip().split()
    #读取坐标，这里补1.0是为了使数组长度变成3，便于之后矩阵运算
    data.append([1.0,float(linearr[0]),float(linearr[1])])
    #读取分类
    label.append(int(linearr[2]))
    #为了展示点的分布，分开读取不同类的点
    if int(linearr[2])==1:
        gdatax.append(linearr[0])
        gdatay.append(linearr[1])
    else:
        rdatax.append(linearr[0])
        rdatay.append(linearr[1])
#使list变成numpy里的matrix矩阵
dataMatrix=np.mat(data)
#transpose()是矩阵的转置
labelMat=np.mat(label).transpose()
m,n=np.shape(dataMatrix)
#梯度下降步长
alpha=0.001
#梯度下降次数
max=500
#先设定三个系数为1
weights=np.ones((n,1))
#梯度下降主步骤，求sigmoid，和分类对比正确性，在求新的weights
for k in range(max):
    h=1.0/(1+np.exp(-dataMatrix*weights))
    error=(labelMat-h)
    weights=weights+alpha*dataMatrix.transpose()*error
#创建等差数列
x=np.linspace(-3,3)
#计算y值
y=(-weights[0,0]-weights[1,0]*x)/weights[2,0]
#画图
plt.plot(x,y)
plt.plot(gdatax,gdatay,'ro',c='g')
plt.plot(rdatax,rdatay,'ro',c='r')
plt.show()