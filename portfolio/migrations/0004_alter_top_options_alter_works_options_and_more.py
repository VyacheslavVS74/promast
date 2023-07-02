# Generated by Django 4.1.7 on 2023-05-26 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_works_material'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='top',
            options={'verbose_name': 'Популярный проект', 'verbose_name_plural': 'Популярные проекты'},
        ),
        migrations.AlterModelOptions(
            name='works',
            options={'ordering': ['-created'], 'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AlterField(
            model_name='top',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата Добавления'),
        ),
        migrations.AlterField(
            model_name='top',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Популярное'),
        ),
        migrations.AlterField(
            model_name='works',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='works',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='works',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio/%Y/%m/%d/', verbose_name='Изображение 1'),
        ),
        migrations.AlterField(
            model_name='works',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio/%Y/%m/%d/', verbose_name='Изображение 2'),
        ),
        migrations.AlterField(
            model_name='works',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio/%Y/%m/%d/', verbose_name='Изображение 3'),
        ),
        migrations.AlterField(
            model_name='works',
            name='material',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Материал'),
        ),
        migrations.AlterField(
            model_name='works',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='works',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='works',
            name='top_sales',
            field=models.ManyToManyField(blank=True, to='portfolio.top', verbose_name='Популярное'),
        ),
    ]