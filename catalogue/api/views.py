from rest_framework import serializers
from catalogue.models import Product
from .serializers import ProductSerializer
from rest_framework.generics import ListCreateAPIView

class ProductCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
