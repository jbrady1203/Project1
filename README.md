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
| -------------- | --------- |
| Frequency of Political Lean in Articles | This plot shows the number of articles that lean liberal or conservative for each news outlet.

# References 

<a id="1">[1]</a>  J. Mcgonical and A. Samuels, “News sentiment analysis,” arxiv, https://arxiv.org/pdf/2007.02238 (accessed Sep. 10, 2023). <br>
<a id="2">[2]</a>  E. H.-J. Kim, M. Song, K. Y. Kang, Y. Kim, and Y. K. Jeong, “Topic-based content and sentiment analysis of Ebola virus on Twitter and in the news,” Sage Journals, https://journals.sagepub.com/doi/10.1177/0165551515608733 (accessed Sep. 10, 2023). <br>
<a id="3">[3]</a>  C. Funk, “The politics of climate,” Pew Research Center Science & Society, https://www.pewresearch.org/science/2016/10/04/the-politics-of-climate/ (accessed Sep. 10, 2023). <br>
<a id="4">[4]</a>  “What is climate change?,” United Nations, https://www.un.org/en/climatechange/what-is-climate-change (accessed Sep. 10, 2023). <br>
<a id="5">[5]</a>  A. Mitchell, “Section 1: Media sources: Distinct favorites emerge on the left and right,” Pew Research Center’s Journalism Project, https://www.pewresearch.org/journalism/2014/10/21/section-1-media-sources-distinct-favorites-emerge-on-the-left-and-right/ (accessed Sep. 10, 2023). <br>
<a id="6">[6]</a>  C. Russell, “Climate change in the media: Public perception and the responsibility of news outlets,” Earth Day, https://www.earthday.org/climate-change-in-the-media-public-perception-and-the-responsibility-of-news-outlets/#:~:text=There%20are%20good%20steps%20being,87%2C000%20in%202020%20to%202021 (accessed Sep. 10, 2023). <br>
<a id="7">[7]</a> <br>
<a id="8">[8]</a> <br>
<a id="9">[9]</a> <br>
<a id="10">[10]</a> <br>
<a id="11">[11]</a> <br>
<a id="12">[12]</a> <br>