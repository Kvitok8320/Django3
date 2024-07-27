from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("<h1>Это мой первый проект на Django</h1>")
    return render(request, 'first/index.html')


def second(request):
    # return HttpResponse("<h1>Это Вторая страница из мой первый проект на Django</h1>")
    return render(request, 'first/second.html')


def third(request):
    # return HttpResponse("<h1>Это мой первый проект на Django</h1>")
    return render(request, 'first/third.html')


def fourth(request):
    # return HttpResponse("<h1>Это Вторая страница из мой первый проект на Django</h1>")
    return render(request, 'first/fourth.html')




# Create your views here.
