from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("<h1>Это мой первый проект на Django</h1>")
    return render(request, 'news/news_page.html')