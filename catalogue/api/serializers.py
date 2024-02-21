from rest_framework import serializers
from catalogue.models import Product 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name')