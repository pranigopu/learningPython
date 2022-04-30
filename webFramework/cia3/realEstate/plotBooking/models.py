from django.db import models

# Create your models here.
"""
-Customer Name
-Address
-Email
-Phone
-Desired SquareFeet
-Need of Loan
"""
class Customer(models.Model):
    custName = models.CharField(max_length = 50)
    address = models.TextField()
    email = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 10)
    desiredSquareFeet = models.FloatField()
    needOfLoan = models.BooleanField()