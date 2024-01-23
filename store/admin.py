from django.contrib import admin
from .models.products import Products
from .models.category import Category

# Register your models here.

admin.site.register(Products)
admin.site.register(Category)
