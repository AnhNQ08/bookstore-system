from django.db import models


class Cart(models.Model):
    customer = models.ForeignKey(
        'accounts.Customer',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart #{self.id}"


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items'
    )
    book = models.ForeignKey(
        'books.Book',
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} item(s)"
