import tensorflow as tf
import architectures.common

def inference(x, num_output, wd, dropout_rate, is_training):
    
    with tf.variable_scope('conv1'):
      network = common.spatialConvolution(x, 11, 4, 64, wd= wd)
      network = common.batchNormalization(network, is_training= is_training)
      network = tf.nn.relu (network)
      #common.activation_summary(network)
    network = common.maxPool(network, 3, 2)
    with tf.variable_scope('conv2'):
      network = common.spatialConvolution(network, 5, 1, 192, wd= wd)
      network = common.batchNormalization(network, is_training= is_training)
      network = tf.nn.relu(network)
      #common.activation_summary(network)
    network = common.maxPool(network, 3, 2)
    with tf.variable_scope('conv3'):
      network = common.spatialConvolution(network, 3, 1, 384, wd= wd)
      network = common.batchNormalization(network, is_training= is_training)
      network = tf.nn.relu(network)
      #common.activation_summary(network)
    with tf.variable_scope('conv4'):
      network = common.spatialConvolution(network, 3, 1, 256, wd= wd)
      network = common.batchNormalization(network, is_training= is_training)
      network = tf.nn.relu(network)
    with tf.variable_scope('conv5'):
      network = common.spatialConvolution(network, 3, 1, 256, wd= wd)
      network = common.batchNormalization(network, is_training= is_training)
      network = tf.nn.relu(network)
    network = common.maxPool(network, 3, 2)
    network = common.flatten(network)
    with tf.variable_scope('fc1'): 
      network = tf.nn.dropout(network, dropout_rate)
      network = common.fullyConnected(network, 4096, wd= wd)
      network = common.batchNormalization(network, is_training= is_training)
      network = tf.nn.relu(network)
    with tf.variable_scope('fc2'):
      network = tf.nn.dropout(network, dropout_rate)
      network = common.fullyConnected(network, 4096, wd= wd)
      network = common.batchNormalization(network, is_training= is_training)
      network = tf.nn.relu(network)
    with tf.variable_scope('output'):
      network = common.fullyConnected(network, num_output, wd= wd)

    return network
