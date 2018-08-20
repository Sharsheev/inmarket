from django.urls import path
from django.conf.urls import url
from .views import base, category, product, cart, add_to_cart

app_name = 'shopocenter'

urlpatterns = [
    path('', base, name='base'),
    path('category/<category_slug>/', category, name='category'),
    path('product/<product_slug>/', product, name='product'),
    path('cart/', cart, name='cart'),
    path('add_to_cart/<product_slug>/', add_to_cart, name='add_to_cart'),
]