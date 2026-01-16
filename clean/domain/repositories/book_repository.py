from abc import ABC, abstractmethod

class BookRepository(ABC):

    @abstractmethod
    def list_all(self):
        pass

    @abstractmethod
    def find_by_id(self, book_id):
        pass
