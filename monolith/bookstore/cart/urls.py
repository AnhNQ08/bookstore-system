from django.urls import path
from .views import cart_detail, add_to_cart

urlpatterns = [
    path('', cart_detail, name='cart'),
    path('add/<int:book_id>/', add_to_cart),
]
