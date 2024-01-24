from django.db import models

# Create your models here.

class Customer(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.EmailField( )
    password=models.CharField(max_length=500)

    def register(self):
        self.save()