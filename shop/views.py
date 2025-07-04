from django.shortcuts import render
from .models import Category, Product, Order
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer 
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.core.mail import send_mail
from backend.settings import EMAIL_HOST_USER

# Create your views here.

class CategoryView(APIView):
    def get(self, request):
        try:
            categories = Category.objects.all()
            serializers = CategorySerializer(categories, many=True)
            
            return Response({
                "data": serializers.data,
                "message": "Categories retrieved successfully"
             }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "data": None,
                "message":"Something went wrong: "+ str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            
    def post(self, request):
        try:
            serializer = CategorySerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": serializer.data,
                    "message": "Category created successfully"
                }, status=status.HTTP_201_CREATED)

            return Response({
                "data": serializer.errors,
                "message": "Validation failed"
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                "data": None,
                "message":"Something went wrong: "+ str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    
    def patch(self, request, pk=None):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": serializer.data,
                    "message": "Category updated successfully"
                }, status=status.HTTP_200_OK)

            return Response({
                "data": serializer.errors,
                "message": "Validation failed"
            }, status=status.HTTP_400_BAD_REQUEST)

        except Category.DoesNotExist:
            return Response({
                "data": None,
                "message": "Category not found"
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                "data": None,
                "message":"Something went wrong: "+ str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    
    def delete(self, request, pk=None):
        try:
            category = Category.objects.get(pk=pk)
            category.delete()
            return Response({
                "data": None,
                "message": "Category deleted successfully"
            }, status=status.HTTP_204_NO_CONTENT)

        except Category.DoesNotExist:
            return Response({
                "data": None,
                "message": "Category not found"
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                "data": None,
                "message":"Something went wrong: "+ str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            
class ProductView(APIView):
    
    def get(self, request):
        try:
            products = Product.objects.all()
            serializers = ProductSerializer(products, many=True)
            
            return Response({
                "data": serializers.data,
                "message": "Products retrieved successfully"
             }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "data": None,
                "message":"Something went wrong: "+ str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            
    def post(self, request):
        try:
            serializer = ProductSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": serializer.data,
                    "message": "Product created successfully"
                }, status=status.HTTP_201_CREATED)

            return Response({
                "data": serializer.errors,
                "message": "Validation failed"
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                "data": None,
                "message":"Something went wrong: "+ str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            
    def patch(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": serializer.data,
                    "message": "Product updated successfully"
                }, status=status.HTTP_200_OK)

            return Response({
                "data": serializer.errors,
                "message": "Validation failed"
            }, status=status.HTTP_400_BAD_REQUEST)

        except Product.DoesNotExist:
            return Response({
                "data": None,
                "message": "Product not found"
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                "data": None,
                "message":"Something went wrong: "+ str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            
    def delete(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return Response({
                "data": None,
                "message": "Product deleted successfully"
            }, status=status.HTTP_204_NO_CONTENT)

        except Product.DoesNotExist:
            return Response({
                "data": None,
                "message": "Product not found"
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                "data": None,
                "message":"Something went wrong: "+ str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class OrderView(APIView):
    
    def get(self, request):
        try:
            orders = Order.objects.all()
            serializers = OrderSerializer(orders, many=True)
            
            return Response({
                "data": serializers.data,
                "message": "Orders retrieved successfully"
             }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "data": None,
                "message":"Something went wrong: "+ str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            
    def post(self, request):
        try:
            serializer = OrderSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                subject = 'Order Confirmation'
                message = "Dear Customer, "+ request.data['customer_name']+ " Your order is placed now. Thank you for your order!"
                recipient_email = request.data.get('customer_email')
                send_mail(subject, message, EMAIL_HOST_USER, [recipient_email], fail_silently=False)
                return Response({
                    "data": serializer.data,
                    "message": "Order created successfully"
                }, status=status.HTTP_201_CREATED)

            return Response({
                "data": serializer.errors,
                "message": "Validation failed"
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                "data": None,
                "message":"Something went wrong: "+ str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            
    def patch(self, request):
        try:
            order = Order.objects.get(pk=request.data.get('id'))
            serializer = OrderSerializer(order, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": serializer.data,
                    "message": "Order updated successfully"
                }, status=status.HTTP_200_OK)

            return Response({
                "data": serializer.errors,
                "message": "Validation failed"
            }, status=status.HTTP_400_BAD_REQUEST)

        except Order.DoesNotExist:
            return Response({
                "data": None,
                "message": "Order not found"
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                "data": None,
                "message":"Something went wrong: "+ str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    def delete(self, request, pk=None):
        try:
            order = Order.objects.get(pk=pk)
            order.delete()
            return Response({
                "data": {},
                "message": "Order deleted successfully"
            }, status=status.HTTP_204_NO_CONTENT)

        except Order.DoesNotExist:
            return Response({
                "data": None,
                "message": "Order not found"
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                "data": None,
                "message":"Something went wrong: "+ str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)