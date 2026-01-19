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

    # 1. Validate input
    if not customer_id or not book_id or not quantity:
        return Response(
            {"error": "customer_id, book_id, quantity are required"},
            status=400
        )

    if int(quantity) <= 0:
        return Response(
            {"error": "Quantity must be greater than 0"},
            status=400
        )

    # 2. Check customer via customer-service
    customer_response = requests.get(f"{CUSTOMER_SERVICE}{customer_id}/")
    if customer_response.status_code != 200:
        return Response(
            {"error": "Customer not found"},
            status=400
        )

    # 3. Check book via book-service
    book_response = requests.get(f"{BOOK_SERVICE}{book_id}/")
    if book_response.status_code != 200:
        return Response(
            {"error": "Book not found"},
            status=400
        )

    # 4. Get or create cart
    cart, _ = Cart.objects.get_or_create(customer_id=customer_id)

    # 5. Add or update cart item
    item, created = CartItem.objects.get_or_create(
        cart=cart,
        book_id=book_id,
        defaults={'quantity': int(quantity)}
    )

    if not created:
        item.quantity += int(quantity)
        item.save()

    return Response(
        {"message": "Added to cart successfully"},
        status=201
    )

@api_view(['GET'])
def view_cart(request, customer_id):
    try:
        cart = Cart.objects.get(customer_id=customer_id)
    except Cart.DoesNotExist:
        return Response(
            {"message": "Cart is empty"},
            status=200
        )

    items = CartItem.objects.filter(cart=cart)
    cart_items = []
    total_price = 0

    for item in items:
        # Call book-service to get book info
        book_response = requests.get(f"{BOOK_SERVICE}{item.book_id}/")

        if book_response.status_code == 200:
            book_data = book_response.json()
            price = float(book_data.get("price", 0))
            title = book_data.get("title", "")
        else:
            price = 0
            title = "Unknown"

        item_total = price * item.quantity
        total_price += item_total

        cart_items.append({
            "book_id": item.book_id,
            "title": title,
            "price": price,
            "quantity": item.quantity,
            "total": item_total
        })

    return Response({
        "customer_id": customer_id,
        "items": cart_items,
        "grand_total": total_price
    })
