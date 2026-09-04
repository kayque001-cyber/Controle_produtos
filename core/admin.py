from django.contrib import admin
from .models import Brand, category, Product

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('is_active', 'name', 'description')
    search_fields = ('name', 'description')
    list_filter = ('is_active',)



@admin.register(category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'description')
    search_fields = ('name', 'description')
    list_filter = ('is_active',)




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'category', 'is_active', 'description', 'price')
    search_fields = ('title', 'description')
    list_filter = ('is_active', 'brand', 'category')