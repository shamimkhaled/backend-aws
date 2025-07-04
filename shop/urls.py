from django.urls import path, include
from .views import CategoryView, ProductView, OrderView

# API URL patterns for the shop application
urlpatterns = [
    path('categories/', CategoryView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryView.as_view(), name='category-detail'),

    path('products/', ProductView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductView.as_view(), name='product-detail'),

    path('orders/', OrderView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderView.as_view(), name='order-detail'),
]
