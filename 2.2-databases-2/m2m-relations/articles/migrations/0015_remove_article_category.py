# Generated by Django 4.0.3 on 2022-08-09 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_remove_categories_is_main'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
    ]
