from django.db import models

# Create your models here.

class Customer(models.Model):
    id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.EmailField( )
    password=models.CharField(max_length=500)

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def register(self):
        self.save()

    def isExist(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            False