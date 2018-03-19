#引入所需库
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
#点集和类别
f=open("testSet.txt")
data=[]
label=[]
#取点
for i in f.readlines():
    linearr=i.strip().split()
    data.append([float(linearr[0]),float(linearr[1])])
    label.append(int(linearr[2]))
data=np.array(data)
#建立线性模型
clf = svm.SVC(kernel='linear')
#训练
clf.fit(data, label)
#取到训练完的权值
w = clf.coef_[0]
a = -w[0] / w[1]
#设定x坐标
xx = np.linspace(-5, 5)
#根据权值求得y
yy = a * xx - (clf.intercept_[0]) / w[1]
#画直线
plt.plot(xx, yy, 'k-')
#画点集
plt.scatter(data[:, 0], data[:, 1], s=30, c=label, cmap=plt.cm.Paired)
plt.show()