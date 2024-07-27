from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'first'),
    path('second', views.second, name = 'second'),
    path('three', views.third, name = 'third'),
    path('four', views.fourth, name = 'fourth'),
]