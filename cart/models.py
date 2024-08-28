from django.conf import settings
from django.db import models
from products.models import Product


class CartItem(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchased = models.BooleanField(default=False)
    session_key = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

    def save(self, *args, **kwargs):
        self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)
