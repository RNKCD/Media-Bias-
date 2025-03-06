#This program collects the news article with the use of NEWS API.
#API key is saved in docs.
#We will be extracting link that will be fed to another program which can extract content of the article using newspaper3k.
import requests as rq

url = "https://newsapi.org/v2/everything?q=politics&pageSize=5&sources=cnn&apiKey=807a2ad7b25d4fa79925a813275d6af0"

# parms = {
#     'q':'politics',
#     'country':'us',
#     'pageSize': 5,
#     'apiKey': '807a2ad7b25d4fa79925a813275d6af0',

# }

response = rq.get(url)

data = response.json()

for articles in data['articles']:
    print(articles['content'])
    print(articles['url'])
    print("----------------------------------------------------------------")
