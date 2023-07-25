from django import forms
from django.forms import TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "password", "password2"]
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'password': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'password2': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            })
        }
