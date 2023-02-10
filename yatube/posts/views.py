from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

# Главная страница
def index(request):
    template = 'posts\index.html'
    title = 'Главная страница Yatube'
    context = {
        'title': title, 
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts\group_list.html'
    title = 'Yatube группы'
    context = {
        'title': title,
    }
    return render(request, template, context)