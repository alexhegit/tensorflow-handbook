import tensorflow as tf

version = tf.__version__
print(version)

if version < "2.0.0":
    # Tensorflow 1.x
    print(tf.test.is_gpu_available())
else:
    # Tensorflow 2.x
    print(tf.config.list_physical_devices('GPU'))
