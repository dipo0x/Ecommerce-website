from django.conf.urls import url
from . import views

app_name = 'shop'

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^45/(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]
