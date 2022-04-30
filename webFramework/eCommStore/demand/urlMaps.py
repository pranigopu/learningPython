from django.urls import path
from .views import *

urlpatterns = [
    path("customer/enter", customer_entry),
    path("customer/remove", customer_removal),
    path("product", product_data),
    path("product/enter", product_entry),
    path("product/remove", product_removal)
]