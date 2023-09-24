import re
import pandas as pd
import numpy as np
import os
import random
import sklearn

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import keras

# from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
import math
import nltk
from nltk.corpus import stopwords

nltk.download("wordnet")

# packages articles uses to go through keras

# read in the dataset
data = pd.read_csv("DATA/articles_dataset.csv")
# print(data)


# removing non-alphanumeric characters and changing all text to lowercase
data["Clean_Text"] = data["Text"].str.replace("-", " ")
data["Clean_Text"] = data["Clean_Text"].str.replace("[^a-zA-Z0-9\s]", "", regex=True)
data["Clean_Text"] = data["Clean_Text"].str.lower()
# print(data)


# Remove stopwords (and, at, the, etc.) from the text
nltk.download("stopwords")
stop_words = (set(stopwords.words("english")),)
data["Clean_Text"] = data["Clean_Text"].apply(
    lambda x: " ".join([word for word in x.split() if word not in (stop_words)])
)
# print(data)

# tokenizing and lemmatizing the data
w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
lemmatizer = nltk.stem.WordNetLemmatizer()


def lemmatize_text(text):
    st = ""
    for w in w_tokenizer.tokenize(text):
        st = st + lemmatizer.lemmatize(w) + " "
    return st


data["tokenized"] = data.Clean_Text.apply(lemmatize_text)

# print(data.tokenized)

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

random.seed(1)

text = data["tokenized"].values
labels = data["Political Lean"].values
encoder = LabelEncoder()
encoded_labels = encoder.fit_transform(labels)

train_text, test_text, train_labels, test_labels = train_test_split(
    text, encoded_labels, stratify=encoded_labels, test_size=0.2
)

vocab_size = 30000  # choose based on statistics
oov_tok = ""
embedding_dim = 300
max_length = 5000
padding_type = "post"
trunc_type = "post"
# tokenize sentences
tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
tokenizer.fit_on_texts(train_text)
word_index = tokenizer.word_index
# convert train dataset to sequence and pad sequences
train_sequences = tokenizer.texts_to_sequences(train_text)
train_padded = pad_sequences(train_sequences, padding="post", maxlen=max_length)
# convert Test dataset to sequence and pad sequences
test_sequences = tokenizer.texts_to_sequences(test_text)
test_padded = pad_sequences(test_sequences, padding="post", maxlen=max_length)


# https://www.analyticsvidhya.com/blog/2022/01/sentiment-analysis-with-lstm/

# model initialization
model = keras.Sequential(
    [
        keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
        keras.layers.Bidirectional(keras.layers.LSTM(64)),
        keras.layers.Dense(24, activation="relu"),
        keras.layers.Dense(1, activation="sigmoid"),
    ]
)
# compile model
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
# model summary
model.summary()

num_epochs = 15
history = model.fit(
    train_padded, train_labels, epochs=num_epochs, verbose=1, validation_split=0.15
)


prediction = model.predict(test_padded)
# Get labels based on probability 1 if p>= 0.5 else 0
pred_labels = []
for i in prediction:
    if i >= 0.5:
        pred_labels.append(1)
    else:
        pred_labels.append(0)
print("Accuracy of prediction on test set : ", accuracy_score(test_labels, pred_labels))
