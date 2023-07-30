from django.shortcuts import render
from catalog.models import Category, Product
from django.views.generic import ListView, DetailView


# Create your views here.

# FBV подход
#def index(request):
    #'''контроллер главной страницы'''
    #context = {
       # 'object_list': Product.objects.all(),
       # 'title': 'Онлайн магазин',
       # 'title_text': 'Добро пожаловать! Выбираем нужную Вам категорию товаров.'
   # }
   # return render(request, 'catalog/index.html', context)


'''CBV подход'''
class MainListView(ListView):
    '''Контролер главной страницы. Отображает все товары без категорий'''
    model = Product
    template_name = 'catalog/index.html'
    extra_context = {
        'title': 'Онлайн магазин',
        'title_text': 'Добро пожаловать! Выбираем нужный товар.'
    }


# FBV подход
#def categories(request):
    #'''контроллер страницы всех категорий'''
    #context = {
     #   'object_list': Category.objects.all(),
      #  'title': 'Онлайн магазин',
     #   'title_text': 'Добро пожаловать! Выбираем нужную Вам категорию товаров.'

    #}
    #return render(request, 'catalog/categories.html', context)


'''CBV подход'''
class CategoriesListView(ListView):
    '''Контроллер страницы Категории'''
    model = Category
    template_name = 'catalog/categories.html'
    extra_context = {
        'title': 'Онлайн магазин',
        'title_text': 'Добро пожаловать! Выбираем нужную Вам категорию товаров.'
    }


# FBV подход
# def category_products(request, pk):
    #'''контроллер страницы всех товаров с категориями'''
    #category_item = Category.objects.get(pk=pk)
    #context = {
    #    'object_list': Product.objects.filter(category_id=pk),
    #    'title': f'Товары из {category_item.name}',
    #    'title_text': 'Добро пожаловать! Выбираем нужный Вам товар.'

    #}
    #return render(request, 'catalog/products.html', context)



'''CBV подход'''
class CategoryProductsListView(ListView):
    '''Контроллер страницы товаров в конкретной Категории'''
    model = Product
    template_name = 'catalog/products.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk,
        context_data['title'] = f'Товары из {category_item.name}',
        context_data['title_text'] = f'Добро пожаловать! Выбираем нужный Вам товар.'

        return context_data



# FBV подход
# def products(request):
   # '''контроллер страницы всех товаров без категорий'''
   # products_list = Product.objects.all()
   # context = {
    #    'object_list': products_list
   # }
   # return render(request, "catalog/products_all.html", context)


'''CBV подход'''
class ProductsListView(ListView):
    '''Контролер страницы Товары. Отображает все товары без категорий'''
    model = Product
    template_name = 'catalog/products_all.html'
    extra_context = {
        'title': 'Онлайн магазин',
        'title_text': 'Добро пожаловать! Ознакомьтесь с товарами.'
    }


# FBV подход
# def product_detailed(request, pk):
    #'''контроллер страницы одного товара'''
    #category_item = Product.objects.get(pk=pk)
    #context = {
    #    'object_list': Product.objects.filter(pk=pk),
    #    'title': f'Товар - {category_item.name}',
    #    'title_text': 'Добро пожаловать! Выбираем нужный Вам товар.',
    #    'name_card': category_item.name,
    #    'price': category_item.price,
    #    'description': category_item.description,
    #    'data_added': category_item.data_create,
    #    'data_edit': category_item.data_edit

    #}
    #return render(request, "catalog/product_detail.html", context)


'''CBV подход'''
class ProductDetailView(DetailView):
    '''Контроллер страницы одного товара'''
    model = Product
    template_name = 'catalog/product_detail.html'
    extra_context = {
        'title': 'Онлайн магазин',
        'title_text': 'Добро пожаловать! Ознакомьтесь с товаром.'
    }
