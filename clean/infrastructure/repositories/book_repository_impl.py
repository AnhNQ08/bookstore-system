from framework.bookstore.models import BookModel
from domain.entities.book import Book

class DjangoBookRepository:
    def get_all(self):
        return [
            Book(b.id, b.title, b.author, b.price, b.stock)
            for b in BookModel.objects.all()
        ]

    def get_by_id(self, book_id):
        b = BookModel.objects.get(id=book_id)
        return Book(b.id, b.title, b.author, b.price, b.stock)
