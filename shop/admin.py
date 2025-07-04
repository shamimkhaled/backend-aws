from django.contrib import admin
from .models import Category, Product, Order

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'description', 'created_at', 'updated_at')
    # prepopulated_fields = {'slug': ('category_name',)}
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'description', 'price', 'stock', 'category', 'created_at', 'updated_at')
    list_filter = ('category',)
    search_fields = ('product_name', 'description')
    # prepopulated_fields = {'slug': ('product_name',)}
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'product', 'quantity', 'total_amount', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('customer_name', 'customer_email', 'product__product_name')
    # prepopulated_fields = {'slug': ('customer_name',)}
