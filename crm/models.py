from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from portfolio.models import Works


class StatusCrm(models.Model):
    status_name = models.CharField(max_length=150, verbose_name='Название статуса')

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):

    order_works = models.ForeignKey(Works, on_delete=models.CASCADE, verbose_name='Работа')
    order_dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    order_name = models.CharField(max_length=50, verbose_name='Имя')
    order_phone = PhoneNumberField()
    order_email = models.EmailField(max_length=50, null=True, blank=True, verbose_name='Email')
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True,
                                     verbose_name='Статус', default=1)

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class CommentCrm(models.Model):
    comment_order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка')
    comment_text = models.TextField(verbose_name='Текст комментария')
    comment_dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
