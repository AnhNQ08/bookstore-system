from abc import ABC, abstractmethod

class CustomerRepository(ABC):

    @abstractmethod
    def create(self, customer):
        pass

    @abstractmethod
    def find_by_email(self, email):
        pass
