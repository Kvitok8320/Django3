from django.http import HttpResponse
from django.shortcuts import render
from .models import news_posts
from .models import news_posts

def home(request):
    # return HttpResponse("<h1>Это мой первый проект на Django</h1>")
    news = news_posts.objects.all()
    return render(request, 'news/news_page.html',{'news': news})

def add_news(request):
    # return HttpResponse("<h1>Это мой первый проект на Django</h1>")
    return render(request, 'news/create_news.html')