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
        'object_list': Category.objects.all()[:2],
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
    '''контроллер страницы всех товаров'''
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Товары из {category_item.name}',
        'title_text': 'Добро пожаловать! Выбираем нужный Вам товар.'

    }
    return render(request, 'catalog/products.html', context)
