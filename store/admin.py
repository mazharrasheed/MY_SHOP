from django.contrib import admin

from .models import Category, Products

# Register your models here.


class AdminProduct(admin.ModelAdmin):

    list_display=['product_name','pro_des','pro_price','category','pro_img']

admin.site.register(Products,AdminProduct)

class AdminCategory(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Category,AdminCategory)
