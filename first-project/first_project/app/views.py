from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os



def home_view(request):
    template_name = 'app/home.html'

    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):

    msg = f'Текущее время: {datetime.datetime.now().time()}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории

    path = "first_project"     # можно любую папку поставить (даже локальный диск C)
    list_of_files =os.listdir(path)
    return render(request, 'app/directory_show.html', {'show_files': list_of_files})
