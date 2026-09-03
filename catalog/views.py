from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    product = Product.objects.all()
    context = {"products": product}
    return render(request, 'catalog/home.html', context)

def contacts(request):
    return render(request, 'catalog/contacts.html')

def products(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {"product": product}
    return render(request, 'catalog/products.html', context)