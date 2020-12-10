from django.shortcuts import render
from mainapp.models import Product, ProductCategory

# Create your views here.

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









def test_context(request):
    context = {
        'title': 'добро пожаловать!',
        'username': 'Denis Ershov',
        'products': [
            {'name': 'Черные худи', 'price': '2990 руб'},
            {'name': 'Джинсы', 'price': '5990 руб'},
        ],
        'promotion_products': [
            {'name': 'Туфли', 'price': '1990 руб'},
        ],
    }
    products = context['products']

    return render(request, 'mainapp/context.html', context)
