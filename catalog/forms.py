from django import forms
from django.core.validators import ValidationError
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        self.validate_words(name)
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        self.validate_words(description)
        return description

    def validate_words(self, value):
        if not value:
            return
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in words:
            if word in value.lower():
                raise forms.ValidationError('Это слово запрещенное')
        return words

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите имя продукта'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание продукта'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите категорию продукта'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите стоимость продукта'
        })

