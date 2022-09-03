#Import Libraries For WebScraping and Sentiment Analysis
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from pygooglenews import GoogleNews

#Classes
gn = GoogleNews(lang = 'en', country = 'US')
analyzer = SentimentIntensityAnalyzer()

prompt=input('What is The Topic You Want Information About: ')

articles=gn.search(prompt)

for item in articles['entries']:
    print(item['title'])
    print(item['link'])
    print (analyzer.polarity_scores(str(item['title'])))