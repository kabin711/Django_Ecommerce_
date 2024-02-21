from django.shortcuts import render
from .forms import CategoryForm, ProductForm
from django.shortcuts import redirect, get_object_or_404
from catalogue.models import Category, Product


from django.views.generic import ListView, CreateView, UpdateView,  DeleteView
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.


@user_passes_test(lambda u:u.is_staff)
def mainDashboard(request):
    if request.method == "GET":
        return render(request, 'custom_dashboard/base.html')

@user_passes_test(lambda u:u.is_staff)
def createCategory(request):
    if request.method == "GET":
        form = CategoryForm()
        return render(request, 'custom_dashboard/category/category_create.html',  {"form":form})
    
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("dashboard:category-list")
            # return render(request, 'dashboard/category/create-category', {"form":form})
        return render(request, 'custom_dashboard/category/category_create.html', {"form":form})
        

@user_passes_test(lambda u:u.is_staff)
def listCategory(request):
    if  request.method == "GET":
        category = Category.objects.all()
        return render(request, "custom_dashboard/category/category-list.html", {"category":category})
    
@user_passes_test(lambda u:u.is_staff)
def updateCategory(request, pk):
    category = get_object_or_404(Category, id = pk)
    if request.method == "GET":
        form = CategoryForm(instance=category)
        return render(request, "custom_dashboard/category/category-update.html",{"pk":pk, 'form':form})
    if request.method == "POST":
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save(commit=True)
            return redirect("dashboard:category-list")
        return render(request, "custom_dashboard/category/category-update.html", {"pk":pk, "form":form})
    


from django.contrib.auth.mixins import UserPassesTestMixin

class ProductList(UserPassesTestMixin, ListView):
    model = Product
    template_name = 'custom_dashboard/product/product_list.html'
    context_object_name = 'products'
    

    def test_func(self):
        return self.request.user.is_staff
    
    
    
    
    # def get_queryset(self):
    #     """
    #     Return the list of items for this view.
    #     The return value must be an iterable and may be an instance of
    #     `QuerySet` in which case `QuerySet` specific behavior will be enabled.
    #     """
    #     return Product.objects.filter(is_active = True)

from django.urls import reverse_lazy

class ProductCreate(CreateView):
    form_class = ProductForm
    template_name = 'custom_dashboard/product/create_product.html'
    success_url = reverse_lazy('dashboard:product-list')
    

class ProductUpdate(UpdateView):
    context_object_name = 'product'
    model = Product
    form_class = ProductForm
    template_name = 'custom_dashboard/product/product_update.html'
    success_url = reverse_lazy('dashboard:product-list')
    
class ProductDelete(DeleteView):
    context_object_name = 'product'
    model = Product
    form_class = ProductForm
    template_name = 'custom_dashboard/product/product_delete.html'