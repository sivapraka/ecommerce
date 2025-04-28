from django.db import models


class AuditData(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #created_by = models.CharField(max_length=120)
    #updated_by = models.CharField(max_length=120)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


# Create your models here.
class Products(AuditData):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True,
                                 related_name='products')


class Orders(AuditData):
    # Many-to-Many with an intermediate model
    product = models.ManyToManyField(Products, through='OrderProduct', related_name='orders')
    quantity = models.PositiveIntegerField(null=False, default=1)
    total_price = models.DecimalField(decimal_places=2, max_digits=10000)
    order_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    orderid = models.CharField(max_length=120)

class OrderProduct(AuditData):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=False, default=1)

class Category(AuditData):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
