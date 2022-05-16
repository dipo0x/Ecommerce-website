from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('contact/', views.contact, name='contact'),
    path('45/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
]
