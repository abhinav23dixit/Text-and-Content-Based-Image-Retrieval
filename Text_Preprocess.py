# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 23:49:33 2018

@author: ishaa
"""

import string


#Token File eg -- 1000268201_693b08cb0e.jpg#0	A child in a pink dress is climbing up a set of stairs in an entry way .
#1000268201_693b08cb0e.jpg#1	A girl going into a wooden building .

def load_text(filename): 
    file = open(filename,'r')
    text = file.read()
    file.close()
    return text

def load_description(doc):
    mapping = dict()
    #one entry in each line
    for line in doc.split('\n'):
        tokens = line.split()
        #if no of tokens less than 2 --> incorrect desc
        if len(line)<2:
            continue
        #first -- id rest -- desc
        image_id, image_desc = tokens[0], tokens[1:]
        image_id = image_id.split('.')[0]
        
        #convert description token back to string
        image_desc = ' '.join(image_desc)
        #create a list (containing all desc of a given image)
        if image_id not in mapping:
            mapping[image_id] = list()
        mapping[image_id].append(image_desc)
    return mapping

#Cleaning description -- convert to lowercase, remove punctuation, remove words less than some len, remove words with number
def clean_description(description):
    #remove punctuation -- make translation table
    #param1 - to be replaced by param2 ---- param3 removed
    table = str.maketrans('','',string.punctuation)
    
    for key, desc_list in descriptions.items():
        for i in range(len(desc_list)):
            desc = desc_list[i]
            #tokenize
            desc = desc.split()
            #to lower
            desc = [word.lower() for word in desc]
            #remove punctuation
            desc = [word.translate(table) for word in desc]
            #remove words less in len
            desc = [word for word in desc if len(word)>1]
            #remove numbers
            desc = [word for word in desc if word.isalpha()]
            #re-convert to desc
            desc_list[i] =  ' '.join(desc)

def save_description(description, filename):
    lines = list()
    for key, desc_list in descriptions.items():
        for desc in desc_list:
            lines.append(key + ' ' + desc)
    data = ('\n').join(lines)
    file = open(filename,'w')
    file.write(data)
    file.close()
    
# convert the loaded descriptions into a vocabulary of words
def to_vocabulary(descriptions):
	# build a list of all description strings
	all_desc = set()
	for key in descriptions.keys():
		[all_desc.update(d.split()) for d in descriptions[key]]
	return all_desc

tokenFile = 'D:\\Study\\Machine Learning\\DataSets\\Image Caption Generator\\Flickr_8k\\Flickr8k.token.txt'
# load descriptions
doc = load_text(tokenFile)
# parse descriptions
descriptions = load_description(doc)
print('Loaded: %d ' % len(descriptions))
# clean descriptions
clean_description(descriptions)
# summarize vocabulary
vocabulary = to_vocabulary(descriptions)
print('Vocabulary Size: %d' % len(vocabulary))
# save to file
descrOut = 'D:\\Study\\Machine Learning\\DataSets\\Image Caption Generator\\descriptions.txt'

save_description(descriptions, descrOut)
