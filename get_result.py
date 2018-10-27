import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.models import model_from_json
import os
import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

filepath="C:\\Users\\Deii\\Downloads\\manus"

os.chdir(filepath)
json_file = open('modell.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

filepath2="C:\\Users\\Deii\\Downloads\\manus\\model3.h5"
loaded_model.load_weights(filepath2)
print("Loaded model from disk")

loaded_model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

def getx_text():
     x_test=np.array([input()])

getx_text()
x_test=x_test.reshape(1,11,11,1)

y_pred=model.predict_classes(x_test)

if(y_pred==0):
	print("Not Depressed  ")
if(y_pred==1):
	print("Depressed")	
