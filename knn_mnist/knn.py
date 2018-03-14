import numpy as np
import operator
from tensorflow.examples.tutorials.mnist import input_data

def classify(inX,dataSet,labels,k):
    dataSetSize=dataSet.shape[0] 
    #length
    diffMat=np.tile(inX,(dataSetSize,1))-dataSet 
    #tile(inx,(length,1))-dataSet=>array([inx,inx,inx,inx...])-dataSet
    sqDiffMat=diffMat**2 
    #每个数**2
    sqDistances=sqDiffMat.sum(axis=1) 
    #.sum()--所有数相加 .sum(axis=0)--列  .sum(axis=1)--行
    distances=sqDistances**0.5
    #每个数**0.5
    sortedDistIndicies=distances.argsort()
    #.argsort()返回排好序后的索引值
    classCount={}
    for i in range(k):
        voteIlabel=labels[sortedDistIndicies[i]]
        #获取由近到远的类别
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
        #.get(key,default) 对类别进行计数
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    #.iteritems()返回迭代器  operator.itemgetter(1)返回第一个域的值  reverse=True倒序
    return sortedClassCount[0][0]
    #输出频率高（靠近）的一个

def mnist_test():
    mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
    print("Download Done!")

    right=0
    all_test = 0
    for label in mnist.test.labels:
        if np.argmax(label)==classify(mnist.test.images[all_test],mnist.train.images,np.argmax(mnist.train.labels,axis=1),10):
            right+=1
        all_test+=1
        print(right,all_test,right/all_test)
    print(right,all_test,right/all_test)

#正确率
#k=100, 92%
#k=10, 95%

if __name__ == "__main__":
    mnist_test()