from django import forms
from .models import Order
from portfolio.models import Works
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget


class OrderForm(forms.ModelForm):
    order_works = forms.ModelChoiceField(queryset=Works.objects.all(), widget=forms.HiddenInput())
    order_phone = PhoneNumberField(widget=PhoneNumberInternationalFallbackWidget(), label='Телефон')

    class Meta:
        model = Order
        fields = ['order_works', 'order_name', 'order_phone', 'order_email']
        labels = {'order_phone': 'Телефон'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['order_phone'].widget.attrs.update({"placeholder": '+72125552368'})
        self.fields['order_name'].widget.attrs.update({"placeholder": 'Введите ваше Имя'})
        self.fields['order_email'].widget.attrs.update({"placeholder": 'Введите вашу почту'})
