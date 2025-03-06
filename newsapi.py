#This program collects the news article with the use of NEWS API.
#API key is saved in docs.
#We will be extracting link that will be fed to another program which can extract content of the article using newspaper3k.
import requests as rq

url = "https://newsapi.org/v2/everything"

# Define parameters properly
params = {
    'q': 'politics',
    'sources': 'cnn',  # 'sources' cannot be used with 'country' in NewsAPI
    'pageSize': 5,
    'apiKey': '807a2ad7b25d4fa79925a813275d6af0',  # Ensure API key is valid
}

# Make the request with params
response = rq.get(url, params=params)

# Convert response to JSON
data = response.json()

# Check if the response contains articles
if 'articles' in data:
    for article in data['articles']:
        print(article['content'])
        print(article['url'])
        print("----------------------------------------------------------------")
else:
    print("Error:", data.get('message', 'Unknown error'))
