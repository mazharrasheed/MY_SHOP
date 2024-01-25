from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View

from ..models.category import Category
from ..models.customer import Customer
from ..models.products import Products


def index(request):

    products=None
    categories=Category.get_all_category()
    categoryID=(request.GET.get('category'))
    if categoryID:
       products=Products.get_all_produts_by_categoryid(categoryID)
    else:
         products=Products.get_all_produts()
    data={'products':products,'categories':categories}
    return render(request,"index.html",data)