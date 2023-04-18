from django.contrib import admin
from products.models import Product
from products.models import Review

admin.site.register(Product)
admin.site.register(Review)
