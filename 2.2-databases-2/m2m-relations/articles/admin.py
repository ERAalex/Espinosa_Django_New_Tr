from django.contrib import admin
from .models import Article, Categories, ScopeDecision

class ScopeDecisionInline(admin.TabularInline):
    model = ScopeDecision
    min_num = 1
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', )
    inlines = [ScopeDecisionInline, ]

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('scope',)

