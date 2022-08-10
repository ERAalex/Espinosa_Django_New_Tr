from django.db import models



class Categories(models.Model):
    scope = models.CharField(max_length=256, verbose_name='Сфера')

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.scope

class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class ScopeDecision(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='positions')
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='positions')
    is_main = models.BooleanField(default=False, verbose_name='Основной')


    class Meta:
        verbose_name = 'Тематики раздела'
        verbose_name_plural = 'Тематики раздела'
