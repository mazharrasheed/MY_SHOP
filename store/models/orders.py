
import datetime

from django.db import models

from .customer import Customer
from .products import Products

# Create your models here.

class Orders(models.Model):
    product=models.ForeignKey(Products, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    qty=models.IntegerField(default=1)
    price=models.IntegerField()
    adress=models.CharField(max_length=250,null=True)
    phone=models.CharField(max_length=16,null=True)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.product.product_name

    def place_order(self):
        self.save()
    @staticmethod
    def get_order_by_custid(customer):
        return Orders.objects.filter(customer=customer).order_by('-date')
