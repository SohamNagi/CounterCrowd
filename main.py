from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from pygooglenews import GoogleNews
from crypt import methods
from flask import Flask, jsonify, request
import json
#Import Libraries For WebScraping and Sentiment Analysis
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from pygooglenews import GoogleNews

def news_process(topic):
    #Classes
    gn = GoogleNews(lang = 'en', country = 'US')
    analyzer = SentimentIntensityAnalyzer()


    articles=gn.search(topic)
    try:
        title=(articles['entries'][0]['title'])
        link=(articles['entries'][0]['link'])
        score=((analyzer.polarity_scores(str(articles['entries'][0]['title'])))['compound'])
    except:
        return jsonify({"list":[{"title":"NA","link":"NA","score":9000}]})
    cur_data=[{"title":title,"link":link,"score":score}]
    data={"list":cur_data}


    for pos,item in enumerate(articles['entries']):
        if pos==0:
            continue
        title=(item['title'])
        link=(item['link'])
        score= (analyzer.polarity_scores(str(item['title'])))['compound']
        cur_data=cur_data={"title":title,"link":link,"score":score}
        data["list"].append(cur_data)
    return data


app=Flask(__name__)
@app.route("/", methods=['GET','POST'])
def hello():
    return jsonify({"about":"Hello World!"})

@app.route('/multi/<string:topic>', methods=['GET'])
def get_multiply10(topic):
    
    return news_process(topic)

    articles=gn.search(topic)
    
    for item in articles['entries']:
        print(item['title'])
    return jsonify({'result':num*10})
if __name__=='__main__':
    app.run(host='0.0.0.0',port=3000,debug=True)