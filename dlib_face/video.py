#python3.5
#windows
#author:gjc
import cv2
import dlib
import numpy as np
from sklearn import svm
import os
from PIL import Image
#获取默认摄像头
cap = cv2.VideoCapture(0)
#dlib加载68个点模型
detector=dlib.get_frontal_face_detector()
predictor_path = "shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(predictor_path)
data=[]
label=[]
#读取认脸已分类好的数据
def read(dir,l):
    f=os.listdir(dir)
    L=len(f)-1
    for i in range(L):
        imgdir=dir+str(f[i])
        im=Image.open(imgdir)
        #draw = ImageDraw.Draw(im)
        dets=detector(np.array(im),0)
        if len(dets)==0:
            continue
        facepoint = np.array([[p.x, p.y] for p in predictor(np.array(im), dets[0]).parts()])
        arr=np.zeros((20,2))
        for j in range(48,68):
            #draw.arc((facepoint[j][0]-5, facepoint[j][1]-5, facepoint[j][0]+5, facepoint[j][1]+5), 0, 360, fill=(55,255,155))  
            arr[j-48][0]=facepoint[j][0]-facepoint[27][0]
            arr[j-48][1]=facepoint[j][1]-facepoint[27][1]
        arr=(arr-arr.min())/(arr.max()-arr.min())
        data.append(arr.flatten())
        label.append(l)
read("data/smile/",1)
read("data/nosmile/",0)
#用svm进行分类
clf = svm.SVC()
clf.fit(np.array(data), label)
while(1):
    #读取摄像头图片
    ret, frame = cap.read()
    #定位
    dets=detector(frame,0)
    #画人脸的框
    for i,d in enumerate(dets):
        cv2.rectangle(frame, (int(d.left()), int(d.top())), (int(d.right()), int(d.bottom())), (0,255,0),2,0)
    for i,d in enumerate(dets):
        facepoint = np.array([[p.x, p.y] for p in predictor(frame, dets[i]).parts()])
        #画68个点
        for j in range(68):
            #if facepoint[j][1]<640 and facepoint[j][0]<480:
            #frame[facepoint[j][1]][facepoint[j][0]] = [0,0,0]
            #cv2.line(frame,(facepoint[j][0],facepoint[j][1]),(facepoint[j+1][0],facepoint[j+1][1]),(155,155,155),2)
            cv2.circle(frame,(facepoint[j][0],facepoint[j][1]),2,(55,255,155),2)
        arr=np.zeros((20,2))
        #读取特征点，归一化
        for j in range(48,68):
            arr[j-48][0]=facepoint[j][0]-facepoint[27][0]
            arr[j-48][1]=facepoint[j][1]-facepoint[27][1]
        arr=(arr-arr.min())/(arr.max()-arr.min())
        #svm分类判断是否笑脸
        if clf.decision_function(arr.flatten().reshape(1,-1))>0:
            cv2.putText(frame, 'smile', (int(d.left()),int(d.top())), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255 ,0), thickness = 2, lineType = 8)  
        else:
            cv2.putText(frame, 'No smile', (int(d.left()),int(d.top())), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255 ,0), thickness = 2, lineType = 8)  
    #展示处理后的图片
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()