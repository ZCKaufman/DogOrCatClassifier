import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras.preprocessing import image
import numpy as np
from keras.models import load_model
import keras.backend as K
from PIL import Image as im
import os

# Set size of images to be used
shape2 = (180, 180)     # Only uses width and height
shape3 = (180, 180, 1)  # Includes depth
UPLOAD_FOLDER='./upload/'
model_loc="DogCatCNN3-19.tf"
#imageLoc = "images/Chloe1.jpg"
finalImg = ""
prediction = ""

def imageProcessing(imageLoc):
    preproc_image = tf.keras.preprocessing.image.load_img(
        imageLoc, color_mode="grayscale", target_size=shape2
    )
    imgArr = image.img_to_array(preproc_image)
    imgEx = np.expand_dims(imgArr, axis=0)
    return imgEx
    finalImg = imgEx
    #predict(imgEx)


def predict(filename):
    path = os.path.join(UPLOAD_FOLDER, filename)
    img = imageProcessing(path)
    model = load_model(model_loc)
    prediction = model.predict(img)
    d = prediction.flatten()
    j = d.max()
    if(j > 0.5):
        return "Dog!"
        prediction = "Dog!"
    elif (j == 0.5):
        return "Too close to call!"
        prediction = "Too close to call!"
    else:
        return "Cat!"
        prediction = "Cat!"
