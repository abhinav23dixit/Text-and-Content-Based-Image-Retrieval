# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 20:12:55 2018

@author: ishaa
"""


from os import listdir
from pickle import dump
from keras.applications.resnet50 import ResNet50
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.resnet50 import preprocess_input
from keras.models import Model


#extract features from all photos in library
def extract_features(directory):
    #load model
    model = ResNet50()
    
    #remove classification layer
    model.layers.pop()
    model = Model(inputs = model.inputs, outputs = model.layers[-1].output)
    
    features = dict()
    
    #os.listdir --> returns a list of files in the directory
    for name in listdir(directory):
        filename = directory + '/' + name
        #load image
        image = load_img(filename, target_size = (224,224))
        #reshaping image into 4D for fitting in model
        image = img_to_array(image)
        image = image.reshape(1,image.shape[0],image.shape[1],image.shape[2])
        
        #The preprocess_input function is meant to adequate your image to the format the model requires
        image = preprocess_input(image)
        
        #extract features
        feature = model.predict(image, verbose = 0)
        #remove .jpg
        image_id = name.split('.')[0]
        features[image_id] = feature
        print('.')
    return features

directory = 'D:\\Study\\Machine Learning\\DataSets\\Image Caption Generator\\Flicker8k_Dataset'
features = extract_features(directory)
print('Extracted features: %d' %len(features))
dump(features, open('D:\\Study\\Machine Learning\\DataSets\\Image Caption Generator\\features_resnet.pkl','wb'))