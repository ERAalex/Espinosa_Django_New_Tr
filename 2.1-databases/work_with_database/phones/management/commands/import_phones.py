
import csv
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
        for phone in phones:
            data = Phone(id='id', name='name', image='image', price='price', release_date='release_date', lte_exists='lte_exists')
            data.save()

