# dlib人脸识别+svm分类

## 原文链接: https://ganjiacheng.cn/blog/?p=287

## 所需库 cv2，dlib，numpy，sklearn，PIL

## 使用方法：

> 将有笑容的图片放到 data/smile/

> 不笑的图片放到 data/nosmile/

> 从百度云https://pan.baidu.com/s/1Y7Q3eme4Qzm793n23vV_FA
下载预训练人脸68个关键点数据，放于主目录下

> python video.py

> 效果：电脑会调用摄像头并时时检测人脸并识别是否是笑脸