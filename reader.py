import numpy as np
import tensorflow as tf


def readTensorFlowFile(fname):

    saver = tf.train.import_meta_graph(fname+'.meta')
    graph = tf.get_default_graph()

    #print(graph.get_all_collection_keys())
    print(graph.get_collection_ref('variables'))

    with tf.Session() as sess:
        tf.train.Saver().restore(sess, fname)
        theta = []
        tmp = []

        for x in graph.get_collection_ref('trainable_variables'):
            if not tmp:
                tmp += [x]
                continue
            if tmp[0].shape[1] == x.shape[0]:
                theta += [(np.array(tmp[0].eval(sess)), np.array(x.eval(sess)))]
                tmp = []

    return theta


print(readTensorFlowFile('my-model-1200'))