from django.shortcuts import render, redirect
from .models import news_posts
from .forms import news_postsForm

def home(request):
    # return HttpResponse("<h1>Это мой первый проект на Django</h1>")
    news = news_posts.objects.all()
    return render(request, 'news/news_page.html',{'news': news})

def add_news(request):
    error = ""
    if request.method == 'POST':
        form = news_postsForm(request.POST)  # Сюда сохранится информация от пользователя.
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Данные были заполнены некорректно"
    form = news_postsForm()
    # return HttpResponse("<h1>Это мой первый проект на Django</h1>")
    return render(request, 'news/create_news.html', {'form': form, 'error': error})