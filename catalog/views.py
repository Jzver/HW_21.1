from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .forms import ProductForm
from .models import Product, Version


# Список продуктов
class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for product in context['object_list']:
            try:
                current_version = Version.objects.filter(product=product, is_current_version=True).latest('id')
                product.current_version = current_version
            except Version.DoesNotExist:
                product.current_version = None
        return context


# Детали продукта
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


# Создание продукта
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')


# Обновление продукта
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')


# Удаление продукта
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product_list')


# Контакты
class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
