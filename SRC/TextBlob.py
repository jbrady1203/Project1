from textblob import TextBlob
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split

# gets the sentiment of each article on a scale of -1 (negative sentiment) to 1 (positive sentiment)
def text_blob(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return sentiment[0]

# reading in dataset
data = pd.read_csv("DATA/articles_dataset.csv")
# 80% of data in train, 20% in test
train, test = train_test_split(data, test_size=0.2, random_state=0)

# gets sentiments for train and test dfs
train["TextBlob Sentiment"] = train["Text"].apply(text_blob)
test["TextBlob Sentiment"] = test["Text"].apply(text_blob)

# gets the mean sentiment score for each political lean for the train df
political_avgs = train.groupby('Political Lean').mean(numeric_only=True)
print(political_avgs)
conservative_avg = political_avgs["TextBlob Sentiment"][0]
liberal_avg = political_avgs["TextBlob Sentiment"][1]

# if an article's (from test df) sentiment is closer to the liberal avg, it is predicted to be liberal otherwise conservative
def get_political_lean(text_sentiment):
    if abs(text_sentiment - liberal_avg) - abs(text_sentiment - conservative_avg) <= 0:
        return "Liberal"
    else:
        return "Conservative"

test["Political Sentiment"] = test["TextBlob Sentiment"].apply(get_political_lean)

# print(train)

# gets the percentage of accurate predictions 
test["Accurate"] = test["Political Lean"] == test["Political Sentiment"]
accuracy = (test["Accurate"].value_counts()[0] / len(test)) * 100
print("Accurate Percentage of Predictions: ", accuracy, "%")

# print(test)

# gets the percentage of accurate predictions for liberal leaning articles
num_liberal_accurate = test[(test["Political Lean"] == "Liberal") & (test["Accurate"] == True)].count()[0]
liberal_accuracy = (num_liberal_accurate/(test["Political Lean"].value_counts()[0])) * 100
print("Accurate Percentage of Predictions for Liberal Leaning Articles: ", liberal_accuracy, "%")

# gets the percentage of accurate predictions for conservative leaning articles
num_conservative_accurate = test[(test["Political Lean"] == "Conservative") & (test["Accurate"] == True)].count()[0]
conservative_accuracy = (num_conservative_accurate/(test["Political Lean"].value_counts()[1])) * 100
print("Accurate Percentage of Predictions for Conservative Leaning Articles: ", conservative_accuracy, "%")

