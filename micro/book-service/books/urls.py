from django.urls import path
from .views import list_books
from .views import get_book

urlpatterns = [
    path('', list_books),
    path('<int:book_id>/', get_book),
]
