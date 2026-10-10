from django.shortcuts import render

# Create your views here.
from .models import Article

# 参考 
# https://docs.djangoproject.com/zh-hans/4.1/intro/tutorial03/#a-shortcut-render

def index(request):
    blog_list = Article.objects.order_by('title')
    context = {'blog_list':blog_list}
    return render(request, 'blog.html', context)