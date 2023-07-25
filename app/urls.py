from django.urls import path
from . import views

urlpatterns = [
    # path('login', views.Login),
    path('', views.index),
    path('menu', views.Menu),
    path('about', views.About),
    path('cart', views.Cart),
]