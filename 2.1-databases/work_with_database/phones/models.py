from django.db import models
from datetime import date
from django.utils.text import slugify


class Phone(models.Model):
    id = models.CharField(max_length=60, primary_key=True)
    name = models.CharField(max_length=60, blank=True)
    image = models.ImageField(upload_to='static/img', blank=True)
    price = models.CharField(max_length=60, blank=True)
    release_date = models.CharField(max_length=60, blank=True)
    lte_exists = models.CharField(max_length=60, blank=True)
    slug = models.SlugField(blank=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)
