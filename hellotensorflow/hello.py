"""
    author: Josh Peak
    description: learning tensorflow API
"""
import os
import tensorflow as tf
from tensorflow import keras


def default():
    print("KERAS %s" % keras.__version__)
    hello = tf.constant('Hello, TensorFlow!')
    #sess = tf.Session()
    sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))

    print(sess.run(hello))


def mnist_classification():
    mnist = tf.keras.datasets.mnist

    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0

    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(512, activation=tf.nn.relu),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation=tf.nn.softmax)
    ])
    model.compile(optimizer=tf.train.AdamOptimizer(),
                  loss=tf.keras.losses.sparse_categorical_crossentropy,
                  metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=5)
    model.save_weights('mymodel.h5', save_format='h5')
    print(model.evaluate(x_test, y_test))


if __name__ == "__main__":
    default()
    mnist_classification()
