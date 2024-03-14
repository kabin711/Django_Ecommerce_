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
    
class Order(models.Model):
    PENDING = 'Pending'
    PROCESSING = 'Processing'
    DELIVERED = 'Delivered'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (PROCESSING, 'Processing'),
        (DELIVERED, 'Delivered'),
    ]
    user = models.OneToOneField(User, related_name = 'user_order', on_delete = models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(max_digits=15, decimal_places = 2, default = 0.0)
    status = models.CharField(max_length=20, choices = STATUS_CHOICES, default = PENDING)
    
    def calculate_total(self):
        total = 0
        for item in self.order_items.all():
            total += item.calculate_subtotal()
            self.total_price = total
            self.save()
        
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_products', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def calculate_subtotal(self):
        return self.quantity * self.product.price