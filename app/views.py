from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Testimonial
from .models import Product, Cart

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart, created = Cart.objects.get_or_create(product=product)
    if not created:
        cart.quantity += 1
        cart.save()
    return redirect(request, 'add_to_cart.html')


def index(request, category_slug=None):
    category = None
    products = Product.objects.filter()
    testimonial = Testimonial.objects.filter()
    if category_slug:
        products = products.filter(category=category)
        testimonial = testimonial.filter(category=category)
    return  render(request, 'index.html',
                    {
                        'category': category,
                        'products': products,
                        'testimonial': testimonial
                    })


def detail(request, id, slug):
    product = get_object_or_404(request, id=id, slug=slug, available=True)
    return render(request, 'detail.html', {'product': product,})


def Menu(request, category_slug=None):
    category = None
    products = Product.objects.filter()
    testimonial = Testimonial.objects.filter()
    if category_slug:
        products = products.filter(category=category)
        testimonial = testimonial.filter(category=category)
    return  render(request, 'Menu.html',
                    {
                        'category': category,
                        'products': products,
                        'testimonial': testimonial
                    })

def About(request, category_slug=None):
    category = None
    products = Product.objects.filter()
    testimonial = Testimonial.objects.filter()
    if category_slug:
        products = products.filter(category=category)
        testimonial = testimonial.filter(category=category)
    return  render(request, 'about.html',
                    {
                        'category': category,
                        'products': products,
                        'testimonial': testimonial
                    })


def Cart(request):
    return render(request, 'cart.html')



def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/menu')
    else:
        form = forms.RegisterForm()

    return render(request, 'registration/register.html', {'form': form})

