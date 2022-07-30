from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


context = {'Name': '', 'Street':'', 'District': ''
    }

total = {

}



def bus_stations(request):
    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8' ) as csvfile:
        reader = csv.DictReader(csvfile)

        name = ['']
        street = ['']
        district = ['']

        for row in reader:
            nam = row['Name']
            stre = row['Street']
            distr = row['District']

            name.append(nam)
            street.append(stre)
            district.append(distr)

        context['Name'] = name
        context['Street'] = street
        context['District'] = district
        total['keys'] = context

    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице


    return render(request, 'stations/index.html', total)
