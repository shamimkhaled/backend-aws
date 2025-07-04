from django.db import models

# Create your models here.

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
class Category(TimestampedModel):
    category_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.category_name

class Product(TimestampedModel):
    product_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to='products/', blank=True, null=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.product_name
    

class Order(TimestampedModel):
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    product = models.ForeignKey(Product, related_name='orders', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"Order #{self.id} by {self.customer_name}"
    
    