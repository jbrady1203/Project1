# Project1

## Content description here

# SRC 
### Code installation
Ensure that you have python3 installed on your computer. While not required, it is also suggested that you run the following installation commands within a python virtual environment. Information about setting up a virtual environment can be found [here](https://docs.python.org/3/library/venv.html).

To install this code make sure to install the following packages:
- ```pip install scikit-learn```
- ```pip install textblob```
- ```pip install pandas```
- ```pip install numpy```
- ```pip install keras```
- ```pip install nltk```
### Code Usage
To run the Keras package use the command ```python3 SRC/Keras.py```.\
The hyperparameters that you can modify on the keras package are ```vocab_size```, ```embedding_dim```, ```max_length```, and ```num_epochs```.

To run the TextBlob package use the command ```python3 SRC/TextBlob.py```.\
TextBlob is a pre-trained package, so there are no hyperparameters to adjust.

# Data 
| Attribute Name | Data Type | Required | Description | Example |
| -------------- | --------- | -------- | ----------- | ------- |
| News Outlet | String | Yes | The name of the news outlet which the article is from | "CNN" |
| Article | String | Yes | All the raw text from the article | "Article Title + Body Text" |
| Political Lean | String | Yes | "Liberal" if the article has a liberal perspective on climate change, otherwise "Conservatice" | "Liberal" |

# Figures
| Figure | Description | Takeaway | 
| -------------- | --------- | ------ |
| Frequency of Political Lean in Articles Barplot| This plot shows the number of articles that lean liberal or conservative for each news outlet. |  Our dataset is composed of more articles that have a liberal perspective on climate change as opposed to a conservative perspective. |
| Number of Articles for each News Outlet Barplot | This plot shows the number of articles for each news outlet | We have about 15 articles from a diverse set of outlets | 
Analysis Flowchart | This shows the structure we used to analyze our data | We used the TextBlob and LSTM models to classify our data and then compare the results

# References 

<a id="1">[1]</a>  J. Mcgonical and A. Samuels, “News sentiment analysis,” arxiv, https://arxiv.org/pdf/2007.02238 (accessed Sep. 10, 2023). <br>
<a id="2">[2]</a>  E. H.-J. Kim, M. Song, K. Y. Kang, Y. Kim, and Y. K. Jeong, “Topic-based content and sentiment analysis of Ebola virus on Twitter and in the news,” Sage Journals, https://journals.sagepub.com/doi/10.1177/0165551515608733 (accessed Sep. 10, 2023). <br>
<a id="3">[3]</a>  C. Funk, “The politics of climate,” Pew Research Center Science & Society, https://www.pewresearch.org/science/2016/10/04/the-politics-of-climate/ (accessed Sep. 10, 2023). <br>
<a id="4">[4]</a>  “What is climate change?,” United Nations, https://www.un.org/en/climatechange/what-is-climate-change (accessed Sep. 10, 2023). <br>
<a id="5">[5]</a>  A. Mitchell, “Section 1: Media sources: Distinct favorites emerge on the left and right,” Pew Research Center’s Journalism Project, https://www.pewresearch.org/journalism/2014/10/21/section-1-media-sources-distinct-favorites-emerge-on-the-left-and-right/ (accessed Sep. 10, 2023). <br>
<a id="6">[6]</a>  C. Russell, “Climate change in the media: Public perception and the responsibility of news outlets,” Earth Day, https://www.earthday.org/climate-change-in-the-media-public-perception-and-the-responsibility-of-news-outlets/#:~:text=There%20are%20good%20steps%20being,87%2C000%20in%202020%20to%202021 (accessed Sep. 10, 2023). <br>
<a id="7">[7]</a> M. Phi, “Illustrated guide to LSTM’s and GRU’s: A step by step explanation,” Medium, https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21 (accessed Sep. 10, 2023). <br>
<a id="8">[8]</a> G. M. Elizabeth Morrissette, “Media bias,” Introduction to Media Studies, https://pressbooks.pub/mediastudies/chapter/media-bias/ (accessed Sep. 10, 2023).<br>
<a id="9">[9]</a> S. Agrawal, “Sentiment analysis using LSTM step-by-step,” Medium, https://towardsdatascience.com/sentiment-analysis-using-lstm-step-by-step-50d074f09948 (accessed Sep. 10, 2023). <br>
<a id="10">[10]</a> K. D. Chaudhuri, “Sentiment Analysis with LSTM,” Analytics Vidhya, https://www.analyticsvidhya.com/blog/2022/01/sentiment-analysis-with-lstm/ (accessed Sep. 10, 2023).<br>
<a id="11">[11]</a> A. PSS, “Sentiment Analysis Using LSTM,” Medium, https://medium.com/mlearning-ai/sentiment-analysis-using-lstm-21767a130857 (accessed Sep. 17, 2023). <br>
<a id="12">[12]</a> J. Karra, “Sentiment Analysis Using LSTM,” Medium, https://jagathprasad0.medium.com/sentiment-analysis-using-lstm-b3efee46c956 (accessed Sep. 17, 2023).<br>
<a id="13">[13]</a> S. Saxena, “What is LSTM? introduction to long short-term memory,” Analytics Vidhya, https://www.analyticsvidhya.com/blog/2021/03/introduction-to-long-short-term-memory-lstm/ (accessed Sep. 17, 2023).<br>
<a id="14">[14]</a> T. Tran, “Deep learning for sentiment analysis,” Kaggle, https://www.kaggle.com/code/tientd95/deep-learning-for-sentiment-analysis (accessed Sep. 17, 2023).<br>
<a id="15">[15]</a> K. Team, “Keras Documentation: LSTM Layer,” Keras, https://keras.io/api/layers/recurrent_layers/lstm/ (accessed Sep. 17, 2023).<br>
<a id="16">[16]</a> N. Van Otten, “Top 5 best sentiment analysis tools in Python & How to use them to get started,” Spot Intelligence, https://spotintelligence.com/2022/12/16/sentiment-analysis-tools-in-python/#Examples_of_how_to_do_sentiment_analysis_in_Python (accessed Sep. 17, 2023).<br>
<a id="17">[17]</a> [Milestone 1 Document](https://docs.google.com/document/d/1RPxb62up4iGrQZO2CqC3ci4BGjlRUp7t4tXi-bIsiEo/edit?usp=sharing)\
<a id="18">[18]</a>[Milestone 2 Document](https://docs.google.com/document/d/1hkDPFE9-G6SREtNFBAGFkU9mRUYiwl0SrS5epVI_57E/edit?usp=sharing)