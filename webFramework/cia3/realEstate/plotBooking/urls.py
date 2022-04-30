from django.urls import path
from .views import *
urlpatterns = [
     path('customerentry/', create_customer)
]