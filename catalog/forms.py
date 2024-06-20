from django import forms
from django.core.exceptions import ValidationError
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_description', 'imagery', 'category', 'cost_product']

    def clean_product_name(self):
        product_name = self.cleaned_data['product_name']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        if any(word in product_name.lower() for word in forbidden_words):
            raise ValidationError('Название продукта содержит запрещенные слова.')
        return product_name

    def clean_product_description(self):
        product_description = self.cleaned_data['product_description']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        if any(word in product_description.lower() for word in forbidden_words):
            raise ValidationError('Описание продукта содержит запрещенные слова.')
        return product_description
