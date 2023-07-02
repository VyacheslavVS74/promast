from django.db import models


class Works(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    image_1 = models.ImageField(upload_to='portfolio/%Y/%m/%d/', null=True, blank=True, verbose_name='Изображение 1')
    image_2 = models.ImageField(upload_to='portfolio/%Y/%m/%d/', null=True, blank=True, verbose_name='Изображение 2')
    image_3 = models.ImageField(upload_to='portfolio/%Y/%m/%d/', null=True, blank=True, verbose_name='Изображение 3')
    top_sales = models.ManyToManyField('Top', blank=True, verbose_name='Популярное')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    price = models.IntegerField(default=0, verbose_name='Цена')
    material = models.CharField(max_length=100, null=True, blank=True, verbose_name='Материал')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class Top(models.Model):
    name = models.CharField(max_length=100, verbose_name='Популярное')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата Добавления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Популярный проект"
        verbose_name_plural = "Популярные проекты"
