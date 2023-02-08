from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

# Главная страница
def index(request):
    template = 'posts\index.html'
    title = 'YaTube'
    context = {
        'title': title,
        'text': 'Это главная страница проекта Yatube'
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts\group_list.html'
    title = 'YaTube'
    context = {
        'title': title,
        'text': 'Здесь будет информация о группах проекта Yatube'
    }
    return render(request, template)