from django.urls import path

from .apps import CatalogConfig
from .views import index, categories, category_products, products, product_detailed

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('<int:pk>/products/', category_products, name='category_products'),
    path('productsall/', products, name='products'),
    path('<int:pk>/product/', product_detailed, name='product_detailed'),

]
