from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')



def show_catalog(request):
    template = 'catalog.html'
    context = Phone.objects.all()
    return render(request, template, {'context' : context})


def sort_name(request):
    template = 'product.html'
    context = Phone.objects.filter().order_by('name')
    return render(request, template, {'context' : context})

def sort_price_max(request):
    template = 'product.html'
    context = Phone.objects.filter().order_by('price')
    return render(request, template, {'context' : context})

def sort_price_min(request):
    template = 'product.html'
    context = Phone.objects.filter().order_by('price').reverse()
    return render(request, template, {'context' : context})





def show_product(request, slug):
    template = 'product.html'
    context = Phone.objects.filter(name=slug)
    return render(request, template, {'context' : context})
