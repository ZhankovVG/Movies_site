from .models import Reviews
from django import forms
# from snowpenguin.django.recaptcha3.fields import ReCaptchaField
# from captcha.fields import ReCaptchaField


class ReviewsForm(forms.ModelForm):
    # Форма отзывов
    # captcha = ReCaptchaField()

    class Meta:
        model = Reviews
        fields = ['email', 'name', 'text']
