import tensorflow.examples.tutorials.mnist.input_data as input_data
import tensorflow as tf
import numpy as np
import os
#防止输出警告
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
#读取/下载mnist
mnist=input_data.read_data_sets("MNIST_data/", one_hot=True)

#x--传入数值 w，b--可调整参数
x=tf.placeholder(tf.float32,[None,784])
w=tf.Variable(tf.zeros([784,10]))
b=tf.Variable(tf.zeros([10]))

#y--softmax(x*w+b)算得每个0-9取值的概率，y_--输入正确值
y=tf.nn.softmax(tf.matmul(x,w)+b)
y_=tf.placeholder(tf.float32,[None,10])

#求对数差做loss
cross_entropy=-tf.reduce_sum(y_*tf.log(y))
train_step=tf.train.GradientDescentOptimizer(0.001).minimize(cross_entropy)

#初始化
sess=tf.InteractiveSession()
tf.global_variables_initializer().run()

#开始训练
for _ in range(2000):
    batch_xs,batch_ys=mnist.train.next_batch(100)
    sess.run(train_step,feed_dict={x:batch_xs,y_:batch_ys})
    if _%50==0:
        a,loss=sess.run([train_step,cross_entropy],feed_dict={x:batch_xs,y_:batch_ys})
        print(loss)

#测试集测试
correct_prediction=tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
accuracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
print("test accuracy %g"%sess.run(accuracy,feed_dict={x:mnist.test.images,y_:mnist.test.labels}))