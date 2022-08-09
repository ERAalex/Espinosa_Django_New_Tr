from django.contrib import admin

from .models import Article, Categories


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', )

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('scope', )

