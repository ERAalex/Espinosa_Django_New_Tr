from django.contrib import admin
from django.urls import path
from books.views import books_view, sort_date_old, sort_date_new, sort_name, show_book




urlpatterns = [
    path('', books_view, name='books'),
    path('admin/', admin.site.urls),
    path('books_name', sort_name, name='sort_name'),
    path('books_old', sort_date_new, name='sort_date_old'),
    path('books_new', sort_date_old, name='sort_date_new'),
    path('catalog/<slug:slug>/', show_book, name='phone'),
]
