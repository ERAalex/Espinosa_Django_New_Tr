from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')




def show_catalog(request):
    template = 'catalog.html'
    context = Phone.objects.all()
    return render(request, template, {'context' : context})


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
