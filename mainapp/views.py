from django.shortcuts import render


# Create your views here.

def index(request):
    title_text_index = {
        'title': 'geekShop - главная',
        'title_text': 'geekshop главная'
    }
    return render(request, 'mainapp/index.html', title_text_index)


def products(request):
    title_text_products = {
        'title': 'geekshop - продукты',
        'title_text': 'geekshop меню',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00',
             'short_desc': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
             'image': 'Adidas hoodie.png'},
            {'name': 'Синяя куртка The North Face', 'price': '23 725,00',
             'short_desc': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
             'image': 'Blue jacket The North Face.png'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00',
             'short_desc': 'Материал с плюшевой текстурой. Удобный и мягкий.',
             'image': 'Brown sports oversized-top ASOS DESIGN.png'},
            {'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00',
             'short_desc': 'Плотная ткань. Легкий материал.', 'image': 'Black Nike Heritage backpack.png'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13 590,00',
             'short_desc': 'Гладкий кожаный верх. Натуральный материал.', 'image': 'Black Dr Martens shoes.png'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': '2 890,00',
             'short_desc': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
             'image': 'Dark blue wide-leg ASOs DESIGN trousers.png'},

        ]
    }
    products = title_text_products['products']
    return render(request, 'mainapp/products.html', title_text_products)


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
