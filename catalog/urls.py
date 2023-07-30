from django.urls import path

from .apps import CatalogConfig
from .views import MainListView, ProductsListView, CategoriesListView, CategoryProductsListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    #FBV path('', index, name='index'),
    path('', MainListView.as_view(), name='index'),
    #FBV path('categories/', categories, name='categories'),
    path('categories/', CategoriesListView.as_view(), name='categories'),
    #FBV path('<int:pk>/products/', category_products, name='category_products'),
    path('<int:pk>/products/', CategoryProductsListView.as_view(), name='category_products'),
    #FBV path('productsall/', products, name='products'),
    path('productsall/', ProductsListView.as_view(), name='products'),
    #FBV path('<int:pk>/product/', product_detailed, name='product_detailed'),
    path('<int:pk>/product/', ProductDetailView.as_view(), name='product_detailed'),

]
