from django.urls import path
from news.views import news, query

urlpatterns = [
    path('', news,name="news"),
    path('query/<str:query>/', query, name='query'),

]
