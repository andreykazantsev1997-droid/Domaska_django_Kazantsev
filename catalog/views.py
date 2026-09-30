from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, DeleteView
from .forms import ProductForm
from .models import Product

# Create your views here.
class UnpublishProductView(LoginRequiredMixin, UpdateView):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden('У вас нет права для отмены публикации продукта')

        product.status_publication = False
        product.save()

        return redirect('catalog:product_detail', pk=pk)

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products')

class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    permission_required = 'catalog.change_product'
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

class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:products')