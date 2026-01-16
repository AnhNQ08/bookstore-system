from domain.entities.cart_item import CartItem


class Cart:
    def __init__(self, id, customer_id):
        self.id = id
        self.customer_id = customer_id
        self.items = []

    def add_item(self, book, quantity):
        self.items.append(CartItem(book, quantity))
