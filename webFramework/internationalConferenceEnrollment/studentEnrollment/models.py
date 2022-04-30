from django.db import models

# Create your models here.
class Student(models.Model):
    regno = models.CharField(max_length = 7, primary_key = True)
    name = models.CharField(max_length = 30)
    department = models.CharField(max_length = 30)
    semester = models.IntegerField()
    email = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 10)