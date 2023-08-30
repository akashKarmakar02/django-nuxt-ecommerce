from django.contrib import admin
from .models import Product, Category, SizeVariant, ColorVariant, ProductImage


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(SizeVariant)
admin.site.register(ColorVariant)
admin.site.register(ProductImage)
