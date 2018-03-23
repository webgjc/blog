import tensorflow as tf
import os
import numpy as np
import cv2

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
char_Len=5*len(number)
dirname=os.listdir('dealyzm/')
dirname.remove('Thumbs.db')

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
x = tf.placeholder(tf.float32, [None, 1320])
x_image = tf.reshape(x, [-1, 22, 60, 1])

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
W_fc2 = weight_varible([1024, char_Len])
b_fc2 = bias_variable([char_Len])

y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)
y_ = tf.placeholder(tf.float32, [None, char_Len])

# model training
cross_entropy = -tf.reduce_sum(y_ * tf.log(y_conv+ 1e-10))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
sess=tf.InteractiveSession()
tf.global_variables_initializer().run()

def getRanPic(num):
    image=[]
    name=[]
    for i in range(num):
        tmpname=[0]*char_Len
        filename=dirname[int(np.random.random()*len(dirname))]
        im=cv2.imread("dealyzm/"+filename,0)/255.0
        im=im.reshape(-1)
        for i in range(5):
            tmpname[number.index(filename[i])+len(number)*i]=1
        image.append(im)
        name.append(tmpname)
    return image,name
def trainFirst():
    saver = tf.train.Saver()
    for _ in range(400):
        batch_xs,batch_ys=getRanPic(20)
        tmp,loss=sess.run([train_step,cross_entropy],feed_dict={x:batch_xs,y_:batch_ys,keep_prob: 1.0})
        if _%20==0:
            batch_xs,batch_ys=getRanPic(20)
            correct_prediction=tf.equal(tf.argmax(tf.reshape(y_conv, [-1, 5, 10]),2),tf.argmax(tf.reshape(y_, [-1, 5, 10]),2))
            accuracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
            acc_test=sess.run(accuracy,feed_dict={x:batch_xs,y_:batch_ys,keep_prob: 1.0})
            print("loss:"+str(loss)+" acc_train:"+str(acc_test))
    saver.save(sess, 'model/testyzm-cnn.model', global_step=_)
def detect():
    saver = tf.train.Saver()
    with tf.Session() as sess:
        batch_xs,batch_ys=getRanPic(100)
        path = 'model/testyzm-cnn.model-' + str(399)
        saver.restore(sess, path)
        correct_prediction=tf.equal(tf.argmax(tf.reshape(y_conv, [-1, 5, 10]),2),tf.argmax(tf.reshape(y_, [-1, 5, 10]),2))
        accuracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
        predict = tf.argmax(tf.reshape(y_conv, [-1, 5, 10]), 2)
        pre,acc = sess.run([predict,accuracy], feed_dict={x:batch_xs,y_:batch_ys,keep_prob: 1.0})
        print(acc)
train=1
if train==0:
    trainFirst()
else:
    detect()