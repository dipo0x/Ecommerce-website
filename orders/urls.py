from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.order_create, name='order_create'),
    path('', views.webhook, name='webhook')
]