from django.contrib import admin
from .models import Category, Product, Banner,Brand

# Register your models here.

admin.site.site_title = "Ecommerce site"
admin.site.name = "Ecommerce by kabin"

admin.site.register([Product])


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'display_order',)
    search_fields = ('name',)
    # ordering = ('name',) 
    list_display_links = ('slug',)
    list_editable = ('name',)
    # list_per_page = (2)
    
admin.site.register(Category, CategoryAdmin)
admin.site.register([Banner])
admin.site.register([Brand])

    