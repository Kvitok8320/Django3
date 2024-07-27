from django.db import models

# Create your models here.
class news_posts(models.Model):
    title = models.CharField('Название', max_length=100)
    short_descr = models.CharField('Кратко', max_length=200)
    content = models.TextField('Содержание')
    pub_date = models.DateTimeField('Дата')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'