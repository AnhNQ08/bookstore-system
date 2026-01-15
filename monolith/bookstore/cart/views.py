from django.shortcuts import render, redirect
from .models import Cart, CartItem
from books.models import Book

def cart_detail(request):
    cart = Cart.objects.first()
    items = cart.items.all() if cart else []
    return render(request, 'cart/cart_detail.html', {'items': items})

def add_to_cart(request, book_id):
    book = Book.objects.get(id=book_id)
    cart, _ = Cart.objects.get_or_create(customer_id=1)

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        book=book,
        defaults={'quantity': 1}
    )

    if not created:
        item.quantity += 1
        item.save()

    return redirect('/cart/')
