import numpy as np
from PIL import Image
import tensorflow as tf
from itertools import product


# For network definition
def weight_variable(shape, name):
    initial = tf.truncated_normal(shape, stddev=0.1, name=name)
    return tf.Variable(initial)


# For network definition
def bias_variable(shape, name):
    initial = tf.truncated_normal(shape, stddev=0.01, name=name)+0.1
    return tf.Variable(initial)


# For input generation
def selector(img, num):

    x1=[]
    x2=[]
    v=[]

    for x in range(num):
        x1 += [float(np.random.randint(low=0, high=img.size[0]-1))]
        x2 += [float(np.random.randint(low=0, high=img.size[1]-1))]
        v += [img.load()[x1[x], x2[x]]]

    return [[np.array(x1)*2/img.size[0]-1, np.array(x2)*2/img.size[1]-1], v]


# Input image
imgName = "circ2.png"
X = Image.open(imgName).convert("F")

# Neuron number in each layer
neuronNum = 64

# Input and output definition
x = tf.placeholder(tf.float32, shape=[None, 2])
y = tf.placeholder(tf.float32, shape=[None, 1])
kp = tf.placeholder(tf.float32)

# First layer definition
W_layer1 = weight_variable([2, neuronNum], 'W1')
b_layer1 = bias_variable([neuronNum], 'b1')

h_layer1 = tf.nn.relu(tf.matmul(x, W_layer1) + b_layer1, name='h1')
h_lay1do = tf.nn.dropout(h_layer1, kp)
x1 = h_lay1do

# Second layer definition
W_layer2 = weight_variable([neuronNum, neuronNum], 'W2')
b_layer2 = bias_variable([neuronNum], 'b2')

h_layer2 = tf.nn.relu(tf.matmul(x1, W_layer2) + b_layer2, name='h2')
h_lay2do = tf.nn.dropout(h_layer2, kp)
x2 = h_lay2do

# Third layer definition
W_layer3 = weight_variable([neuronNum, neuronNum], 'W3')
b_layer3 = bias_variable([neuronNum], 'b3')

h_layer3 = tf.nn.relu(tf.matmul(x2, W_layer3) + b_layer3, name='h3')
h_lay3do = tf.nn.dropout(h_layer3, kp)
x3 = h_lay3do

# Fourth layer definition
W_layer4 = weight_variable([neuronNum, neuronNum], 'W4')
b_layer4 = bias_variable([neuronNum], 'b4')

h_layer4 = tf.nn.relu(tf.matmul(x3, W_layer4) + b_layer4, name='h4')
h_lay4do = tf.nn.dropout(h_layer4, kp)
x4 = h_lay4do

# Fifth layer definition
W_layer5 = weight_variable([neuronNum, neuronNum], 'W5')
b_layer5 = bias_variable([neuronNum], 'b5')

h_layer5 = tf.nn.relu(tf.matmul(x4, W_layer5) + b_layer5, name='h5')
h_lay5do = tf.nn.dropout(h_layer5, kp)
x5 = h_lay5do

# Sixth layer definition
W_layer6 = weight_variable([neuronNum, neuronNum], 'W6')
b_layer6 = bias_variable([neuronNum], 'b6')

h_layer6 = tf.nn.relu(tf.matmul(x5, W_layer6) + b_layer6, name='h6')
h_lay6do = tf.nn.dropout(h_layer6, kp)
x6 = h_lay6do

# Last layer definition
W_layer7 = weight_variable([neuronNum, 1], 'W7')
b_layer7 = tf.Variable(tf.constant(0.0, shape=[1], name='b7'))
Y = tf.identity(tf.nn.sigmoid(tf.matmul(x6, W_layer7) + b_layer7)*255, name='y')

# Cost function
error_fun = tf.reduce_mean((Y-y)**2)
# Training algortihm
train_step = tf.train.AdamOptimizer(1e-3).minimize(error_fun)
# Saver start
saver = tf.train.Saver(max_to_keep=101)

# Abstract iternum
iternum = 2e7
# Batch size
bs = int(np.floor(np.sqrt(X.size[0]*X.size[1])))
# Training start
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    # Print for debug
    print("Image size: ", X.size)
    print("Batch size: ", bs)
    for i in range(int(np.floor(iternum/bs))):
        # Batch generator
        batch = selector(X, bs)
        # Testing part
        if i % int(np.floor(iternum/(100*bs))) == 0:
            # Generating an index vector with the possible indices
            T = product(range(X.size[0]), range(X.size[1]))
            test_input = np.array(list(T), dtype=np.float32)
            # Normalization of the input to [-1:1]
            test_input[:, 0] = test_input[:, 0] * 2 / X.size[0] - 1
            test_input[:, 1] = test_input[:, 1] * 2 / X.size[1] - 1
            # Evaluating the neural network in its current state
            test_real_output = Y.eval(feed_dict={x: test_input, kp: 1.0})
            # Loading the original image into a numpy array
            test_expected_output = np.array(list(X.getdata()))
            # Reshaping the image data into correct images
            result = np.array(test_real_output.reshape([X.size[0], X.size[1]]).transpose())
            error = abs(np.subtract(result, test_expected_output.reshape([X.size[1], X.size[0]])))
            # Saving the error and current output
            Image.fromarray(error).convert('L').save('err1.png')
            Image.fromarray(result).convert('L').save('out1.png')
            # Saving at every 10%
            if i % int(np.floor(iternum/(10*bs))) == 0:
                saver.save(sess, './my-model', global_step=i)
            print('step %d, %d%% done, training accuracy: %g' % (i, int(i*bs*101/iternum), float(np.mean(error**2))))
        # Taking the data from the batch
        _x = np.array([[batch[0]]]).transpose().reshape((bs, 2))
        _y = np.array([[batch[1]]]).reshape(bs, 1)
        # The actual training command
        train_step.run(feed_dict={x: _x, y: _y, kp: 0.9})
    # Saving the final network
    saver.save(sess, './'+imgName, global_step=None)