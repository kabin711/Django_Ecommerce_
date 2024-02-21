from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    slug = models.CharField(max_length = 50, null = True, blank= True)
    is_popular = models.BooleanField(default = False)
    image  = models.ImageField(upload_to='category', null=True)
    display_order = models.IntegerField(default = 1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length = 20, unique = True)
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    color_choices = (('Red', 'Red'),
                     ('Green', 'Green'), 
                     ('Others', 'Others'))
    size_choices = (('xl', 'xl'),
                     ('xxl', 'xxl'), 
                     ('Others', 'Others'))
    
    
    name = models.CharField(max_length = 40)
    category = models.ForeignKey(Category, related_name = "category_products", on_delete = models.CASCADE)
    price = models.IntegerField(default = 0)
    quantity = models.IntegerField(default = 0)
    image = models.ImageField(upload_to='product', blank=True, null=True)
    image2 = models.ImageField(upload_to='product', blank=True, null=True)
    image3 = models.ImageField(upload_to='product', blank=True, null=True)
    image4 = models.ImageField(upload_to='product', blank=True, null=True)
    color = models.CharField(max_length=40, choices = color_choices, default = 'Others')
    size = models.CharField(max_length=40, choices = size_choices, default = 0) 
    description = models.CharField(max_length = 400, null = True, blank= True)
    related_product = models.ManyToManyField('self', related_name='related_product', blank=True)
    brands = models.ForeignKey(Brand, related_name = 'product_brand', on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default = True)  
    is_featured = models.BooleanField(default = False)
    def __str__(self):
        return self.name
    
class Banner(models.Model):
    name = models.CharField(max_length = 20)
    image = models.ImageField(upload_to='banner', null=True, blank=True)
    def __str__(self):
        return self.name
