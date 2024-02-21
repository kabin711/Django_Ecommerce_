from typing import Any
from django.forms import ModelForm
from catalogue.models import Category, Product
from django.core.exceptions import ValidationError

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'slug', 'display_order')
    

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'price', 'quantity', 'image','description', 'is_active', 'is_featured')
    
    # def clean(self):
    #     data = super().clean()
    #     name = data.get('name')
        
    #     if Product.objects.filter(name = name).exists():
    #         raise ValidationError('Name Already exists')
    #     return data