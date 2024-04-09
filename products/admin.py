from django.contrib import admin
from .models import Product, ProductLike

# Register your models here.

admin.site.register(Product)
admin.site.register(ProductLike)