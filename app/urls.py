from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,),
    path('register', views.Register),
    path('menu', views.Menu, name='product_list'),
    path('about', views.About),
    path('cart', views.Cart, name='cart'),
    # path('product_list', views.product_list, name='product_list'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]