from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'cart'

urlpatterns = [
    url(r'^$', views.cart_detail, name='cart_detail'),
    path('remove/<product_slug>/', views.cart_remove, name='cart_remove'),
    path('add/<product_slug>', views.cart_add, name='cart_add')
]

