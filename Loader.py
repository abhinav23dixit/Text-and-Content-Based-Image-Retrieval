# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 08:58:40 2018

@author: ishaa
"""

import pickle

def load_doc(filename):
    file = open(filename,'r')
    text = file.read()
    file.close()    
    return text

#Image Identifier --- TrainImage.txt
    #2513260012_03d33305cf.jpg
def load_set(filename):
    doc = load_doc(filename)
    dataset = list()
    
    for line in doc.split('\n'):
        if len(line)<1:
            continue
        identifier = line.split('.')[0]
        dataset.append(identifier)
    return set(dataset)

#load cleaned description
#1000268201_693b08cb0e child in pink dress is climbing up set of stairs in an entry way
#assign start and end token to the description
def load_clean_descriptions(filename, dataset):
    doc = load_doc(filename)
    descriptions = dict()
    
    for line in doc.split('\n'):
        tokens = line.split()
        image_id, image_desc = tokens[0],tokens[1:]
        #if image_id not in dataset ignore
        if image_id in dataset:
            if image_id not in descriptions:
                descriptions[image_id] = list()
            desc = 'startseq ' + ' '.join(image_desc) + ' endseq'
            descriptions[image_id].append(desc)
    return descriptions

    
# load photo features from features.pkl
def load_photo_features(filename, dataset):
	# load all features
	all_features = pickle.load(open(filename, 'rb'))
	# filter features
	features = {k: all_features[k] for k in dataset}
	return features








