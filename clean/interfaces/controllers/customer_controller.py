from django.http import JsonResponse
from usecases.customer.register_customer import RegisterCustomerUseCase
from infrastructure.repositories.customer_repository_impl import DjangoCustomerRepository

def register(request):
    usecase = RegisterCustomerUseCase(DjangoCustomerRepository())
    c = usecase.execute(
        request.POST["name"],
        request.POST["email"],
        request.POST["password"]
    )
    return JsonResponse({"id": c.id})
