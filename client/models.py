from django.db import models
from accounts.models import User
from catalogue.models import Product

class Cart(models.Model):
    user = models.OneToOneField(User, related_name = 'cart_user', on_delete = models.CASCADE )
    
    @classmethod
    def get_Total_count(cls, user):
        count = 0
        for i in CartItem.objects.filter(cart__user = user):
            count += i.quantity
        return count

    @classmethod
    def get_total(cls, user):
        total = 0
        for i in CartItem.objects.filter(cart__user = user):
            total += i.quantity * i.product.price
        return total
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name = 'cart_item', on_delete = models.CASCADE)
    product = models.ForeignKey(Product, related_name = 'cart_product', on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 0)
    
# class Order(models.Model):
#     user = models.OneToOneField(User, related_name = 'user_order', on_delete = models.CASCADE )