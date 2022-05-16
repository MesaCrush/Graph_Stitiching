import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import cifar10
from tensorflow.keras import layers
# from sklearn.utils import resample
import pandas as pd
import numpy as np


#model_presistent
def classifier(csv):
    x_test = np.reshape(csv,  (1, 28, 28))
    path = '/www/wwwroot/python/model'
  
    main_model = load_model(path)
    predict_x = main_model.predict(x_test)
    classes_x = np.argmax(predict_x,axis=1)

    return classes_x

