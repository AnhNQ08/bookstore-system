from django.http import JsonResponse
from usecases.cart.add_to_cart import AddToCartUseCase
from infrastructure.repositories.cart_repository_impl import DjangoCartRepository
from infrastructure.repositories.book_repository_impl import DjangoBookRepository

def add_to_cart(request):
    usecase = AddToCartUseCase(
        DjangoCartRepository(),
        DjangoBookRepository()
    )
    usecase.execute(
        int(request.POST["customer_id"]),
        int(request.POST["book_id"]),
        int(request.POST["quantity"])
    )
    return JsonResponse({"status": "ok"})
