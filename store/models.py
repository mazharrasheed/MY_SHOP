from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)

    @staticmethod
    def get_all_products():

        return Category.objects.all()

    def __str__(self):
        return self.name

class Products(models.Model):
    product_name=models.CharField(max_length=50)
    pro_des=models.CharField(max_length=250 ,default="")
    pro_price=models.IntegerField(default=0)
    pro_img=models.ImageField(upload_to="uploaded/products/")
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)

    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
           return Products.get_all_products()


    def __str__(self):
        return self.product_name