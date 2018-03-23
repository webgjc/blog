import numpy as np
import matplotlib.pyplot as plt
#得到测试点
x=np.linspace(-5,5,50)
y=np.sin(x)
z=2*x

#设置画板大小
plt.figure(figsize=(6,6))
#用plot画图,前两个参数为数据的x和y值
#第三个参数为三个属性的结合：颜色如(b，g，r)+标记如(.，o，,)+连线如(-，--，-.)
#label为线条说明，markersize为标记大小，linewidth为连线大小
plt.plot(x,y,"go-",label="yyy",markersize=2,linewidth=1)
plt.plot(x,z,"b.-",label="zzz")

#坐标轴显示范围
plt.axis([-5,5,-5,5])
#设置坐标轴刻度
plt.xticks([-5,0,5])
plt.yticks([-5,0,5],["bad","normal","good"])
#坐标轴说明
plt.xlabel("x axis")
plt.ylabel("y axis")
#图标题
plt.title("this is title")
#显示线条说明
plt.legend()
#显示网格
plt.grid(True)
#做标注
plt.annotate("con",xy=(0,0),xycoords='data',xytext=(+30,-30),textcoords='offset points',fontsize=16,arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
#做注释
plt.text(x,y,"con",fondict={'size':16,'color':'r'})
#画图
plt.show()