from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('second', views.second),
    path('three', views.third),
    path('four', views.fourth),
]