from django.shortcuts import render
from .models import CartItem

def cart_detail(request):
    items = CartItem.objects.all()
    return render(request, 'cart/cart_detail.html', {'items': items})
