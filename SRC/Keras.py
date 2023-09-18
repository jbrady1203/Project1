import re
import pandas as pd
import numpy as np
import os
import sklearn
# from sklearn.preprocessing import LabelEncoder
# from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import keras
# from sklearn.metrics import classification_report
# from sklearn.metrics import accuracy_score
import math
import nltk
from nltk.corpus import stopwords

#packages articles uses to go through keras

#read in the dataset
data = pd.read_csv('DATA/articles_dataset.csv')
print(data)


#Remove all tags, urls, and non alpha numerical characters
def remove_tags(string):
    removelist = ""
    result = re.sub(r'[^w'+removelist+']', ' ',string)    #remove non-alphanumeric characters 
    result = result.lower()
    return result
data['Text']=data['Text'].apply(lambda cw : remove_tags(cw))

print(data)


#Remove stopwords (and, the, at) from the text
# nltk.download('stopwords')
# stop_words = set(stopwords.words('english'))
# data['Text'] = data['Text'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))



# tokenizing and lemmatizing the data
# w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
# lemmatizer = nltk.stem.WordNetLemmatizer()
# def lemmatize_text(text):
#     st = ""
#     for w in w_tokenizer.tokenize(text):
#         st = st + lemmatizer.lemmatize(w) + " "
#     return st
# data['Text'] = data.Text.apply(lemmatize_text)
# data