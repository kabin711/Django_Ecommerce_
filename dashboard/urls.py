# from .views import mainDashboard
from .views import *
from django.urls import path

app_name = 'dashboard'

urlpatterns = [
    path('', mainDashboard, name='main-dashboard'),
    path('category-create/', createCategory,  name = 'category-create'),
    path('category-update/<int:pk>/', updateCategory, name = "category-update"),
    path('category-list/', listCategory, name = 'category-list'),
    path('product-list/', ProductList.as_view(), name = 'product-list' ),
    path('product-create/', ProductCreate.as_view(), name = 'product-create'),
    path('product-update/<int:pk>/', ProductUpdate.as_view(), name = "product-update"),
    path('product-delete/<int:pk>/', ProductDelete.as_view(), name = "product-delete"),
]