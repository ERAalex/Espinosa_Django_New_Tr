from django.core.paginator import Paginator
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
    template = 'books/book_pag.html'
    context = Book.objects.filter(pub_date=slug)
    name_give = slug

    show_l = Book.objects.filter().order_by('pub_date')



    page = request.GET.get('page', 1)

    paginator = Paginator(show_l, 1)
    try:
        book_show = paginator.page(page)
    except PageNotAnInteger:
        book_show = paginator.page(1)
    except EmptyPage:
        book_show = paginator.page(paginator.num_pages)

    for i in book_show.paginator.page_range:
        if context in show_l:
            yes = i
        else:
            yes = 'netu'
        return yes



    return render(request, template, {'context' : context, 'yes': yes, 'name_give' : name_give, 'book_show': book_show})




