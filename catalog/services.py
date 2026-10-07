from catalog.models import Product
from django.core.cache import cache


def get_products_by_category(category_id):

    return Product.objects.filter(category_id=category_id)

def get_cached_products():
    products = cache.get('product_list')
    if products is None:
        products = Product.objects.all()
        cache.set('product_list', products, 900)
    return products
