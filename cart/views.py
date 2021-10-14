from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_slug):
    cart = Cart(request)  # create a new cart object passing it the request object 
    product = get_object_or_404(Product, slug=product_slug) 
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], slug=product_slug, update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=product_slug)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})
