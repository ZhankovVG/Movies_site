from .models import Reviews
from django import forms


class ReviewsForm(forms.ModelForm):
    # Форма отзывов
    class Meta:
        model = Reviews
        fields = ['email', 'name', 'text']
