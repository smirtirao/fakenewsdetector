import nltk
import requests
import json
import datetime
from textblob import TextBlob

api_key = "50000e65e0c44c198719f8e60c7a8a89" 
base_url = "https://newsapi.org/v2/everything?"

user_input= input("Enter headline here:") 
query= TextBlob(user_input)
for words, tag in query.tags :
 print(words, tag)
for sentence in query.sentences:
  print(sentence.sentiment.polarity)


testFile = open("data.json","w") # Write contentes to a file

def get_news(api_key,options):
    constructor_string = []
    if 'q' in options:
        constructor_string.append("q=" + options['q'])
    if 'from' in options:
        constructor_string.append("from=" + options['from'])
    if 'sortBy' in options:
        constructor_string.append("sortBy=" + options['sortBy'])
    constructor_string.append("apiKey="+api_key)

    full_query = base_url + '&'.join(constructor_string)

    r = requests.get(full_query)
    if r.status_code == 200:
        data = r.json()
        for x in data['articles']:
            blob = TextBlob(x['description'])
            x['ner'] = blob.tags
        formatted = json.dumps(data,indent=4)
        testFile.write(formatted)


get_news(api_key, {"q":user_input,"sortBy":"publishedAt","from":"2019-01-10"})