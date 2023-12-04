from django.shortcuts import render, redirect
from .models import Product, Cart, CartItem


def store_view(request):
    item_objects = Product.objects.all()
    context = {'item_objects': item_objects}
    return render(request, 'store.html', context)

def cart_view(request):
   cart_items = CartItem.objects.filter(cart__user=request.user)
   context = {'cart_items': cart_items}
   return render(request, 'cart.html', context)

def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
       
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
       
    return redirect('store:store')


def increase_cart_item(request, product_id):
   product = Product.objects.get(pk=product_id)
   cart = request.user.cart
   cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
   cart_item.quantity += 1
   cart_item.save()
   return redirect('store:cart')


def decrease_cart_item(request, product_id):
   product = Product.objects.get(pk=product_id)
   cart = request.user.cart
   cart_item = cart.cartitem_set.get(product=product)
   if cart_item.quantity > 1:
       cart_item.quantity -= 1
       cart_item.save()
   else:
       cart_item.delete()
   return redirect('store:cart')
