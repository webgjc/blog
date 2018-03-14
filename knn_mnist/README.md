# KNN分类算法（mnist为例）

## 文章源地址：https://ganjiacheng.cn/blog/?p=71

## 所需python库：numpy,tensorflow

## 运行：
>python knn.py

## 结果分析：
### 运行输出为正确个数，总个数，正确率。
### 在k取10时有95%的正确率。
### 单个分类来看速度还可以，不过多了的话由于每个测试集都要和全部训练集计算一遍欧氏距离，还是很费时间的。