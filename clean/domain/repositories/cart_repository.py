from abc import ABC, abstractmethod

class CartRepository(ABC):

    @abstractmethod
    def get_cart_by_customer(self, customer_id):
        pass

    @abstractmethod
    def add_item(self, cart_item):
        pass

    @abstractmethod
    def get_items(self, cart_id):
        pass
