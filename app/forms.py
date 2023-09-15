from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Testimonial, Register
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, Textarea

class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = ["login", "email", "password", "password2"]
        widgets = {
            "login": TextInput(attrs={
                'style': 'width: 600px; height: 50px; margin: auto; border-radius: 20px; border: 0; text-align: center;',
                'class': 'form-control',
                'placeholder': 'Придумайте логин',
        }),
            "email": EmailInput(attrs={
                'style': 'width: 500px; height: 50px; margin: auto; border-radius: 20px; border: 1px solid  White; text-align: center;',
                'class': 'form-control',
                'placeholder': 'Введите свой e-mail',
        }),

            "password": PasswordInput(attrs={
                'style': 'width: 400px; height: 50px; margin: auto; border-radius: 20px; border: 1px solid  White; text-align: center;',
                'class': 'form-control',
                'placeholder': 'Придумайте пароль',
        }),
            "password2": PasswordInput(attrs={
                'style': 'width: 300px; height: 50px; margin: auto; border-radius: 20px; border: 1px solid  White; text-align: center;',
                'class': 'form-control',
                'placeholder': 'Подтвердите пароль',
        })}

# class RegisterForm(UserCreationForm):
#
#
#     class Meta:
#         model = User
#         fields = ["username", "email"]
#         widgets = {
#             "username": TextInput(attrs={
#                 'style': 'width: 600px; height: 50px; margin: auto; border-radius: 20px; border: 0; text-align: center;',
#                 'class': 'form-control',
#                 'placeholder': 'Придумайте логин',
#         }),
#             "email": EmailInput(attrs={
#                 'style': 'width: 500px; height: 50px; margin: auto; border-radius: 20px; border: 1px solid  White; text-align: center;',
#                 'class': 'form-control',
#                 'placeholder': 'Введите свой e-mail',
#
#         })}


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

# class CartAddProductForm(forms.Form):
#     quantity = forms.TypedChoiceField(
#         choices=PRODUCT_QUANTITY_CHOICES,
#         coerce=int)
#     update = forms.BooleanField(required=False,
#                                 initial=False,
#                                 widget=forms.HiddenInput)

class TestimonialForm(ModelForm):
    class Meta:
        model = Testimonial
        fields = ["name", "image", "description"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите свое имя',
        }),
            "image": forms.FileInput(attrs={
                'class': 'form-control-file',
                'placeholder': 'выберите файл',
        }),

            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите свой отзыв',
        })}



