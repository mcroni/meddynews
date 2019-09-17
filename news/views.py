from django.shortcuts import render
import requests
from django.http import JsonResponse
import random
# Create your views here.
news_vendors = {
    "reddit": "https://www.reddit.com/r/news/.json",
    "newsapi":'https://newsapi.org/v2/top-headlines?country=us&apiKey=0837d40b0c74488fb26770bce8c781f4'
}


def news(request):
    """generic view for grabbing news from the various apis listed above"""
    news = []
    for vendor,url in news_vendors.items():
        if vendor == "reddit":
            try:
                response = requests.get(url=url, headers={'User-agent': 'Mozilla/5.0'}).json()['data']['children']
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
    return JsonResponse(data=news,safe=False)