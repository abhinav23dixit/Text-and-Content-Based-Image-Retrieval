# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 20:41:32 2018

@author: ishaa
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 09:00:02 2018

@author: ishaa
"""

import Loader
import Model_handling
from pickle import load
from pickle import dump
from PIL import Image

from keras.preprocessing.text import Tokenizer
from keras.models import load_model
from nltk.translate.bleu_score import corpus_bleu

#convert descriptions into a list of descriptions
def to_lines(descriptions):
    all_desc = list()
    for key in descriptions.keys():
        [all_desc.append(des) for des in descriptions[key]]
    return all_desc

#Encode using tokenizer
#eg - tokenize  --> Boy on horse --> startseq Boy on horse endSeq
# X1      X2                        y (word)
# photo   startseq                  Boy
# photo   startseq, Boy             on
# photo   startseq, Boy,on          horse
# photo   startseq,Boy,on,horse     endseq
def create_tokenizer(descriptions):
    lines = to_lines(descriptions)
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(lines)
    return tokenizer    


# calculate the length of the description with the most words
def max_length(descriptions):
	lines = to_lines(descriptions)
	return max(len(d.split()) for d in lines)


#mapping of integer to word
def word_for_id(integer, tokenizer):
    for word, index in tokenizer.word_index.items():
        if index == integer:
            return word
    return None

def evaluate_model(model, descriptions, photos, tokenizer, max_length):
    actual, predicted = list(), list()
    
    for key, desc_list in descriptions.items():
            #generate description
            yhat = Model_handling.generate_desc(model, tokenizer, photos[key], max_length)
            # store actual and predicted captions
            references = [d.split() for d in desc_list]
            actual.append(references)
            predicted.append(yhat.split())
    # calculate BLEU score
    print('BLEU-1: %f' % corpus_bleu(actual, predicted, weights=(1.0, 0, 0, 0)))
    print('BLEU-2: %f' % corpus_bleu(actual, predicted, weights=(0.5, 0.5, 0, 0)))
    print('BLEU-3: %f' % corpus_bleu(actual, predicted, weights=(0.3, 0.3, 0.3, 0)))
    print('BLEU-4: %f' % corpus_bleu(actual, predicted, weights=(0.25, 0.25, 0.25, 0.25)))

    
#load trainset
trainFile = 'D:\\Study\\Machine Learning\\DataSets\\Image Caption Generator\\Flickr_8k\\Flickr_8k.trainImages.txt'
train = Loader.load_set(trainFile)
print('Dataset: %d' % len(train))
# descriptions
train_descriptions = Loader.load_clean_descriptions('D:\\Study\\Machine Learning\\DataSets\\Image Caption Generator\\descriptions.txt', train)
print('Descriptions: train=%d' % len(train_descriptions))
# photo features
train_features = Loader.load_photo_features('D:\\Study\\Machine Learning\\DataSets\\Image Caption Generator\\features_resnet.pkl', train)
print('Photos: train=%d' % len(train_features))
tokenizer = create_tokenizer(train_descriptions)
vocab_size = len(tokenizer.word_index) + 1
print('Vocabulary Size: %d' % vocab_size)

# determine the maximum sequence length
max_length = max_length(train_descriptions)
print('Description Length: %d' % max_length)
# prepare sequences

                    
dataset_root_dir = 'D:\\Study\\Machine Learning\\DataSets\\Image Caption Generator\\'
code_root_dir = 'D:\\Study\\Machine Learning\\Codes\\Caption Generator\\Reverse-Image-Search\\'


# define the model
model = Model_handling.define_model(vocab_size, max_length)
# train the model, run epochs manually and save after each epoch
epochs = 20
steps = len(train_descriptions)
for i in range(epochs):
	# create the data generator
	generator = Model_handling.data_generator(train_descriptions, train_features, tokenizer, max_length)
	# fit for one epoch
	model.fit_generator(generator, epochs=1, steps_per_epoch=steps, verbose=1)
	# save model
	model.save(code_root_dir +  'ResNet50\\model_' + str(i) + '.h5')



# load test set
testImgList = dataset_root_dir + 'Flickr_8k\\Flickr_8k.testImages.txt'
testImg = Loader.load_set(testImgList)
print('Dataset: %d' % len(testImg))
# descriptions
test_descriptions = Loader.load_clean_descriptions(dataset_root_dir + 'descriptions.txt', testImg)
print('Descriptions: test=%d' % len(test_descriptions))
# photo features
test_features = Loader.load_photo_features('D:\\Study\\Machine Learning\\DataSets\\Image Caption Generator\\features_resnet.pkl', testImg)
print('Photos: test=%d' % len(test_features))

weights = code_root_dir + 'ResNet50\\model_19.h5'
model = load_model(weights)
evaluate_model(model, test_descriptions, test_features, tokenizer, max_length)

# prepare tokenizer
tokenizer = create_tokenizer(train_descriptions)
# save the tokenizer
dump(tokenizer, open(code_root_dir + 'tokenizer_resnet50.pkl', 'wb'))
