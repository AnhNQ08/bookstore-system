from framework.bookstore.models import CartModel, CartItemModel
from domain.entities.cart import Cart
from domain.entities.cart_item import CartItem

class DjangoCartRepository:

    def get_or_create(self, customer_id):
        cart_model, _ = CartModel.objects.get_or_create(
            customer_id=customer_id
        )
        cart = Cart(cart_model.id, cart_model.customer_id)

        for item in CartItemModel.objects.filter(cart=cart_model):
            cart.items.append(
                CartItem(item.book, item.quantity)
            )

        return cart

    def save(self, cart):
        cart_model = CartModel.objects.get(id=cart.id)
        CartItemModel.objects.filter(cart=cart_model).delete()

        for item in cart.items:
            CartItemModel.objects.create(
                cart=cart_model,
                book_id=item.book.id,
                quantity=item.quantity
            )

    def get_by_customer(self, customer_id):
        cart_model = CartModel.objects.get(customer_id=customer_id)
        cart = Cart(cart_model.id, customer_id)

        for item in CartItemModel.objects.filter(cart=cart_model):
            cart.items.append(
                CartItem(item.book, item.quantity)
            )
        return cart
