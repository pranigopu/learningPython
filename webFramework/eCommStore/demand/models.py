from django.db import models

# Create your models here.

# INITIAL MODELS (NOT SUBJECT TO MUCH MODIFICATION)
class Product(models.Model):
    pid = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 30, unique = True)
    description = models.TextField()
class Customer(models.Model):
    cuid = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 100, unique = True)
    phone = models.PositiveIntegerField(null = True)
    address = models.TextField()

# TRANSACTION-ORIENTED MODELS (SUBJECT TO CONSTANT UPDATION)
class Order(models.Model):
    oid = models.AutoField(primary_key = True)
    placementTime = models.DateTimeField()
    instructions = models.TextField()
class ProductOrder(models.Model):
    oid = models.ForeignKey(Order, on_delete = models.CASCADE)
    pid = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.FloatField()
class CustomerOrder(models.Model):
    oid = models.ForeignKey(Order, on_delete = models.CASCADE)
    cuid = models.ForeignKey(Customer, on_delete = models.CASCADE)