import numpy as np
from keras.datasets import mnist


(x_train, y_train) , (x_test , y_test ) = mnist.load_data()
print(x_train.shape, y_train.shape)
