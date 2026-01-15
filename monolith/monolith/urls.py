from django.contrib import admin
from django.urls import path, include
from books.views import book_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book_list),          # Trang chủ
    path('books/', include('books.urls')),
    path('cart/', include('cart.urls')),
]
