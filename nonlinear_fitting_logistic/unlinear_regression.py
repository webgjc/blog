#引入相关库
import numpy as np
import matplotlib.pyplot as plt
#模拟产生点坐标
k=int(np.random.random()*5+1)
x=np.arange(-2,2,0.1)
y=0
for i in range(k):
    y+=np.random.random()*(x**k)
y+=np.random.random(len(x))
#N--幂指数也就是最高x^6
#这里可以改进，如果N再高计算中会出现nan
N=6
#这个矩阵为上面的θ
A=np.array([1]*N)
#点的数量
l=len(x)
#梯度下降步长
alpha=0.01
#进行一千次迭代
for _ in range(1000):
    #z为cost function叠加的那部分和的矩阵
    z=np.zeros(N)
    #遍历每个点，计算代价和
    for i in range(l):
        sh=0
        for j in range(N):
            sh+=A[j]*x[i]**j
        for m in range(N):
            z[m]+=(sh-y[i])*x[i]**m
    #直接用矩阵计算更新所有θ
    A=A-alpha*z/l 
#下面为画图部分
plt.plot(x,y,"ro")
tmpx=np.linspace(-2,2)
def cal(x):
    tmpy=0
    for i in range(N):
        tmpy+=A[i]*x**i
    return tmpy
tmpy=[cal(tmpx[i]) for i in range(len(tmpx))]
plt.plot(tmpx,tmpy)
plt.show()