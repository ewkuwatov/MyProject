from django import forms
from django.forms import TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

# class CartAddProductForm(forms.Form):
#     quantity = forms.TypedChoiceField(
#         choices=PRODUCT_QUANTITY_CHOICES,
#         coerce=int)
#     update = forms.BooleanField(required=False,
#                                 initial=False,
#                                 widget=forms.HiddenInput)

