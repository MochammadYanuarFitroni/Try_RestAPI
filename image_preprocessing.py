import tensorflow as tf
import numpy as np
import PIL.Image as Image
from io import BytesIO

def load_image(image):
    img = Image.open(BytesIO(image))
    img = tf.image.resize(img, (64, 64))
    img = np.array(img)
    img = img / 255.0
    img = img.reshape(1, 64, 64, 3)
    return img