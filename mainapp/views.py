from django.shortcuts import render
from mainapp.models import Product, ProductCategory


def index(request):
    title_text_index = {
        'title': 'geekShop - главная',
        'title_text': 'geekshop главная',
    }

    return render(request, 'mainapp/index.html', title_text_index)


def products(request, pk=None):
    print(pk)
    title_text_products = {
        'title': 'geekshop - продукты',
        'title_text': 'geekshop меню',

        'products': Product.objects.all(),

    }
    products = title_text_products['products']
    return render(request, 'mainapp/products.html', context=title_text_products)
