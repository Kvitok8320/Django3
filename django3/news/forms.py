from .models import news_posts
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class news_postsForm(ModelForm):
	class Meta:
		model = news_posts
		fields = ['title', 'short_descr', 'content', 'pub_date']
		widgets = {
			'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок новости'}),
			'short_descr': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание новости'}),
			'content': Textarea(attrs={'class': 'form-control', 'placeholder': 'Содержание новости'}),
			'pub_date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'})
		}