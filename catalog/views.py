from django.shortcuts import render
from catalog.models import Category, Product


# Create your views here.
# def home(request):
    # return render(request, 'catalog/home.html')


# def contacts(request):
    # if request.method == 'POST':
       # print(request.POST.get('name'))
       # print(request.POST.get('phone'))
       # print(request.POST.get('message'))
    # return render(request, 'catalog/contacts.html')


def index(request):
    '''контроллер главной страницы'''
    context = {
        'object_list': Product.objects.all(),
        'title': 'Онлайн магазин',
        'title_text': 'Добро пожаловать! Выбираем нужную Вам категорию товаров.'
    }
    return render(request, 'catalog/index.html', context)


def categories(request):
    '''контроллер страницы всех категорий'''
    context = {
        'object_list': Category.objects.all(),
        'title': 'Онлайн магазин',
        'title_text': 'Добро пожаловать! Выбираем нужную Вам категорию товаров.'

    }
    return render(request, 'catalog/categories.html', context)

def category_products(request, pk):
    '''контроллер страницы всех товаров с категориями'''
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Товары из {category_item.name}',
        'title_text': 'Добро пожаловать! Выбираем нужный Вам товар.'

    }
    return render(request, 'catalog/products.html', context)


def products(request):
    '''контроллер страницы всех товаров без категорий'''
    products_list = Product.objects.all()
    context = {
        'object_list': products_list
    }
    return render(request, "catalog/products_all.html", context)


def product_detailed(request, pk):
    '''контроллер страницы одного товара'''
    category_item = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(pk=pk),
        'title': f'Товар - {category_item.name}',
        'title_text': 'Добро пожаловать! Выбираем нужный Вам товар.',
        'name_card': category_item.name,
        'price': category_item.price,
        'description': category_item.description,
        'data_added': category_item.data_create,
        'data_edit': category_item.data_edit

    }
    return render(request, "catalog/product_detail.html", context)



