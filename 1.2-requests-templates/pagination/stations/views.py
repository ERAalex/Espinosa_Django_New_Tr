from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))



def bus_stations(request):
    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8' ) as csvfile:
        csv_file = list(csv.DictReader(csvfile))
    paginator = Paginator(csv_file, 10)
    current_page = request.GET.get('page', 1)
    page = paginator.get_page(current_page)
    context = {
        'Name': paginator.object_list,
        'page': page
    }
    return render(request, 'stations/index.html', context)
