from django.http import HttpResponse
from django.shortcuts import render
from .models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})

def categories(request, cat):
    print(request.GET)
    return HttpResponse(f"<h1> Page for cats {cat}</h1>")

def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})

