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

nltk.download("wordnet")

# packages articles uses to go through keras

# read in the dataset
data = pd.read_csv("DATA/articles_dataset.csv")
print(data)


# removing non-alphanumeric characters and changing all text to lowercase
data["Clean_Text"] = data["Text"].str.replace("-", " ")
data["Clean_Text"] = data["Clean_Text"].str.replace("[^a-zA-Z0-9\s]", "", regex=True)
data["Clean_Text"] = data["Clean_Text"].str.lower()
print(data)


# Remove stopwords (and, at, the, etc.) from the text
nltk.download("stopwords")
stop_words = (set(stopwords.words("english")),)
data["Clean_Text"] = data["Clean_Text"].apply(
    lambda x: " ".join([word for word in x.split() if word not in (stop_words)])
)
print(data)

# tokenizing and lemmatizing the data
w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
lemmatizer = nltk.stem.WordNetLemmatizer()


def lemmatize_text(text):
    st = ""
    for w in w_tokenizer.tokenize(text):
        st = st + lemmatizer.lemmatize(w) + " "
    return st


data["tokenized"] = data.Clean_Text.apply(lemmatize_text)

print(data.tokenized)

s = 0.0
for i in data["tokenized"]:
    word_list = i.split()
    s = s + len(word_list)
print("Average length of each article : ", s / data.shape[0])
liberal = 0
for i in range(data.shape[0]):
    if data.iloc[i]["Political Lean"] == "Liberal":
        liberal = liberal + 1
conservative = data.shape[0] - liberal
print(
    "Percentage of reviews with positive sentiment is "
    + str(liberal / data.shape[0] * 100)
    + "%"
)
print(
    "Percentage of reviews with negative sentiment is "
    + str(conservative / data.shape[0] * 100)
    + "%"
)

# https://www.analyticsvidhya.com/blog/2022/01/sentiment-analysis-with-lstm/
