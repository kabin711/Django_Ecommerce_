from .views import *
from django.urls import path

app_name = 'clients'

urlpatterns = [
   path('', IndexView.as_view(), name = 'index'),
   path('product/<int:product_id>/', ProductPageView.as_view(), name='productview'),
   path('categorylist/<str:slug>/', CategoryList.as_view(), name='categorylist'),
   path('AddtoCart/<int:product_id>/', AddToCart, name='addtocart'),
   path('viewcart/', view_cart, name='view_cart'),
   path('remove_from_cart/<int:item_id>/', Remove_From_Cart, name='remove_cart'),
   
   
   
]