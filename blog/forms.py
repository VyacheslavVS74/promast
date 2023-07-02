from .models import Review
from django.forms import ModelForm


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        labels = {
            'text': 'Добавьте комментарий'
        }
