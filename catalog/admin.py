from django.contrib import admin
from .models import Category, Product

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Выводим id и name в списке категорий
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Выводим id, name, price и category в списке продуктов
    list_display = ('id', 'name', 'price', 'category')

    # Настраиваем фильтрацию продуктов по категории
    list_filter = ('category',)

    # Настраиваем поиск по полям name и description
    search_fields = ('name', 'description')