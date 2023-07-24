from django.urls import path

from .apps import CatalogConfig
from .views import index, categories, category_products

app_name = CatalogConfig.name

urlpatterns = [
    # path('', home, name='home'),
    # path('contacts/', contacts, name='contacts'),
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('<int:pk>/products/', category_products, name='category_products'),
]
