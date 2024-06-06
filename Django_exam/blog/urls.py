from django.contrib import admin
from django.urls import path
from blog.views import index, product_detail, customers, customer_detail, add_customer, edit_customer, delete_customer

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>/', product_detail, name='product_detail'),
    path('customers/', customers, name='customers'), 
    path('customer_detail/<int:pk>/', customer_detail, name='customer_detail'),
    path('add_customer/', add_customer, name='add_customer'),
    path('edit_customer/<int:pk>/', edit_customer, name='edit_customer'),  
    path('customers/<int:pk>/', delete_customer, name='delete_customer'), 
]

