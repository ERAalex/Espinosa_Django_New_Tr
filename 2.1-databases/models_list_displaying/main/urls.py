from django.contrib import admin
from django.urls import path
from books.views import books_view




urlpatterns = [
    path('', books_view, name='books'),
    path('admin/', admin.site.urls),
]
