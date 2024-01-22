from django.db import models

# Create your models here.

class Products(models.Model):
    product_name=models.CharField(max_length=50)
    pro_des=models.CharField(max_length=250 ,default="")
    pro_price=models.IntegerField(default=0)
    pro_img=models.ImageField(upload_to="products/")