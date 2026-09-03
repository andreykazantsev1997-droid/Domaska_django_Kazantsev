from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView

from .models import Product

# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name ='products'

class ProductTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/products.html'
    context_object_name = 'product'