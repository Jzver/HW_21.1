from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from catalog.models import Product


# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)
        return super().get(request, *args, **kwargs)