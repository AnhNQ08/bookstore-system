import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cart, CartItem

CUSTOMER_SERVICE = "http://localhost:8000/api/customers/"
BOOK_SERVICE = "http://localhost:8001/api/books/"

@api_view(['POST'])
def add_to_cart(request):
    customer_id = request.data.get('customer_id')
    book_id = request.data.get('book_id')
    quantity = request.data.get('quantity')

    # check customer
    r1 = requests.get(f"{CUSTOMER_SERVICE}{customer_id}/")
    if r1.status_code != 200:
        return Response({"error": "Customer not found"}, status=400)

    # check book
    r2 = requests.get(f"{BOOK_SERVICE}{book_id}/")
    if r2.status_code != 200:
        return Response({"error": "Book not found"}, status=400)

    cart, _ = Cart.objects.get_or_create(customer_id=customer_id)
    CartItem.objects.create(cart=cart, book_id=book_id, quantity=quantity)

    return Response({"message": "Added to cart"})
