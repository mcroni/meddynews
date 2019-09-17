import requests
import random

news_vendors = ['reddit',"newsapi"]

class NewsAggregator:
    def __init__(self,query=None):
        self.query = query
        self.news = []

    def search_by_vendor(self):
        for news_vendor in news_vendors:
            if news_vendor == "reddit":
                print("searching for reddit news")
                url = "https://www.reddit.com/r/news/.json" if self.query is None else \
                    "https://www.reddit.com/r/{}/.json".format(self.query)
                try:
                    response = requests.get(url=url,headers={'User-agent': 'Mozilla/5.0'}).json()['data']['children']

                    for i in response:
                        data = {
                            "headline": i['data']['title'],
                            "link": i['data']['url'],
                            "source": 'reddit'
                        }
                        # print(data)
                        self.news.append(data)
                except ConnectionError as e:
                    pass

            if news_vendor == "newsapi":
                print("searching for newsapi news")
                parameters = {'apiKey': '0837d40b0c74488fb26770bce8c781f4', 'language': "en"}
                if self.query is not None:
                    parameters['q'] = self.query
                url = 'https://newsapi.org/v2/top-headlines?'
                try:
                    response = requests.get(url, params=parameters).json()['articles']
                    for i in response:
                        data = {
                            "headline": i['title'],
                            "link": i['url'],
                            "source": "newsapi"
                        }
                        # print(data)
                        self.news.append(data)
                except ConnectionError as e:
                    pass

        random.shuffle(self.news)
        return self.news



#
# news = NewsAggregator("bitcoin")
# a = news.search_by_vendor()
# print(a)