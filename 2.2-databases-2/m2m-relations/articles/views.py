from django.shortcuts import render
from articles.models import Article, ScopeDecision

def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.all().order_by('title')   # используйте упорядочивания результатов по названию
    order_scope = ScopeDecision.objects.all().order_by('is_main')
    context = {'object_list': object_list, 'order_scope': order_scope}




    return render(request, template, context)
