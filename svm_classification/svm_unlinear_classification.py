#引入所需库
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
#这个文件创建方式点击这里
f=open("testSet2.txt")
data=[]
label=[]
#定义250000个点的二维点集
xx,yy=np.meshgrid(np.linspace(-3, 3, 500),np.linspace(-3, 3, 500))
#读取点
for i in f.readlines():
    linearr=i.strip().split()
    data.append([float(linearr[0]),float(linearr[1])])
    label.append(int(linearr[2]))
data=np.array(data)
#建立模型，核函数默认
clf = svm.SVC()
#训练数据
clf.fit(data, label)
#根据250000个点得到距离超平面距离
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
#结果转为二维
Z = Z.reshape(xx.shape)
#画出平面上距离超平面为0的轮廓
contours = plt.contour(xx, yy, Z, levels=[0], linewidths=2,linetypes='--')
#画点集
plt.scatter(data[:, 0], data[:, 1], s=30, c=label, cmap=plt.cm.Paired)
plt.show()