from .models import news_posts
from django.forms import ModelForm

class news_postsForm(ModelForm):
	class Meta:
		model = news_posts
		fields = ['title', 'short_descr', 'content', 'pub_date']