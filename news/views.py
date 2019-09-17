import requests
import random
from newsapi import NewsApiClient
from django.http import JsonResponse
from news.aggregators import NewsAggregator




def news(request):
    """generic view for grabbing news from the various apis listed above"""
    news = NewsAggregator().search_by_vendor()
    return JsonResponse(data=news, safe=False)


def query(request,query):
    """view to implement a feature that allows someone to search."""
    news = NewsAggregator(query=query).search_by_vendor()
    return JsonResponse(data=news, safe=False)
