from django.urls import path
from django.contrib import admin
from interfaces.controllers.customer_controller import register
from interfaces.controllers.book_controller import list_books
from interfaces.controllers.cart_controller import add_to_cart

urlpatterns = [
    path("admin/", admin.site.urls),
    path('register/', register),
    path('books/', list_books),
    path('add-to-cart/', add_to_cart),
]
