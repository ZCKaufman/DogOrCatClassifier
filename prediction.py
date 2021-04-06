from keras.preprocessing import image
import numpy as np
from keras.models import load_model
import keras.backend as K

def imageProcessing(loc):
  #print(loc)
  preproc_image = tf.keras.preprocessing.image.load_img(
    loc, color_mode="grayscale", target_size=shape2
  )
  #print(preproc_image)
  imgArr = image.img_to_array(preproc_image)
  imgEx = np.expand_dims(imgArr, axis=0)
  #img = imgArr/255
  return imgEx

def predict(imgLoc, model_loc):
  img = imageProcessing(imgLoc)
  model = load_model(model_loc)
  #print(img)
  prediction = model.predict(img)
  #print(prediction)
  d = prediction.flatten()
  j = d.max()

  #print(j)
  if(j > 0.5):
    print("Dog!")
  elif (j == 0.5):
    print("Too close to call!")
  else:
    print("Cat!")