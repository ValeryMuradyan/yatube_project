from django.shortcuts import render

from .models import Post

# Create your views here.

# Главная страница
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts, 
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    template = 'posts\group_list.html'
    title = 'Yatube группы'
    context = {
        'title': title,
    }
    return render(request, template, context)