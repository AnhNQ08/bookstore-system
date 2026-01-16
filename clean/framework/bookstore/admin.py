from django.contrib import admin
from .models import *

admin.site.register(CustomerModel)
admin.site.register(BookModel)
admin.site.register(CartModel)
admin.site.register(CartItemModel)
