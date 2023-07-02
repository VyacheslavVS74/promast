from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Изображение')
    content = models.TextField(blank=True, verbose_name='Контент')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-time_created']

    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"


class Review(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Пользователь')
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='Пост')
    text = models.TextField(null=False, blank=False, verbose_name='Комментарий')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата комментария')

    def __str__(self):
        return self.text

    class Meta:
        unique_together = [['owner', 'post']]
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
