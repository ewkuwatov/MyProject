from django.shortcuts import render, redirect
from . import forms
from .models import *


def index(request):
    return  render(request, 'index.html')

def Menu(request):
    return  render(request, 'Menu.html')

def About(request):
    return  render(request, 'about.html')

def Cart(request):
    return  render(request, 'cart.html')


def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = forms.RegisterForm(request.POST)

    return render(request, 'registration/register.html', {'form': form})
