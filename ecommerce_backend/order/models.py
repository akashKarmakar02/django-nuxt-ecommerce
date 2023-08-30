from django.db import models

from accounts.models import User
from base.models import BaseModel
from products.models import Product, ColorVariant, SizeVariant


class Cart(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color_variant = models.ForeignKey(ColorVariant, on_delete=models.CASCADE, null=True, blank=True)
    size_variant = models.ForeignKey(SizeVariant, on_delete=models.CASCADE, null=True, blank=True)
    item_count = models.IntegerField(default=1)

    class Meta:
        unique_together = ['cart', 'product']

    def __str__(self):
        return f"{self.product} ({self.item_count})"
