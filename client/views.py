from typing import Any
from django.shortcuts import render,get_object_or_404
from django.shortcuts import render, redirect
from accounts.models import User
from django.views.generic import TemplateView
from .models import Cart, CartItem
from catalogue.models import (Category,
                              Product,
                              Banner,Brand)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
# Create your views here.

class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['product'] = Product.objects.all()
        if self.request.user.is_authenticated:
            # cart = get_object_or_404(Cart, user = self.request.user)
            # context['cart'] = cart
            context['cart_count'] = Cart.get_Total_count(self.request.user)
            context['total'] = Cart.get_total(self.request.user)
            context['cart_item'] = CartItem.objects.filter(cart__user = self.request.user)
        else:
            context['cart_item'] = []
            context['cart_count'] = 0
        
        
        return context
        # return super().get_context_data(**kwargs)

class IndexView(BaseView):  
    template_name = 'client/index.html'
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['banner'] = Banner.objects.all()
        context['popular_category'] = Category.objects.filter(is_popular = True)
        context['is_featured'] = Product.objects.filter(is_featured= True)
        return self.render_to_response(context)
    
    
    

class ProductPageView(BaseView):
    template_name = 'client/index/productview.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        
        product_id = kwargs.get('product_id')
        context['product'] = get_object_or_404(Product, pk=product_id)
        return render(request, self.template_name, context)


class CategoryList(BaseView):
    template_name = 'client/index/categorylist.html'
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['category_brand'] = Brand.objects.filter(product_brand__category__slug = kwargs.get('slug')).distinct()
        sort_by = request.GET.get('sortby')
        brand_list = request.GET.getlist('brands')
        context['brand_list'] = brand_list
        context['sort_by'] = sort_by
        if sort_by:
            sort_by = '-'+sort_by
            product = Product.objects.filter(category__slug = kwargs.get('slug')).order_by(sort_by)
            if not len(brand_list) == 0:
                product = product.filter(brands_id__in = brand_list)
            # context['product'] = product
        else:
            product = Product.objects.filter(category__slug = kwargs.get('slug'))
            if not len(brand_list) == 0:
                product = product.filter(brands_id__in = brand_list) 
        paginator = Paginator(product, 2)
        try:
           page = request.GET.get('page')
           product = paginator.get_page(page)
        except PageNotAnInteger:
           product = paginator.get_page(1)
        except EmptyPage:
           product = paginator.get_page(paginator.num_pages)
        context['product'] = product
        return render(request, self.template_name, context)

@login_required(login_url = '/accounts/login')
def AddToCart(request, product_id):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        try: 
            cart = Cart.objects.get(user = request.user)
        except:
            cart = Cart.objects.create(user = request.user)
            print(cart)
    
        product = get_object_or_404(Product, id = product_id)

        if CartItem.objects.filter(cart = cart, product_id = product_id).exists():
            item = CartItem.objects.get(cart = cart, product_id = product_id)
            quantity = item.quantity + int(quantity)
            item.quantity = quantity
            item.save()
        
        else:
            item = CartItem.objects.create(cart = cart,
                product = product, quantity = quantity)
    
    category_slug = item.product.category.slug
    return redirect('clients:categorylist', slug = category_slug)

def view_cart(request):
    # Retrieve cart items for the current user
    user_cart_items = CartItem.objects.filter(cart__user=request.user)

    # Calculate total and other necessary information if needed
    total_items = user_cart_items.count()
    total_amount = 0
    for cart_item in user_cart_items:  
        cart_item.total_cost = cart_item.quantity * cart_item.product.price
        total_amount += cart_item.total_cost
    context = {
        'cart_items': user_cart_items,
        'total_items': total_items,
        'total_amount': total_amount,
    }

    return render(request, 'client/index/viewcart.html', context)

def Remove_From_Cart(request, item_id):
    item = CartItem.objects.get(id=item_id)
    item.delete()
    return redirect('clients:view_cart')