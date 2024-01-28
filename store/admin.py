from django.contrib import admin

from .models.category import Category
from .models.customer import Customer
from .models.products import Products
from .models.orders import Orders

# Register your models here.

class AdminProduct(admin.ModelAdmin):

    list_display=['product_name','pro_des','pro_price','category','pro_img']

admin.site.register(Products,AdminProduct)

class AdminCategory(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Category,AdminCategory)


class AdminCustomer(admin.ModelAdmin):
    list_display=['firstname','lastname','phone','email']

admin.site.register(Customer,AdminCustomer)



admin.site.register(Orders)