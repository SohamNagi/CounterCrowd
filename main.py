#Import Libraries For WebScraping and Sentiment Analysis
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from pygooglenews import GoogleNews

gn = GoogleNews(lang = 'en', country = 'US')

prompt=input('What is The Topic You Want Information About: ')

articles=gn.search(prompt)

for item in articles['entries']:
    print(item['title'])