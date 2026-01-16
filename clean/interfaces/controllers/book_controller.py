from django.http import JsonResponse
from usecases.book.list_books import ListBooksUseCase
from infrastructure.repositories.book_repository_impl import DjangoBookRepository

def list_books(request):
    usecase = ListBooksUseCase(DjangoBookRepository())
    books = usecase.execute()

    return JsonResponse([
        {
            "id": b.id,
            "title": b.title,
            "author": b.author,
            "price": float(b.price),
            "stock": b.stock
        } for b in books
    ], safe=False)
