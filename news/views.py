import requests
import random
from newsapi import NewsApiClient
from django.http import JsonResponse

# api client for newsapi for better searching
newsapi = NewsApiClient(api_key='0837d40b0c74488fb26770bce8c781f4')

# list of news aggregators
news_vendors = {
    "reddit": "https://www.reddit.com/r/{}/.json",
    "newsapi": 'https://newsapi.org/v2/top-headlines?country=us&apiKey=0837d40b0c74488fb26770bce8c781f4'
}


def news(request):
    """generic view for grabbing news from the various apis listed above"""
    news = []
    for vendor, url in news_vendors.items():
        if vendor == "reddit":
            try:
                response = requests.get(url=url.format("news"), headers={'User-agent': 'Mozilla/5.0'}).json()['data']['children']
                for i in response:
                    data = {
                        "headline": i['data']['title'],
                        "link": i['data']['url'],
                        "source": vendor
                    }
                    news.append(data)
            except ConnectionError as e:
                pass

        if vendor == "newsapi":
            try:
                response = requests.get(url=url, headers={'User-agent': 'Mozilla/5.0'}).json()['articles']
                for i in response:
                    data = {
                        "headline": i['title'],
                        "link": i['url'],
                        "source": vendor
                    }
                    news.append(data)
            except ConnectionError as e:
                pass

    random.shuffle(news)
    return JsonResponse(data=news, safe=False)


def query(request,query):
    """view to implement a feature that allows someone to search."""
    news = []
    for vendor, url in news_vendors.items():
        if vendor == "newsapi":
            try:
                all_articles = newsapi.get_everything(q=query,language='en')['articles']
                for i in all_articles:
                    data = {
                        "headline": i['title'],
                        "link": i['url'],
                        "source": vendor
                    }
                    news.append(data)
            except ConnectionError as e:
                pass

        if vendor == "reddit":
            try:
                response = requests.get(url=url.format(query), headers={'User-agent': 'Mozilla/5.0'}).json()['data']['children']
                for i in response:
                    data = {
                        "headline": i['data']['title'],
                        "link": i['data']['url'],
                        "source": vendor
                    }
                    news.append(data)
            except ConnectionError as e:
                pass

    random.shuffle(news)
    return JsonResponse(data=news, safe=False)
