from django.db import models

# Create your models here.
class news_posts(models.Model):
    title = models.CharField('Название')
    short_descr = models.CharField('Кратко', max_length=200)
    content = models.TextField('Содержание')
    pub_date = models.DateTimeField('Дата')
