from textblob import TextBlob
import pandas as pd


def text_blob(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return sentiment[0]

data = pd.read_csv("DATA/articles_dataset.csv")
data["TextBlob Sentiment"] = data["Text"].apply(text_blob)

def get_political_lean(text_sentiment):
    political_avgs = data.groupby('Political Lean').mean()
    conservative_avg = political_avgs["TextBlob Sentiment"][0]
    liberal_avg = political_avgs["TextBlob Sentiment"][1]
    if abs(text_sentiment - liberal_avg) - abs(text_sentiment - conservative_avg) <= 0:
        return "Liberal"
    else:
        return "Conservative"

data["Political Sentiment"] = data["TextBlob Sentiment"].apply(get_political_lean)

print(data)