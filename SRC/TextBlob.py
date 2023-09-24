from textblob import TextBlob
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split


def text_blob(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return sentiment[0]

data = pd.read_csv("DATA/articles_dataset.csv")
train, test = train_test_split(data, test_size=0.2, random_state=0)

train["TextBlob Sentiment"] = train["Text"].apply(text_blob)
test["TextBlob Sentiment"] = test["Text"].apply(text_blob)

political_avgs = train.groupby('Political Lean').mean(numeric_only=True)
print(political_avgs)
conservative_avg = political_avgs["TextBlob Sentiment"][0]
liberal_avg = political_avgs["TextBlob Sentiment"][1]

def get_political_lean(text_sentiment):
    if abs(text_sentiment - liberal_avg) - abs(text_sentiment - conservative_avg) <= 0:
        return "Liberal"
    else:
        return "Conservative"

test["Political Sentiment"] = test["TextBlob Sentiment"].apply(get_political_lean)

print(train)

test["Accurate"] = test["Political Lean"] == test["Political Sentiment"]
print(test)

accuracy = (test["Accurate"].value_counts()[0] / len(test)) * 100
print("Accurate Percentage of Predictions: ", accuracy, "%")