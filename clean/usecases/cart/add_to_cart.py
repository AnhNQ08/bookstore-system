class AddToCartUseCase:
    def __init__(self, cart_repo, book_repo):
        self.cart_repo = cart_repo
        self.book_repo = book_repo

    def execute(self, customer_id, book_id, quantity):
        cart = self.cart_repo.get_or_create(customer_id)
        book = self.book_repo.get_by_id(book_id)
        cart.add_item(book, quantity)
        self.cart_repo.save(cart)
