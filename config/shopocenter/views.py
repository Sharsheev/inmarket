from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Category, Brand, Product, CartItem, Cart


def base(request):
    cart = Cart.objects.all()
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
        'cart': cart,
    }
    return render(request, 'base.html', context)


def category(request, category_slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=category_slug)
    products_of_category = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products_of_category': products_of_category,
        'categories': categories,
    }
    return render(request, 'category.html', context)


def product(request, product_slug):
    cart = Cart.objects.all()
    categories = Category.objects.all()
    product = Product.objects.get(slug=product_slug)
    context = {
        'product': product,
        'categories': categories,
        'cart': cart,
    }
    return render(request, 'product.html', context)

def cart(request):
    cart = Cart.objects.all()
    context = {
        'cart': cart,
    }
    return render(request, 'cart.html', context)

# def items(self):
#     items = Cart.objects.first()
#     return self.items

def add_to_cart(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    new_item = CartItem.objects.get_or_create(product=product, item_total=product.price)
    cart = Cart.objects.all()
    if new_item not in cart:
        b = cart.objects.add(new_item)
        s = b.save()
        return HttpResponseRedirect('/cart/')
