from django.shortcuts import render
from mainapp.models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    content = {
        'title': 'geekShop - главная',
        'title_text': 'geekshop главная',
    }
    return render(request, 'mainapp/index.html', content)


def products(request, category_id=None, page=1):
    context = {
        'title': 'geekshop - продукты',
        'title_text': 'geekshop меню',
        'categories': ProductCategory.objects.all(),
    }
    if category_id:
        products = Product.objects.filter(category_id=category_id).order_by('price')
    else:
        products = Product.objects.all()
    paginator = Paginator(products, 2)


    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context.update({'products': products_paginator})
    # products = content['products']
    return render(request, 'mainapp/products.html', context)
