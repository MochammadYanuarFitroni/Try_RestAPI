import tensorflow as tf
import numpy as np


labels = {0:'ka', 1:'ca', 2:'ta', 3:'pa', 4:'ya', 5:'wa', 6:'ga', 7:'ja', 8:'da', 9:'ba', 10:'ra', 11:'sa', 12:'nga', 13:'nya', 14:'na', 15:'ma', 16:'la', 17:'ha'}

def make_predict(image_pre):
    model = tf.keras.models.load_model('model_cnn.h5')
    
    predicted = model.predict(image_pre)
    result = np.argmax(predicted)

    return labels[result]