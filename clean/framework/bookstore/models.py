from django.db import models

class CustomerModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

class BookModel(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

class CartModel(models.Model):
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItemModel(models.Model):
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
