
from django.shortcuts import render, redirect
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = Book.objects.all()
    return render(request, template, {'context': context})


def sort_name(request):
    template = 'books/books_list.html'
    context = Book.objects.filter().order_by('name')
    return render(request, template, {'context' : context})

def sort_date_old(request):
    template = 'books/books_list.html'
    context = Book.objects.filter().order_by('pub_date')
    return render(request, template, {'context' : context})

def sort_date_new(request):
    template = 'books/books_list.html'
    context = Book.objects.filter().order_by('pub_date').reverse()
    return render(request, template, {'context' : context})


def show_book(request, slug):
    template = 'books/books_list.html'
    context = Book.objects.filter(pub_date=slug)
    return render(request, template, {'context' : context})

