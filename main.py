import numpy as np
from PIL import Image
import tensorflow as tf
from itertools import product


def weight_variable(shape, name):
    initial = tf.truncated_normal(shape, stddev=0.5, name=name)
    return tf.Variable(initial)


def bias_variable(shape, name):
    initial = tf.truncated_normal(shape, stddev=0.01, name=name)+0.1
    return tf.Variable(initial)


def selector(img, num):

    x1=[]#[0.0]*num
    x2=[]#[0.0]*num
    v=[]#[0.0]*num

    for x in range(num):
        x1 += [float(np.random.randint(low=0, high=img.size[0]-1))]
        x2 += [float(np.random.randint(low=0, high=img.size[1]-1))]
        v += [img.load()[x1[x], x2[x]]]
        #x1[x] = x1[x]**2
        #x2[x] = x2[x]**2
    #v = img.load()[x1, x2]

    return [[np.array(x1)*2/img.size[0]-1, np.array(x2)*2/img.size[1]-1], v]


def selector2(img, num):

    y1 = [[np.random.randint(0, img.size[0] - 1), np.random.randint(0, img.size[1] - 1)] for _ in range(num)]

    return [[y[0], y[1], img.load()[y[0], y[1]]] for y in y1]


def INT_TO_XY(img, i):

    return divmod(i,img.size[0])


def XY_TO_INT(img, x, y):

    return x*img.size[0] + y


# Image input:
# X = image
X = Image.open("baboon.jpeg").convert("F")
#X.show()
Y = Image.new("F", X.size)

#X.size[0]
#print(np.array([X.size]*10))
#print([list(divmod(0,512))])#np.ndarray(INT_TO_XY(X, 10)))

x = tf.placeholder(tf.float32, shape=[None, 2])
y_ = tf.placeholder(tf.float32, shape=[None, 1])
kp = tf.placeholder(tf.float32)

W_layer1 = weight_variable([2, 32], 'W1')
b_layer1 = bias_variable([32], 'b1')

h_layer1 = tf.nn.relu(tf.matmul(x, W_layer1) + b_layer1, name='h1')
h_lay1do = tf.nn.dropout(h_layer1, kp)
x1 = h_lay1do#tf.concat([h_lay1do, x], 1)

W_layer2 = weight_variable([32, 32], 'W2')
b_layer2 = bias_variable([32], 'b2')

h_layer2 = tf.nn.relu(tf.matmul(x1, W_layer2) + b_layer2, name='h2')
h_lay2do = tf.nn.dropout(h_layer2, kp)
x2 = h_lay2do#tf.concat([h_lay2do, x], 1)

W_layer3 = weight_variable([32, 32], 'W3')
b_layer3 = bias_variable([32], 'b3')

h_layer3 = tf.nn.relu(tf.matmul(x2, W_layer3) + b_layer3, name='h3')
h_lay3do = tf.nn.dropout(h_layer3, kp)
x3 = h_lay3do#tf.concat([h_lay3do, x], 1)

W_layer4 = weight_variable([32, 32], 'W4')
b_layer4 = bias_variable([32], 'b4')

h_layer4 = tf.nn.relu(tf.matmul(x3, W_layer4) + b_layer4, name='h4')
h_lay4do = tf.nn.dropout(h_layer4, kp)
x4 = h_lay4do#tf.concat([h_lay4do, x], 1)

W_layer5 = weight_variable([32, 16], 'W5')
b_layer5 = bias_variable([16], 'b5')

h_layer5 = tf.nn.sigmoid(tf.matmul(x4, W_layer5) + b_layer5, name='h5')
h_lay5do = tf.nn.dropout(h_layer5, kp)
x5 = h_lay5do#tf.concat([h_lay5do, x], 1)

W_layer6 = weight_variable([16, 32], 'W6')
b_layer6 = bias_variable([32], 'b6')

h_layer6 = tf.nn.relu(tf.matmul(x5, W_layer6) + b_layer6, name='h6')
h_lay6do = tf.nn.dropout(h_layer6, kp)
x6 = h_lay6do#tf.concat([h_lay6do, x], 1)

W_layer7 = weight_variable([32, 1], 'W7')
b_layer7 = tf.Variable(tf.constant(0.0, shape=[1], name='b7'))

y = tf.identity(tf.nn.sigmoid(tf.matmul(x4, W_layer7) + b_layer7)*255, name='y')

error_fun = tf.reduce_mean((y-y_)**2)

train_step = tf.train.AdamOptimizer(3e-3).minimize(error_fun)

saver = tf.train.Saver(max_to_keep=101)

iternum = 1e7

bs = int(np.floor(np.sqrt(X.size[0]*X.size[1])))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    #tf.train.Saver().restore(sess, './my-model-3200')
    print(X.size)
    for i in range(int(np.floor(iternum/bs))):
        #print(np.array(batch1))
        batch = selector(X, bs)
        #print('asd')
        #batch2 = selector2(X, bs)
        #print(np.array(batch2[0]))
        if i % int(np.floor(iternum/(100*bs))) == 0:
            #print("asd")
            #batch = selector(X, bs)
            T = product(range(X.size[0]), range(X.size[1]))
            asd = np.array(list(T), dtype=np.float32)
            asd[:, 0] = asd[:, 0]*2 / X.size[0] -1
            asd[:, 1] = asd[:, 1]*2 / X.size[1] -1
            #print(asd.shape)
            #print(asd)
            #asd = np.array(asd[0:260000, :])#np.concatenate([np.array(asd[0:260000:13, :]), np.array([X.size]*np.array(asd[0:260000:13, :]).shape[0], dtype=np.float32)], 1)
            asd2 = np.array(list(X.getdata()))
            #asd2 = asd2[0:260000]
            #print(asd2)
            #print(asd.shape)
            YY = y.eval(feed_dict={x: asd, kp: 1.0})
            #Y.putdata(YY, scale=13.0, offset=0.0)
            #tmp = np.subtract(asd2, YY.transpose())
            res = np.array(YY.reshape([X.size[0], X.size[1]]).transpose())
            e = np.array(np.subtract(res, asd2.reshape([X.size[0], X.size[1]])))
            c1 = -1*(e/abs(e+1e-8))*np.exp2(np.maximum(np.minimum(np.round(np.log2(abs(e+1e-8)/8)), 3), 0))*8
            c2 = -1*(e/abs(e+1e-8))*(np.maximum(np.minimum(np.round(np.sqrt(abs(e+1e-8)/14.2222)), 3), 0)**2)*14.2222
            #c2 = -1*(e/abs(e+1e-8))*(np.minimum(np.round(np.sqrt(abs(e+1e-8)/2.5)), 7)**2)*2.5
            c1 += res
            c2 += res
            code1 = Image.fromarray(c1).convert('L')
            code2 = Image.fromarray(c2).convert('L')
            err = Image.fromarray(abs(e)).convert('L')
            im = Image.fromarray(res).convert('L')
            code1.save('code1.png')
            code2.save('code2.png')
            err.save('err1.png')
            im.save('out1.png')
            #train_accuracy = 0
            #for t in range(X.getdata().size[0]*X.getdata().size[1]):
            #  if t % 1000 == 0:
            #      print(t)#[list(INT_TO_XY(X,t))]
            #train_accuracy += abs(list(X.getdata())[t]-y.eval(feed_dict={x: np.array(list(T), np.float32)}))
            if i % int(np.floor(iternum/(10*bs))) == 0:
                saver.save(sess, './my-model', global_step=i)
            print('step %d, training accuracy %g' % (i, float(np.mean(abs(e)**2))))
            print('step %d, compression1 accuracy %g' % (i, float(np.mean(abs(np.array(X)-c1)**2))))
            print('step %d, compression2 accuracy %g' % (i, float(np.mean(abs(np.array(X)-c2)**2))))
        #qwe = np.array([[batch[0]]]).transpose().reshape((20000, 2))
        #qwe0 = np.array([[batch[0]]]).reshape((20000, 2))
        #qwe2 = np.array([[batch[1]]]).reshape(20000, 1)
        _x = np.array([[batch[0]]]).transpose().reshape((bs, 2))#np.concatenate([np.array([[batch[0]]]).transpose().reshape((bs, 2)), np.array([X.size]*bs, dtype=np.float32)], 1)
        _y = np.array([[batch[1]]]).reshape(bs, 1)
        #_x = np.array(batch2).transpose()
        #_y = _x[2].reshape(bs, 1)
        #_x = np.array([_x[0], _x[1]]).transpose()
        train_step.run(feed_dict={x: _x, y_: _y, kp: 0.99})

    saver.save(sess, './my-model', global_step=-1)
    #print('test accuracy %g' % accuracy.eval(feed_dict={
    #    x: mnist.test.images, y_: mnist.test.labels}))