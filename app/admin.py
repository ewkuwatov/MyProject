from django.contrib import admin
from .models import Product, Testimonial
# Register your models here.


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_filter = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_filter = ['name']


