import tensorflow as tf
import numpy as np
import os
import cv2
import requests
from PIL import Image
from io import BytesIO

def weight_varible(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
# paras
W_conv1 = weight_varible([5, 5, 1, 32])
b_conv1 = bias_variable([32])

# conv layer-1
x = tf.placeholder(tf.float32, [None, 126])
x_image = tf.reshape(x, [-1, 9, 14, 1])

h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)

# conv layer-2
W_conv2 = weight_varible([5, 5, 32, 64])
b_conv2 = bias_variable([64])

h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

# full connection
shape = h_pool2.get_shape().as_list()
dim = 1
for d in shape[1:]:
    dim *= d
W_fc1 = weight_varible([dim, 1024])
b_fc1 = bias_variable([1024])

h_pool2_flat = tf.reshape(h_pool2, [-1, dim])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

# dropout
keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# output layer: softmax
W_fc2 = weight_varible([1024, 10])
b_fc2 = bias_variable([10])

y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)
y_ = tf.placeholder(tf.float32, [None, 10])

# model training
cross_entropy = -tf.reduce_sum(y_ * tf.log(y_conv+ 1e-10))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

correct_prediction = tf.equal(tf.arg_max(y_conv, 1), tf.arg_max(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

sess=tf.InteractiveSession()
tf.global_variables_initializer().run()

dirname=os.listdir("crop/")
dirname.remove("Thumbs.db")

def getRanPic(num):
    image=[]
    name=[]
    for i in range(num):
        tmpname=[0]*10
        filename=dirname[int(np.random.random()*len(dirname))]
        im=cv2.imread("crop/"+filename,0)/255.0
        im=im.reshape(-1)
        tmpname[int(filename[0])]=1
        image.append(im)
        name.append(tmpname)
    return image,name

def trainFirst():
    saver = tf.train.Saver()
    for _ in range(1000):
        batch_xs,batch_ys=getRanPic(50)
        train_step.run(feed_dict={x:batch_xs,y_:batch_ys,keep_prob: 1.0})
        if _%50==0:
            batch_xs,batch_ys=getRanPic(50)
            loss,acc=sess.run([cross_entropy,accuracy],feed_dict={x:batch_xs,y_:batch_ys,keep_prob: 1.0})
            print("loss:"+str(loss)+" acc_train:"+str(acc))
    saver.save(sess, 'model/next-crop-yzm-cnn.model', global_step=_)

def test(im):
    img=[]
    name=[]
    for i in range(5):
        crop=np.array(im.crop((9*i+5,4,9*i+14,18)))
        ret,im_hb=cv2.threshold(crop,127,255,cv2.THRESH_BINARY)
        img.append(im_hb.reshape(-1)/255)
        name.append([0]*10)
    saver = tf.train.Saver()
    with tf.Session() as sess:
        batch_xs,batch_ys=img,name
        path = 'model/testcropyzm-cnn.model-' + str(999)
        saver.restore(sess, path)
        predict = tf.arg_max(y_conv, 1)
        pre = sess.run(predict, feed_dict={x:batch_xs,y_:batch_ys,keep_prob: 1.0})
    return "".join(map(str,pre))
    
if __name__=='__main__':
    train=1
    if train==0:
        trainFirst()
    else:
        f=os.listdir("croptest/")
        f.remove("Thumbs.db")
        for i in f:
            test(i)