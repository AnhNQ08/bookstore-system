from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer

@api_view(['POST'])
def register(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    customer = Customer.objects.filter(
        email=email, password=password
    ).first()

    if not customer:
        return Response({"error": "Invalid credentials"}, status=400)

    return Response({
        "id": customer.id,
        "name": customer.name,
        "email": customer.email
    })
