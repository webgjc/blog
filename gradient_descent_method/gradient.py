#python2.7
#产生点
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-2,2,0.1)
y=2*x+np.random.random(len(x))
#随机设定一个初始的a，b
a=np.random.random()
b=np.random.random()
l=len(x)
#步长
alpha=0.01
#进行1000次梯度下降，每次计算出上面求出的偏导，并在赋值给a,b。
for _ in range(1000):
    j=0
    k=0
    for i in range(l):
        j+=(a*x[i]+b-y[i])*x[i]
        k+=a*x[i]+b-y[i]
    a=a-alpha*j/l
    b=b-alpha*k/l
    print(a,b)
#画点
plt.plot(x,y,"ro")
#画线
tmpx=np.linspace(-2,2)
tmpy=tmpx*a+b
plt.plot(tmpx,tmpy)
plt.show()