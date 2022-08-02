from django.db import models
from datetime import date


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, blank=True)
    image = models.ImageField(upload_to='static/img', blank=True)
    price = models.CharField(max_length=60, blank=True)
    release_date = models.DateField(default=date.today)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)