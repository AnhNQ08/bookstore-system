from django.urls import path
from .views import register, login, get_customer

urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('<int:customer_id>/', get_customer),
]
