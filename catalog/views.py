from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView
from django import forms
from .models import Product

# Create your views here.
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products')

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name ='products'

class ProductTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

class ProductDeleteView(DetailView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:products')