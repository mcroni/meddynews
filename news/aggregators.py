import requests
import random

news_vendors = ['reddit',"newsapi"]


class NewsAggregator:
    def __init__(self,vendor,query=None):
        self.vendor = vendor
        self.query = query
        self.news = []

    def search_by_vendor(self):
        for news_vendor in news_vendors:

            if news_vendor == "reddit":
                url = "https://www.reddit.com/r/news/.json" if self.query is None else \
                    "https://www.reddit.com/r/{}/.json".format(self.query)
                news = []
                try:
                    response = requests.get(url=url,headers={'User-agent': 'Mozilla/5.0'}).json()['data']['children']
                    for i in response:
                        data = {
                            "headline": i['data']['title'],
                            "link": i['data']['url'],
                            "source": 'reddit'
                        }
                        news.append(data)
                    return news
                except ConnectionError as e:
                    return news

            if news_vendor == "newsapi":
                parameters = {'apiKey': '0837d40b0c74488fb26770bce8c781f4', 'language': "en"}
                if self.query is not None:
                    parameters['q'] = self.query
                url = 'https://newsapi.org/v2/top-headlines?'
                news = []
                try:
                    response = requests.get(url, params=parameters).json()['articles']
                    print(response)
                    for i in response:
                        data = {
                            "headline": i['title'],
                            "link": i['url'],
                            "source": "newsapi"
                        }
                        news.append(data)
                    print(news)
                except ConnectionError as e:
                    pass




news = NewsAggregator("newsapi","bitcoin")
print(news.search_by_vendor())